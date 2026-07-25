from __future__ import annotations

import re
from dataclasses import dataclass

SKU_PATTERN = re.compile(
    r"\b([A-Z]{2,5}[0-9]{0,2}[A-Z]?[-][A-Z0-9]{3,}(?:[-][A-Z0-9]{3,})*)\b"
)
ORDER_NUMBER_PATTERN = re.compile(
    r"\b(?:Order(?:ing)?(?:\s+No\.?|\s+number)?[:\s]+)?(\d{7})\b",
    re.I,
)
IM_DOC_PATTERN = re.compile(r"\bIM(\d{7})\b", re.I)
KA_ARTICLE_PATTERN = re.compile(r"\bKA-(\d{5})\b", re.I)
PROTOCOL_TERMS = {
    "profinet": "Profinet",
    "ethernet/ip": "EtherNet/IP",
    "ethernet ip": "EtherNet/IP",
    "io-link": "IO-Link",
    "io link": "IO-Link",
    "rest api": "REST API",
    "modbus tcp": "Modbus TCP",
    "canopen": "CANopen",
}
FAMILY_HINTS = {
    "W4": "W4",
    "WTB4": "WTB4",
    "WTB4S": "WTB4S",
    "WTB4FP": "WTB4FP",
    "WTB4FT": "WTB4FT",
    "SIG200": "SIG200",
    "SIG350": "SIG350",
}


@dataclass(frozen=True)
class EntityHit:
    entity_id: str
    label: str
    entity_type: str
    evidence_ids: list[str]
    unit_id: str


def detect_entities(
    units: list[dict],
    evidence_map: dict[str, list[str]],
) -> tuple[list[EntityHit], list[str]]:
    hits: dict[str, EntityHit] = {}
    warnings: list[str] = []

    for unit in units:
        text = unit["content"]
        unit_id = unit["unit_id"]
        evidence_ids = evidence_map.get(unit_id, [])
        if not evidence_ids:
            warnings.append(f"{unit_id} has no mapped evidence IDs during entity detection")

        for match in SKU_PATTERN.finditer(text):
            sku = match.group(1)
            if _is_noise_sku(sku):
                continue
            entity_id = _slug(f"sku-{sku}")
            _register(hits, entity_id, sku, "ProductSKU", evidence_ids, unit_id)

        for match in ORDER_NUMBER_PATTERN.finditer(text):
            order_no = match.group(1)
            entity_id = _slug(f"order-{order_no}")
            _register(hits, entity_id, order_no, "OrderNumber", evidence_ids, unit_id)

        for match in IM_DOC_PATTERN.finditer(text):
            doc_id = f"IM{match.group(1)}"
            entity_id = _slug(f"doc-{doc_id.lower()}")
            _register(hits, entity_id, doc_id, "DocumentID", evidence_ids, unit_id)

        for match in KA_ARTICLE_PATTERN.finditer(text):
            article = f"KA-{match.group(1)}"
            entity_id = _slug(f"kb-{article.lower()}")
            _register(hits, entity_id, article, "KnowledgeBaseArticle", evidence_ids, unit_id)

        lowered = text.lower()
        for needle, label in PROTOCOL_TERMS.items():
            if needle in lowered:
                entity_id = _slug(f"protocol-{label.lower()}")
                _register(hits, entity_id, label, "Protocol", evidence_ids, unit_id)

        for needle, label in FAMILY_HINTS.items():
            if re.search(rf"\b{re.escape(needle)}\b", text):
                entity_id = _slug(f"family-{label.lower()}")
                _register(hits, entity_id, label, "ProductFamily", evidence_ids, unit_id)

        if "sick assethub" in lowered or "assethub" in lowered:
            _register(
                hits,
                "product-sick-assethub",
                "SICK AssetHub",
                "SoftwareProduct",
                evidence_ids,
                unit_id,
            )

    return list(hits.values()), warnings


def _register(
    hits: dict[str, EntityHit],
    entity_id: str,
    label: str,
    entity_type: str,
    evidence_ids: list[str],
    unit_id: str,
) -> None:
    existing = hits.get(entity_id)
    merged_evidence = sorted(set((existing.evidence_ids if existing else []) + evidence_ids))
    hits[entity_id] = EntityHit(
        entity_id=entity_id,
        label=label,
        entity_type=entity_type,
        evidence_ids=merged_evidence,
        unit_id=unit_id,
    )


def _is_noise_sku(value: str) -> bool:
    if len(value) < 5:
        return True
    if value.startswith("IM") or value.startswith("KA-"):
        return True
    if value.isdigit():
        return True
    return False


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug[:80]
