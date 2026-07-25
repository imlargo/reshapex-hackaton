# Branch Plan

Status: prepared; do not create feature branches until the team replaces person
labels, answers the P0 intake questions, and commits the coordination baseline.

## Gate

- [x] Three independent outcome areas exist.
- [x] Cross-workstream stage records are frozen at v0.2.
- [x] Writable paths do not overlap.
- [x] Each branch can work from contract fixtures without unmerged peer code.
- [x] Every branch has an outcome-level completion condition and small check.
- [x] Expected parallel research/build time exceeds coordination and merge cost.
- [ ] Coordination baseline committed and exact SHA copied into all packets.

| User | Branch | Base SHA | Owned outcome | Allowed paths | Forbidden/shared paths | Small check |
| --- | --- | --- | --- | --- | --- | --- |
| Usuario 1 | `codex/adaptive-rag` | pending baseline commit | inventory, adaptive RAG/storage/index/query, runtime, integration | existing `app.py`, `src/agentsprint_starter/*.py`, existing `tests/test_*.py`, new `src/agentsprint_starter/rag/**`, `src/agentsprint_starter/service/**`, `tests/rag/**`, `tests/service/**`, coordinator control/integration files | Usuario 2 and Usuario 3 paths; raw inbox | RAG decision experiment plus deterministic query boundary smoke |
| Usuario 2 | `codex/semantic-processing` | pending baseline commit | extraction, normalization, entities, relationships | `src/agentsprint_starter/processing/**`, `tests/processing/**`, `agentsprint/05_knowledge/**`, own handoff file | existing core, RAG/service, web/quality, root/shared config, contracts, raw inbox | representative-corpus transformation and schema check |
| Usuario 3 | `codex/web-validation` | pending baseline commit | web journey plus validation/readiness | `web/**`, `src/agentsprint_starter/quality/**`, `tests/quality/**`, own handoff file, pre-integration UI evidence under `web/evidence/**` | core/RAG/service, processing, root/shared config, contracts, control room | validation fixture check plus production web build |

If an owner needs a root dependency or contract change, they record a request
in their handoff; Usuario 1 is the only writer who applies it.
