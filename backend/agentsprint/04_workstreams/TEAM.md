# Team and Execution Mode

| Field | Value |
| --- | --- |
| Participant count | 3 |
| Coordinator / integrator | Usuario 1; replace with real name before branch activation |
| User identifiers | Usuario 1 — adaptive RAG/integration; Usuario 2 — semantic processing; Usuario 3 — web/validation |
| Selected mode | `independent branch fan-out` after coordination-baseline commit |
| Rationale | The supplied flow can cross three stable records while each owner researches independently in non-overlapping paths |
| Shared/coordinator-owned paths | contracts, manifests, root dependencies, shared schemas, routing, integration glue, control room |
| Feature freeze | T+150 unless organizer material changes it |

## Authority model

Each person owns a result and its internal technical decisions. Within their
write scope they have authority to research, compare, select, implement, and
replace their approach. Their handoff records the evidence behind consequential
decisions and the rollback condition.

Coordination is required only when a decision:

- changes a frozen stage record or acceptance condition;
- writes outside the owner's assigned paths;
- adds or changes a shared/root dependency;
- changes the primary journey, evidence rules, or freeze date;
- creates a security, privacy, licensing, or secret-management risk.

## Phase ownership

| Usuario | Owned phases | Additional responsibility | Final evidence |
| --- | --- | --- | --- |
| Usuario 1 | Inventory/classification; research and selection of RAG types; automatic storage design; indexing; retrieval/query boundary | Agent/runtime, shared integration, sequential merge, real-provider proof | RAG comparison/experiment plus real model/tool/query trace |
| Usuario 2 | Specialized extraction; normalization; entity and relationship detection | Transformation quality and source lineage | representative-corpus experiment plus normalized package |
| Usuario 3 | Web intake and query experience; validation and readiness gate | Provenance, quality, citations, trace, failure states, accessibility | production build plus validation evidence and journey recording |
