from __future__ import annotations

from agentsprint_starter.rag import (
    ContentUnit,
    KnowledgeEntity,
    KnowledgeRelationship,
    NormalizedKnowledgePackage,
    ProcessingReport,
)


def make_package(
    *,
    contents: list[str],
    formats: list[str] | None = None,
    entities: list[KnowledgeEntity] | None = None,
    relationships: list[KnowledgeRelationship] | None = None,
    inventory_id: str = "INV-TEST00000001",
) -> NormalizedKnowledgePackage:
    unit_formats = formats or ["prose"] * len(contents)
    units = [
        ContentUnit(
            unit_id=f"UNIT-{index:03d}",
            source_id=f"SRC-TEST-{index:03d}",
            content=content,
            location=f"section {index}",
            metadata={"format": unit_formats[index - 1], "title": f"Unit {index}"},
            evidence_ids=[f"EVID-TEST-{index:03d}"],
        )
        for index, content in enumerate(contents, start=1)
    ]
    return NormalizedKnowledgePackage(
        package_id="PKG-TEST-001",
        inventory_id=inventory_id,
        content_units=units,
        entities=entities or [],
        relationships=relationships or [],
        processing_report=ProcessingReport(
            accepted=len(units),
            failed=0,
            warnings=[],
            method_summary="Deterministic contract fixture.",
        ),
    )


def simple_graph_package() -> NormalizedKnowledgePackage:
    entities = [
        KnowledgeEntity(id="sensor", label="Sensor WTB4", type="ProductSKU"),
        KnowledgeEntity(id="protocol", label="IO-Link", type="Protocol"),
    ]
    relationships = [
        KnowledgeRelationship(
            subject_id="sensor",
            predicate="supports_protocol",
            object_id="protocol",
            evidence_ids=["EVID-TEST-002"],
            confidence="high",
        )
    ]
    return make_package(
        contents=[
            "The WTB4 product family contains compact photoelectric sensors.",
            "Sensor WTB4 supports the IO-Link protocol.",
        ],
        entities=entities,
        relationships=relationships,
    )


def complex_graph_package() -> NormalizedKnowledgePackage:
    entities = [
        KnowledgeEntity(id=f"node-{index}", label=f"Component {index}", type="Component")
        for index in range(8)
    ]
    pairs = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 0),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    ]
    relationships = [
        KnowledgeRelationship(
            subject_id=f"node-{left}",
            predicate="depends_on",
            object_id=f"node-{right}",
            evidence_ids=[
                f"EVID-TEST-{1 + (index % 3):03d}",
            ],
            confidence="high" if index % 2 == 0 else "medium",
        )
        for index, (left, right) in enumerate(pairs)
    ]
    return make_package(
        contents=[
            "Component 0 connects the controller to the sensor chain.",
            "Components 1 through 4 describe the first dependency path.",
            "Components 5 through 7 close redundant dependency paths.",
        ],
        entities=entities,
        relationships=relationships,
    )
