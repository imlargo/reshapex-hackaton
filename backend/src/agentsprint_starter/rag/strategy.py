from __future__ import annotations

import hashlib
import re
import unicodedata
from collections.abc import Iterable

from .contracts import (
    IndexDescription,
    NormalizedKnowledgePackage,
    RagStrategyPlan,
    SearchAlgorithm,
    SelectionSignals,
    StorageDescription,
    StorageTopology,
    StrategyDescription,
)

RELATIONSHIP_TERMS = {
    "afecta",
    "belongs",
    "cadena",
    "compatible",
    "conectado",
    "connect",
    "depend",
    "depende",
    "dependency",
    "impact",
    "relacion",
    "relation",
    "requires",
    "ruta",
    "soporta",
    "supports",
}
MULTIHOP_TERMS = {
    "cadena",
    "camino",
    "dependencias",
    "impacto",
    "multihop",
    "ruta",
    "saltos",
    "transitive",
    "upstream",
}
STRUCTURED_TERMS = {
    "agrupar",
    "average",
    "campo",
    "comparar",
    "count",
    "cuantos",
    "filter",
    "filtrar",
    "listar",
    "promedio",
    "rango",
    "tabla",
}
STRUCTURED_FORMATS = {
    "csv",
    "database_row",
    "json",
    "record",
    "row",
    "structured",
    "table",
    "yaml",
}

ALGORITHMS = {
    StorageTopology.RELATIONAL: SearchAlgorithm.SQL_FILTER_BM25,
    StorageTopology.VECTOR: SearchAlgorithm.TFIDF_COSINE,
    StorageTopology.SIMPLE_GRAPH: SearchAlgorithm.BREADTH_FIRST,
    StorageTopology.COMPLEX_GRAPH: SearchAlgorithm.PERSONALIZED_PAGERANK,
}
STRATEGY_NAMES = {
    StorageTopology.RELATIONAL: "relational-rag",
    StorageTopology.VECTOR: "sparse-vector-rag",
    StorageTopology.SIMPLE_GRAPH: "simple-graph-rag",
    StorageTopology.COMPLEX_GRAPH: "weighted-graph-rag",
}
CAPABILITIES = {
    StorageTopology.RELATIONAL: [
        "exact metadata filters",
        "bounded full-text ranking",
        "structured comparison",
    ],
    StorageTopology.VECTOR: [
        "ranked retrieval across mixed prose",
        "language-agnostic token-space similarity",
    ],
    StorageTopology.SIMPLE_GRAPH: [
        "direct relationship lookup",
        "bounded breadth-first traversal",
        "evidence-backed edges",
    ],
    StorageTopology.COMPLEX_GRAPH: [
        "weighted multi-hop relationship retrieval",
        "personalized importance ranking",
        "evidence-backed edges",
    ],
}
COMPONENTS = {
    StorageTopology.RELATIONAL: ["sqlite_in_memory", "evidence_rows"],
    StorageTopology.VECTOR: ["in_memory_tfidf_vectors", "evidence_records"],
    StorageTopology.SIMPLE_GRAPH: ["in_memory_adjacency_list", "evidence_records"],
    StorageTopology.COMPLEX_GRAPH: [
        "in_memory_weighted_graph",
        "evidence_records",
    ],
}


def select_rag_strategy(
    package: NormalizedKnowledgePackage,
    objective: str,
    *,
    preferred_storage: StorageTopology | None = None,
) -> RagStrategyPlan:
    signals = selection_signals(package, objective)
    limitations = [
        "The selected adapter is local and demo-scoped; it is not a production database."
    ]
    topology = _automatic_topology(signals)
    decision_mode = "automatic"

    if preferred_storage is not None:
        decision_mode = "requested"
        topology, request_limitation = _apply_request_gate(
            preferred_storage,
            signals,
        )
        if request_limitation:
            limitations.append(request_limitation)

    if package.processing_report.failed:
        limitations.append(
            f"{package.processing_report.failed} source(s) failed semantic processing."
        )
    limitations.extend(package.processing_report.warnings)

    status = "ready"
    if not package.content_units:
        status = "failed"
        limitations.append("The normalized package has no content units to index.")
    elif package.processing_report.failed or package.processing_report.warnings:
        status = "partial"

    plan_seed = f"{package.package_id}|{objective.strip()}|{topology.value}"
    fingerprint = hashlib.sha256(plan_seed.encode("utf-8")).hexdigest()[:12].upper()
    rationale = _rationale(topology, signals, decision_mode)
    evidence_ids = list(
        dict.fromkeys(
            evidence_id
            for unit in package.content_units
            for evidence_id in unit.evidence_ids
        )
    )[:12]
    algorithm = ALGORITHMS[topology]

    return RagStrategyPlan(
        plan_id=f"RAG-PLAN-{fingerprint}",
        package_id=package.package_id,
        strategy=StrategyDescription(
            name=STRATEGY_NAMES[topology],
            capabilities=CAPABILITIES[topology],
            selection_rationale=rationale,
            evidence_ids=evidence_ids,
            limitations=limitations,
            search_algorithm=algorithm,
        ),
        storage=StorageDescription(
            topology=topology,
            components=COMPONENTS[topology],
            selection_rationale=(
                f"Use {topology.value} with {algorithm.value}; the storage and "
                "search algorithm are selected as one bounded plan."
            ),
        ),
        index=IndexDescription(
            index_id=f"INDEX-{fingerprint}",
            status=status,
            location=f"memory://{topology.value}/{fingerprint}",
            metrics={
                "content_units": signals.content_units,
                "entities": signals.entities,
                "relationships": signals.relationships,
                "structured_ratio": round(signals.structured_ratio, 4),
                "relationship_density": round(signals.relationship_density, 4),
                "edges_per_entity": round(signals.edges_per_entity, 4),
                "cycle_surplus": signals.cycle_surplus,
                "search_algorithm": algorithm.value,
            },
        ),
        decision_mode=decision_mode,
        selection_signals=signals,
    )


