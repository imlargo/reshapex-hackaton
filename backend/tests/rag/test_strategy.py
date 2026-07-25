from agentsprint_starter.rag import (
    SearchAlgorithm,
    StorageTopology,
    select_rag_strategy,
)

from .factories import (
    complex_graph_package,
    make_package,
    simple_graph_package,
)


def test_mixed_prose_selects_vector_similarity() -> None:
    package = make_package(
        contents=[
            "Operating instructions explain installation and commissioning.",
            "A support article describes a firmware troubleshooting procedure.",
        ]
    )

    plan = select_rag_strategy(package, "Answer technical support questions.")

    assert plan.storage.topology is StorageTopology.VECTOR
    assert plan.strategy.search_algorithm is SearchAlgorithm.TFIDF_COSINE


def test_structured_filter_use_selects_relational_search() -> None:
    package = make_package(
        contents=[
            "sku,temperature,protocol\nWTB4,-40..60,IO-Link",
            "sku,temperature,protocol\nSIG200,-25..50,Profinet",
        ],
        formats=["csv", "table"],
    )

    plan = select_rag_strategy(
        package,
        "Filtrar la tabla por protocolo y comparar el rango de temperatura.",
    )

    assert plan.storage.topology is StorageTopology.RELATIONAL
    assert plan.strategy.search_algorithm is SearchAlgorithm.SQL_FILTER_BM25


def test_direct_relationship_use_selects_simple_graph() -> None:
    plan = select_rag_strategy(
        simple_graph_package(),
        "¿Qué protocolo es compatible con el Sensor WTB4?",
    )

    assert plan.storage.topology is StorageTopology.SIMPLE_GRAPH
    assert plan.strategy.search_algorithm is SearchAlgorithm.BREADTH_FIRST


def test_dense_multihop_use_is_the_only_automatic_complex_graph_path() -> None:
    plan = select_rag_strategy(
        complex_graph_package(),
        "Mostrar la ruta de impacto y dependencias con varios saltos desde Component 0.",
    )

    assert plan.storage.topology is StorageTopology.COMPLEX_GRAPH
    assert plan.strategy.search_algorithm is SearchAlgorithm.PERSONALIZED_PAGERANK
    assert plan.selection_signals.cycle_surplus >= 2


def test_complex_graph_request_downgrades_when_complexity_is_not_grounded() -> None:
    plan = select_rag_strategy(
        simple_graph_package(),
        "Mostrar la relación compatible con Sensor WTB4.",
        preferred_storage=StorageTopology.COMPLEX_GRAPH,
    )

    assert plan.storage.topology is StorageTopology.SIMPLE_GRAPH
    assert any(
        "Complex graph was requested" in limitation
        for limitation in plan.strategy.limitations
    )
