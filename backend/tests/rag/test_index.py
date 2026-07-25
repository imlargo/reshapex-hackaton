import pytest

from agentsprint_starter.rag import (
    NormalizedKnowledgePackage,
    ProcessingReport,
    build_queryable_index,
    select_rag_strategy,
)

from .factories import complex_graph_package, make_package, simple_graph_package


def test_vector_index_ranks_relevant_evidence() -> None:
    package = make_package(
        contents=[
            "The inspection threshold is 500 operating hours.",
            "Electrical power must be isolated before opening the enclosure.",
        ]
    )
    plan = select_rag_strategy(package, "Answer maintenance questions.")
    index = build_queryable_index(package, plan)

    matches = index.search("inspection threshold", limit=1)

    assert [record.evidence_id for record in matches] == ["EVID-TEST-001"]


def test_relational_index_uses_real_sqlite_rows_and_bm25_ranking() -> None:
    package = make_package(
        contents=[
            "sku WTB4 protocol IO-Link temperature 60",
            "sku SIG200 protocol Profinet temperature 50",
        ],
        formats=["row", "row"],
    )
    plan = select_rag_strategy(package, "Filtrar tabla por protocolo.")
    index = build_queryable_index(package, plan)

    matches = index.search("IO-Link protocol", limit=1)

    assert [record.evidence_id for record in matches] == ["EVID-TEST-001"]
    index.close()


def test_simple_graph_bfs_returns_the_edge_evidence() -> None:
    package = simple_graph_package()
    plan = select_rag_strategy(package, "¿Qué protocolo es compatible con Sensor WTB4?")
    index = build_queryable_index(package, plan)

    matches = index.search("Sensor WTB4 compatible", limit=2)

    assert matches[0].evidence_id == "EVID-TEST-002"


def test_complex_graph_returns_grounded_multihop_evidence() -> None:
    package = complex_graph_package()
    plan = select_rag_strategy(
        package,
        "Ruta de impacto y dependencias con varios saltos desde Component 0.",
    )
    index = build_queryable_index(package, plan)

    matches = index.search("Component 0 impact dependencies", limit=3)

    assert matches
    assert all(record.evidence_id.startswith("EVID-TEST-") for record in matches)


def test_empty_normalized_package_fails_without_fake_index() -> None:
    package = NormalizedKnowledgePackage(
        package_id="PKG-EMPTY-001",
        inventory_id="INV-EMPTY-001",
        content_units=[],
        processing_report=ProcessingReport(
            accepted=0,
            failed=1,
            warnings=["No extractable content."],
            method_summary="Empty fixture.",
        ),
    )
    plan = select_rag_strategy(package, "Answer support questions.")

    assert plan.index.status == "failed"
    with pytest.raises(ValueError, match="without normalized content"):
        build_queryable_index(package, plan)
