from __future__ import annotations

import re
from dataclasses import dataclass

from .entities import FAMILY_HINTS, EntityHit

ORDERING_LINE = re.compile(
    r"(?P<sku>[A-Z0-9]{2,5}[A-Z]?[-][A-Z0-9-]{3,}).{0,80}?(?P<order>\d{7})",
    re.I,
)
SKU_IN_FILENAME = re.compile(r"dataSheet_([A-Z0-9-]+)_(\d{7})_", re.I)


@dataclass(frozen=True)
class RelationshipHit:
    subject_id: str
    predicate: str
    object_id: str
    evidence_ids: list[str]
    confidence: str


def detect_relationships(
    units: list[dict],
    entities: list[EntityHit],
    evidence_map: dict[str, list[str]],
) -> tuple[list[RelationshipHit], list[str]]:
    by_label = {entity.label.casefold(): entity for entity in entities}
    by_id = {entity.entity_id: entity for entity in entities}
    hits: dict[tuple[str, str, str], RelationshipHit] = {}
    warnings: list[str] = []

    for unit in units:
        text = unit["content"]
        evidence_ids = evidence_map.get(unit["unit_id"], [])
        source_name = str(unit.get("metadata", {}).get("source_name", ""))

        filename_match = SKU_IN_FILENAME.search(source_name)
        if filename_match:
            sku = filename_match.group(1)
            order_no = filename_match.group(2)
            sku_entity = _find_entity(by_label, sku)
            order_entity = _find_entity(by_label, order_no)
            if sku_entity and order_entity:
                _add_relation(
                    hits,
                    sku_entity.entity_id,
                    "has_order_number",
                    order_entity.entity_id,
                    evidence_ids,
                    "high",
                )
                family = _family_for_sku(sku)
                family_entity = _find_entity(by_label, family)
                if family_entity:
                    _add_relation(
                        hits,
                        sku_entity.entity_id,
                        "belongs_to_family",
                        family_entity.entity_id,
                        evidence_ids,
                        "high",
                    )

        for match in ORDERING_LINE.finditer(text):
            sku = match.group("sku")
            order_no = match.group("order")
            sku_entity = _find_entity(by_label, sku)
            order_entity = _find_entity(by_label, order_no)
            if sku_entity and order_entity:
                _add_relation(
                    hits,
                    sku_entity.entity_id,
                    "has_order_number",
                    order_entity.entity_id,
                    evidence_ids,
                    "medium",
                )

        lowered = text.lower()
        if "sig200" in lowered or "sig 200" in lowered:
            sig_entity = _find_entity(by_label, "SIG200") or by_id.get("family-sig200")
            if sig_entity:
                for protocol in ("Profinet", "EtherNet/IP", "REST API"):
                    if protocol.casefold().replace("/", "") in lowered.replace("/", ""):
                        protocol_entity = _find_entity(by_label, protocol)
                        if protocol_entity:
                            _add_relation(
                                hits,
                                sig_entity.entity_id,
                                "supports_protocol",
                                protocol_entity.entity_id,
                                evidence_ids,
                                "medium",
                            )

        if "io-link" in lowered or "io link" in lowered:
            io_entity = _find_entity(by_label, "IO-Link")
            if io_entity:
                for entity in entities:
                    if (
                        entity.entity_type == "ProductSKU"
                        and entity.label.upper().startswith("WTB")
                        and evidence_ids
                    ):
                        _add_relation(
                            hits,
                            entity.entity_id,
                            "supports_protocol",
                            io_entity.entity_id,
                            evidence_ids[:1],
                            "low",
                        )

    if not hits:
        warnings.append("No relationships extracted; corpus may need richer ordering tables")

    return list(hits.values()), warnings


def _family_for_sku(sku: str) -> str:
    upper = sku.upper()
    for hint in sorted(FAMILY_HINTS, key=len, reverse=True):
        if upper.startswith(hint):
            return FAMILY_HINTS[hint]
    if upper.startswith("WTB"):
        return "WTB4"
    return "W4"


def _find_entity(by_label: dict[str, EntityHit], label: str) -> EntityHit | None:
    return by_label.get(label.casefold())


def _add_relation(
    hits: dict[tuple[str, str, str], RelationshipHit],
    subject_id: str,
    predicate: str,
    object_id: str,
    evidence_ids: list[str],
    confidence: str,
) -> None:
    if not evidence_ids:
        return
    key = (subject_id, predicate, object_id)
    existing = hits.get(key)
    merged = sorted(set((existing.evidence_ids if existing else []) + evidence_ids))[:12]
    hits[key] = RelationshipHit(
        subject_id=subject_id,
        predicate=predicate,
        object_id=object_id,
        evidence_ids=merged,
        confidence=confidence if not existing else _max_confidence(existing.confidence, confidence),
    )


def _max_confidence(left: str, right: str) -> str:
    order = {"low": 0, "medium": 1, "high": 2}
    return left if order[left] >= order[right] else right
