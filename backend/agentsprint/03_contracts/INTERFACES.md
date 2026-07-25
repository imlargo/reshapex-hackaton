# Frozen Stage Interfaces

Status: v0.2 aligned to the supplied nine-stage flow.

These schemas freeze what crosses owners, not how an owner implements it.
Optional fields may be added compatibly; removing or redefining a required
field requires coordinator approval.

## SourceDescriptor

```json
{
  "source_id": "SRC-001",
  "name": "source name",
  "media_type": "detected media type",
  "size_bytes": 123,
  "checksum": "stable checksum",
  "status": "accepted|unsupported|failed",
  "message": "human-readable status"
}
```

## SourceInventory — Usuario 1 to Usuario 2

```json
{
  "inventory_id": "INV-001",
  "objective": "what the knowledge base must help users do",
  "sources": ["SourceDescriptor"],
  "classes": [
    {
      "source_id": "SRC-001",
      "document_class": "owner-defined",
      "language": "detected language",
      "signals": {},
      "evidence_ids": ["EVID-001"]
    }
  ],
  "limitations": []
}
```

## NormalizedKnowledgePackage — Usuario 2 to Usuario 1

```json
{
  "package_id": "PKG-001",
  "inventory_id": "INV-001",
  "content_units": [
    {
      "unit_id": "UNIT-001",
      "source_id": "SRC-001",
      "content": "normalized bounded content",
      "location": "page/section/row/chunk",
      "metadata": {},
      "evidence_ids": ["EVID-001"]
    }
  ],
  "entities": [
    {"id": "entity-id", "label": "visible label", "type": "owner-defined"}
  ],
  "relationships": [
    {
      "subject_id": "entity-id",
      "predicate": "owner-defined",
      "object_id": "entity-id",
      "evidence_ids": ["EVID-001"],
      "confidence": "low|medium|high"
    }
  ],
  "processing_report": {
    "accepted": 1,
    "failed": 0,
    "warnings": [],
    "method_summary": "owner-authored"
  }
}
```

## RagStrategyPlan and QueryableIndex — Usuario 1 to Usuario 3

The selected RAG family and technologies remain Usuario 1 decisions.

```json
{
  "plan_id": "RAG-PLAN-001",
  "package_id": "PKG-001",
  "strategy": {
    "name": "owner-selected strategy",
    "capabilities": ["supported query capability"],
    "selection_rationale": "evidence-based reason",
    "evidence_ids": ["EVID-001"],
    "limitations": []
  },
  "storage": {
    "topology": "owner-selected topology",
    "components": [],
    "selection_rationale": "evidence-based reason"
  },
  "index": {
    "index_id": "INDEX-001",
    "status": "ready|partial|failed",
    "location": "opaque location or identifier",
    "metrics": {}
  }
}
```

## ValidationReport — Usuario 3 to integration gate

```json
{
  "validation_id": "VAL-001",
  "index_id": "INDEX-001",
  "status": "ready|conditional|not_ready",
  "checks": [
    {
      "name": "owner-selected check",
      "status": "pass|warning|fail",
      "detail": "result",
      "evidence_ids": ["EVID-001"]
    }
  ],
  "limitations": [],
  "next_action": "string"
}
```

## KnowledgeQueryRequest

```json
{"index_id": "INDEX-001", "question": "non-empty grounded question"}
```

## KnowledgeAnswer

```json
{
  "answer": "string",
  "citations": [{"evidence_id": "EVID-001", "claim": "supported claim"}],
  "confidence": "low|medium|high",
  "evidence_grade": "insufficient|partial|strong",
  "unresolved_risk": "string",
  "next_action": "string",
  "sufficient_evidence": true,
  "trace": {"steps": [], "tool_events": [], "latency_ms": 0}
}
```

## ErrorEnvelope

```json
{
  "error": {
    "code": "stable_code",
    "message": "honest user-facing description",
    "retryable": false,
    "details": {}
  }
}
```

## Application boundary

Usuario 3 may mock stage records until integration. Usuario 1 owns the
transport and shared orchestration; Usuario 2 owns the semantic package
producer; Usuario 3 owns the client and validation/readiness consumer.
