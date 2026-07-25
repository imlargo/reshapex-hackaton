from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agentsprint_starter.rag import (
    ContentUnit,
    KnowledgeEntity,
    KnowledgeRelationship,
    NormalizedKnowledgePackage,
    ProcessingReport,
    SourceInventory,
    SourceStatus,
)

from .entities import detect_entities
from .extract import extract_file
from .inventory import package_id_for_inventory, resolve_source_path, stable_evidence_id
from .normalize import normalize_segments
from .relations import detect_relationships


@dataclass(frozen=True)
class ProcessingOutcome:
    package: NormalizedKnowledgePackage
    evidence_rows: list[dict]


def process_inventory(
    inventory: SourceInventory,
    corpus_dir: Path,
    *,
    package_id: str | None = None,
) -> ProcessingOutcome:
    corpus_dir = corpus_dir.resolve()

    raw_units: list[dict] = []
    evidence_rows: list[dict] = []
    warnings: list[str] = []
    failed_sources = 0
    accepted_sources = 0

    for source in inventory.sources:
        if source.status is not SourceStatus.ACCEPTED:
            failed_sources += 1
            warnings.append(f"Skipped {source.source_id} ({source.name}): {source.message}")
            continue

        path = resolve_source_path(corpus_dir, source.name)
        if not path.exists():
            failed_sources += 1
            warnings.append(f"Missing file for {source.source_id}: {path}")
            continue

        extraction = extract_file(path)
        if extraction.failed or not extraction.segments:
            failed_sources += 1
            warnings.extend(extraction.warnings)
            continue

        accepted_sources += 1
        warnings.extend(extraction.warnings)
        normalized_units, unit_warnings = normalize_segments(
            extraction.segments,
            source_id=source.source_id,
            source_name=source.name,
        )
        warnings.extend(unit_warnings)

        for offset, unit in enumerate(normalized_units, start=1):
            evidence_id = stable_evidence_id(source.source_id, offset, unit["content"])
            unit["evidence_ids"] = [evidence_id]
            raw_units.append(unit)
            evidence_rows.append(
                {
                    "evidence_id": evidence_id,
                    "source_id": source.source_id,
                    "unit_id": unit["unit_id"],
                    "location": unit["location"],
                    "source_name": source.name,
                }
            )

    for index, unit in enumerate(raw_units, start=1):
        unit["unit_id"] = f"UNIT-{index:04d}"
        evidence_rows[index - 1]["unit_id"] = unit["unit_id"]

    evidence_map = {unit["unit_id"]: unit["evidence_ids"] for unit in raw_units}
    entity_hits, entity_warnings = detect_entities(raw_units, evidence_map)
    warnings.extend(entity_warnings)
    relation_hits, relation_warnings = detect_relationships(raw_units, entity_hits, evidence_map)
    warnings.extend(relation_warnings)

    content_units = [ContentUnit(**unit) for unit in raw_units]
    entities = [
        KnowledgeEntity(id=hit.entity_id, label=hit.label, type=hit.entity_type)
        for hit in entity_hits
    ]
    relationships = [
        KnowledgeRelationship(
            subject_id=hit.subject_id,
            predicate=hit.predicate,
            object_id=hit.object_id,
            evidence_ids=hit.evidence_ids,
            confidence=hit.confidence,  # type: ignore[arg-type]
        )
        for hit in relation_hits
    ]

    method_summary = (
        "Hybrid pdftotext/HTML extraction, paragraph chunking (1800 chars), "
        "regex entity detection for SKU/order/IM/protocol/family, and "
        "rule-based relationships from ordering tables and product metadata."
    )[:1000]

    resolved_package_id = package_id or package_id_for_inventory(inventory.inventory_id)
    if not content_units:
        warnings.append("No content units extracted; returning empty normalized package.")
    package = NormalizedKnowledgePackage(
        package_id=resolved_package_id,
        inventory_id=inventory.inventory_id,
        content_units=content_units,
        entities=entities,
        relationships=relationships,
        processing_report=ProcessingReport(
            accepted=accepted_sources,
            failed=failed_sources,
            warnings=warnings[:50],
            method_summary=method_summary,
        ),
    )
    return ProcessingOutcome(package=package, evidence_rows=evidence_rows)


def write_cleaned_artifacts(
    inventory: SourceInventory,
    corpus_dir: Path,
    output_dir: Path,
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for source in inventory.sources:
        if source.status is not SourceStatus.ACCEPTED:
            continue
        path = resolve_source_path(corpus_dir, source.name)
        if not path.exists():
            continue
        extraction = extract_file(path)
        if extraction.failed:
            continue
        text = "\n\n".join(segment.text for segment in extraction.segments)
        safe_name = source.source_id.replace("/", "-")
        target = output_dir / f"{safe_name}_{path.stem}.md"
        target.write_text(text, encoding="utf-8")
        written.append(target)
    return written