def selection_signals(
    package: NormalizedKnowledgePackage,
    objective: str,
) -> SelectionSignals:
    tokens = set(_tokens(objective))
    structured_units = sum(_is_structured(unit.metadata) for unit in package.content_units)
    unit_count = len(package.content_units)
    entity_count = len(package.entities)
    relationship_count = len(package.relationships)
    possible_edges = entity_count * (entity_count - 1) / 2
    density = relationship_count / possible_edges if possible_edges else 0.0
    edges_per_entity = relationship_count / entity_count if entity_count else 0.0

    return SelectionSignals(
        content_units=unit_count,
        entities=entity_count,
        relationships=relationship_count,
        structured_ratio=structured_units / unit_count if unit_count else 0.0,
        relationship_density=min(density, 1.0),
        edges_per_entity=edges_per_entity,
        cycle_surplus=_cycle_surplus(package),
        relationship_intent=bool(tokens & RELATIONSHIP_TERMS),
        multihop_intent=bool(tokens & MULTIHOP_TERMS),
        structured_intent=bool(tokens & STRUCTURED_TERMS),
    )


def _automatic_topology(signals: SelectionSignals) -> StorageTopology:
    if signals.relationship_intent and signals.relationships:
        if _complex_graph_supported(signals):
            return StorageTopology.COMPLEX_GRAPH
        return StorageTopology.SIMPLE_GRAPH
    if (
        signals.structured_ratio >= 0.75
        or signals.structured_ratio >= 0.5
        and signals.structured_intent
    ):
        return StorageTopology.RELATIONAL
    return StorageTopology.VECTOR


def _apply_request_gate(
    requested: StorageTopology,
    signals: SelectionSignals,
) -> tuple[StorageTopology, str]:
    if requested is StorageTopology.COMPLEX_GRAPH and not _complex_graph_supported(
        signals
    ):
        fallback = (
            StorageTopology.SIMPLE_GRAPH
            if signals.relationships
            else StorageTopology.VECTOR
        )
        return (
            fallback,
            (
                "Complex graph was requested but the package lacks the dense, cyclic, "
                "multi-hop evidence gate; the smallest supported topology was selected."
            ),
        )
    if requested is StorageTopology.SIMPLE_GRAPH and not signals.relationships:
        return (
            StorageTopology.VECTOR,
            (
                "Simple graph was requested but no grounded relationships were supplied; "
                "vector retrieval was selected instead."
            ),
        )
    return requested, ""


def _complex_graph_supported(signals: SelectionSignals) -> bool:
    return (
        signals.multihop_intent
        and signals.entities >= 8
        and signals.relationships >= 12
        and signals.edges_per_entity >= 1.4
        and signals.cycle_surplus >= 2
    )


def _rationale(
    topology: StorageTopology,
    signals: SelectionSignals,
    decision_mode: str,
) -> str:
    prefix = (
        "The requested preference passed the safety/complexity gate."
        if decision_mode == "requested"
        else "The objective and normalized package were evaluated automatically."
    )
    metrics = (
        f" Structured ratio={signals.structured_ratio:.2f}; "
        f"entities={signals.entities}; relationships={signals.relationships}; "
        f"edges/entity={signals.edges_per_entity:.2f}; "
        f"cycle surplus={signals.cycle_surplus}."
    )
    reasons = {
        StorageTopology.RELATIONAL: (
            " Structured records and filter/comparison behavior favor a relational "
            "row model with exact filtering before lexical ranking."
        ),
        StorageTopology.VECTOR: (
            " Mixed prose without a justified relationship traversal favors a sparse "
            "vector similarity index."
        ),
        StorageTopology.SIMPLE_GRAPH: (
            " The intended use asks about grounded relationships, while graph "
            "complexity remains suitable for bounded breadth-first traversal."
        ),
        StorageTopology.COMPLEX_GRAPH: (
            " The intended use is explicitly multi-hop and the grounded graph is "
            "dense/cyclic enough to justify weighted personalized ranking."
        ),
    }
    return prefix + reasons[topology] + metrics


def _is_structured(metadata: dict[str, str | int | float | bool]) -> bool:
    if metadata.get("structured") is True:
        return True
    values = {_normalize(str(value)) for value in metadata.values()}
    return bool(values & STRUCTURED_FORMATS)


def _cycle_surplus(package: NormalizedKnowledgePackage) -> int:
    if not package.relationships:
        return 0
    parent = {entity.id: entity.id for entity in package.entities}

    def find(node: str) -> str:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    cycles = 0
    seen_edges: set[tuple[str, str]] = set()
    for relationship in package.relationships:
        edge = tuple(sorted((relationship.subject_id, relationship.object_id)))
        if edge in seen_edges:
            cycles += 1
            continue
        seen_edges.add(edge)
        left = find(relationship.subject_id)
        right = find(relationship.object_id)
        if left == right:
            cycles += 1
        else:
            parent[left] = right
    return cycles


def _tokens(text: str) -> Iterable[str]:
    return re.findall(r"[a-z0-9]+", _normalize(text))


def _normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    return "".join(character for character in decomposed if not unicodedata.combining(character))
