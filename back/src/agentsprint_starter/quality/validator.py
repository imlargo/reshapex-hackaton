from __future__ import annotations

import hashlib

from agentsprint_starter.rag import (
    NormalizedKnowledgePackage,
    RagStrategyPlan,
    SourceInventory,
    SourceStatus,
)

from .schemas import ValidationCheck, ValidationReport


def validate_knowledge_base(
    inventory: SourceInventory,
    package: NormalizedKnowledgePackage,
    plan: RagStrategyPlan,
) -> ValidationReport:
    checks: list[ValidationCheck] = []
    limitations = list(inventory.limitations)

    accepted = sum(1 for source in inventory.sources if source.status is SourceStatus.ACCEPTED)
    checks.append(
        ValidationCheck(
            name="inventory_accepted_sources",
            status="pass" if accepted else "fail",
            detail=f"{accepted} accepted source(s) in inventory.",
            evidence_ids=_sample_evidence(package, limit=3),
        )
    )

    checks.append(
        ValidationCheck(
            name="semantic_content_units",
            status="pass" if package.content_units else "fail",
            detail=f"{len(package.content_units)} normalized content unit(s).",
            evidence_ids=_sample_evidence(package, limit=3),
        )
    )

    checks.append(
        ValidationCheck(
            name="processing_failures",
            status="pass" if package.processing_report.failed == 0 else "warning",
            detail=(
                f"accepted={package.processing_report.accepted}, "
                f"failed={package.processing_report.failed}"
            ),
            evidence_ids=_sample_evidence(package, limit=2),
        )
    )

    relationship_ok = all(rel.evidence_ids for rel in package.relationships)
    checks.append(
        ValidationCheck(
            name="relationship_lineage",
            status="pass" if relationship_ok else "fail",
            detail=f"{len(package.relationships)} relationship(s) with evidence lineage.",
            evidence_ids=_relationship_evidence(package, limit=6),
        )
    )

    index_status = plan.index.status
    if index_status == "ready":
        index_check_status = "pass"
    elif index_status == "partial":
        index_check_status = "warning"
    else:
        index_check_status = "fail"
    checks.append(
        ValidationCheck(
            name="index_status",
            status=index_check_status,
            detail=f"Index {plan.index.index_id} status={index_status}.",
            evidence_ids=_sample_evidence(package, limit=2),
        )
    )

    if package.processing_report.warnings:
        limitations.extend(package.processing_report.warnings[:5])
        checks.append(
            ValidationCheck(
                name="processing_warnings",
                status="warning",
                detail=f"{len(package.processing_report.warnings)} processing warning(s) recorded.",
                evidence_ids=_sample_evidence(package, limit=2),
            )
        )

    fail_count = sum(1 for check in checks if check.status == "fail")
    warn_count = sum(1 for check in checks if check.status == "warning")
    if fail_count:
        status = "not_ready"
        next_action = "Fix failed readiness checks before exposing query in the UI."
    elif warn_count:
        status = "conditional"
        next_action = "Query may proceed with visible limitations and warnings."
    else:
        status = "ready"
        next_action = "Knowledge base is ready for grounded queries."

    seed = f"{inventory.inventory_id}:{package.package_id}:{plan.plan_id}"
    validation_id = "VAL-" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12].upper()

    return ValidationReport(
        validation_id=validation_id,
        index_id=plan.index.index_id,
        status=status,
        checks=checks,
        limitations=limitations[:12],
        next_action=next_action,
    )


def _sample_evidence(package: NormalizedKnowledgePackage, *, limit: int) -> list[str]:
    return [unit.evidence_ids[0] for unit in package.content_units[:limit] if unit.evidence_ids]


def _relationship_evidence(package: NormalizedKnowledgePackage, *, limit: int) -> list[str]:
    ids: list[str] = []
    for relation in package.relationships:
        ids.extend(relation.evidence_ids)
        if len(ids) >= limit:
            break
    return ids[:limit]
