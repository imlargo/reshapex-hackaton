from __future__ import annotations

from pathlib import Path

import pytest

from agentsprint_starter.config import Settings
from agentsprint_starter.processing import (
    REPRESENTATIVE_GLOBS,
    build_inventory_from_directory,
    process_inventory,
)
from agentsprint_starter.rag import AdaptiveRagCompiler, KnowledgeBaseRequest, NormalizedKnowledgePackage
from agentsprint_starter.testing import DeterministicChatModel


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


@pytest.fixture(scope="session")
def corpus_dir(repo_root: Path) -> Path:
    path = repo_root / "contents"
    if not path.exists():
        pytest.skip("SICK contents corpus not available")
    return path


@pytest.fixture(scope="session")
def representative_inventory(corpus_dir: Path):
    return build_inventory_from_directory(corpus_dir, include_globs=REPRESENTATIVE_GLOBS)


@pytest.fixture(scope="session")
def representative_outcome(representative_inventory, corpus_dir: Path):
    return process_inventory(representative_inventory, corpus_dir)


def test_representative_inventory_has_accepted_sources(representative_inventory) -> None:
    assert len(representative_inventory.sources) >= 5
    assert any(source.status.value == "accepted" for source in representative_inventory.sources)


def test_normalized_package_schema_valid(representative_outcome) -> None:
    package = representative_outcome.package
    validated = NormalizedKnowledgePackage.model_validate(package.model_dump(mode="json"))
    assert validated.content_units
    assert validated.processing_report.accepted >= 1
    assert validated.inventory_id == representative_outcome.package.inventory_id


def test_every_content_unit_has_evidence_ids(representative_outcome) -> None:
    for unit in representative_outcome.package.content_units:
        assert unit.evidence_ids
        assert unit.source_id.startswith("SRC-")


def test_relationships_are_grounded(representative_outcome) -> None:
    package = representative_outcome.package
    if not package.relationships:
        pytest.skip("No relationships extracted from representative subset")
    known_evidence = {
        evidence_id for unit in package.content_units for evidence_id in unit.evidence_ids
    }
    for relation in package.relationships:
        assert relation.evidence_ids
        assert set(relation.evidence_ids).issubset(known_evidence)
        assert relation.confidence in {"low", "medium", "high"}


def test_expected_wtb4s_order_number_relation(representative_outcome) -> None:
    package = representative_outcome.package
    order_entity = next(
        (entity for entity in package.entities if entity.label == "1042061"),
        None,
    )
    sku_entity = next(
        (entity for entity in package.entities if entity.label.upper().startswith("WTB4S")),
        None,
    )
    if not order_entity or not sku_entity:
        pytest.skip("Expected WTB4S / 1042061 entities not found in subset")
    matching = [
        rel
        for rel in package.relationships
        if rel.subject_id == sku_entity.id
        and rel.predicate == "has_order_number"
        and rel.object_id == order_entity.id
    ]
    assert matching, "Missing has_order_number relation for WTB4S datasheet"


def test_honest_failure_for_missing_source(corpus_dir: Path, representative_inventory) -> None:
    broken = representative_inventory.model_copy(deep=True)
    broken.sources[0].name = "does-not-exist/missing.pdf"
    outcome = process_inventory(broken, corpus_dir)
    assert outcome.package.processing_report.failed >= 1
    assert outcome.package.processing_report.warnings


def test_end_to_end_compile_with_usuario1_rag(
    representative_inventory,
    representative_outcome,
) -> None:
    compiler = AdaptiveRagCompiler()
    request = KnowledgeBaseRequest(objective=representative_inventory.objective)
    package = representative_outcome.package

    compiled = compiler.compile(request, representative_inventory, package)
    tool_result = compiled.tools.execute(
        "search_evidence",
        {"query": "WTB4S Profinet order number", "limit": 3},
    )
    runner = compiled.create_runner(
        DeterministicChatModel(),
        settings=Settings(_env_file=None),
    )
    outcome = runner.run("Which order number matches WTB4S-3N2131?")

    assert tool_result["evidence"]
    assert outcome.result.citations
    assert any(event.kind == "tool" for event in outcome.trace.events)
    compiled.index.close()
