# Architecture Boundary

Status: stage topology frozen; internal methods delegated to owners.

```text
web intake [Usuario 3]
  -> SourceInventory [Usuario 1]
  -> NormalizedKnowledgePackage [Usuario 2]
  -> RagStrategyPlan + QueryableIndex [Usuario 1]
  -> ValidationReport [Usuario 3]
  -> query-ready knowledge base [integration: Usuario 1]
  -> cited web query experience [Usuario 3]
```

## Fixed constraints

- Preserve stable `SRC-*` and evidence IDs from intake to visible results.
- Never modify raw inputs in place.
- Material claims and relationship edges require returned evidence IDs.
- The runtime keeps the repository-required DeepSeek, LangChain, and bounded
  LangGraph path; no silent model fallback.
- Errors, unsupported formats, insufficient evidence, and storage limitations
  must be explicit.
- Shared schemas, root dependencies, routing, and cross-stage glue have one
  writer: Usuario 1 as coordinator.

## Delegated decision authority

| Owner | Flow stages and authority | Must preserve |
| --- | --- | --- |
| Usuario 1 — adaptive RAG and integration | Inventory/classification; research and selection of RAG types; automatic storage design; indexing; retrieval/query boundary; agent/runtime; integration | stage contracts, evidence rules, bounded execution, query-ready operability |
| Usuario 2 — semantic processing | Specialized extraction; normalization; entity and relationship detection; internal intermediate artifacts and evaluation | immutable raw sources, provenance, normalized-package contract, measurable transformation quality |
| Usuario 3 — web and validation | Web intake/query journey; validation strategy and readiness gate; quality, provenance, citation, trace, failure-state, and accessibility experience | stage contracts, honest readiness status, primary journey, production build |

An owner may research, implement, or replace an internal approach without
approval. They must raise a decision request before changing another owner's
contract, shared path, or acceptance condition.

## Owner research record

For each consequential decision, the owner records:

1. the challenge found in the supplied material or flow;
2. alternatives considered;
3. evidence or experiment used;
4. the selected approach and expected advantage;
5. limitations and a rollback/revisit condition.

No parser, RAG family, embedding model, store, graph technology, validation
method, or web framework is centrally prescribed before its owner completes
that research.
