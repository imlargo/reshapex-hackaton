from __future__ import annotations

from pathlib import Path

import pytest
from rag.factories import make_package

from agentsprint_starter.processing import (
    REPRESENTATIVE_GLOBS,
    build_inventory_from_directory,
    process_inventory,
)
from agentsprint_starter.quality import validate_knowledge_base
from agentsprint_starter.rag import (
    AdaptiveRagCompiler,
    KnowledgeBaseRequest,
    RagStrategyPlan,
    SearchAlgorithm,
    StorageTopology,
)
from agentsprint_starter.rag.contracts import (
    IndexDescription,
    SelectionSignals,
    StorageDescription,
    StrategyDescription,
)


def test_validate_ready_fixture_package() -> None:
    compiler = AdaptiveRagCompiler()
    request = KnowledgeBaseRequest(objective="Answer inspection threshold questions.")
    inventory = compiler.inventory(
        request,
        [("inspection.md", b"The inspection threshold is 500 operating hours.")],
    )
    package = make_package(
        contents=["The inspection threshold is 500 operating hours."],
        inventory_id=inventory.inventory_id,
    )
    compiled = compiler.compile(request, inventory, package)
    report = validate_knowledge_base(inventory, package, compiled.plan)

    assert report.status in {"ready", "conditional"}
    assert report.index_id == compiled.plan.index.index_id
    assert any(check.name == "index_status" for check in report.checks)
    compiled.index.close()


def test_validate_fails_without_content_units() -> None:
    compiler = AdaptiveRagCompiler()
    request = KnowledgeBaseRequest(objective="Answer support questions.")
    inventory = compiler.inventory(request, [("support.md", b"Support content.")])
    package = make_package(contents=[], inventory_id=inventory.inventory_id)
    package = package.model_copy(update={"content_units": []})
    plan = RagStrategyPlan(
        plan_id="RAG-PLAN-000000000001",
        package_id=package.package_id,
        strategy=StrategyDescription(
            name="sparse-vector",
            capabilities=["keyword"],
            selection_rationale="Fixture plan for empty package validation.",
            search_algorithm=SearchAlgorithm.TFIDF_COSINE,
        ),
        storage=StorageDescription(
            topology=StorageTopology.VECTOR,
            components=["units"],
            selection_rationale="In-memory fixture.",
        ),
        index=IndexDescription(
            index_id="INDEX-000000000001",
            status="failed",
            location="memory://fixture",
        ),
        decision_mode="automatic",
        selection_signals=SelectionSignals(
            content_units=0,
            entities=0,
            relationships=0,
            structured_ratio=0.0,
            relationship_density=0.0,
            edges_per_entity=0.0,
            cycle_surplus=0,
            relationship_intent=False,
            multihop_intent=False,
            structured_intent=False,
        ),
    )
    report = validate_knowledge_base(inventory, package, plan)

    assert report.status == "not_ready"


def test_validate_sick_representative_corpus() -> None:
    corpus_dir = Path("contents")
    if not corpus_dir.exists():
        pytest.skip("SICK corpus not available")
    inventory = build_inventory_from_directory(corpus_dir, include_globs=REPRESENTATIVE_GLOBS)
    package = process_inventory(inventory, corpus_dir).package
    compiler = AdaptiveRagCompiler()
    request = KnowledgeBaseRequest(objective=inventory.objective)
    compiled = compiler.compile(request, inventory, package)
    report = validate_knowledge_base(inventory, package, compiled.plan)

    assert report.status in {"ready", "conditional", "not_ready"}
    assert len(report.checks) >= 4
    compiled.index.close()
