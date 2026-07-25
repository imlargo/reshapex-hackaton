# Task Packet — Usuario 1: Adaptive RAG and Integration

- User / branch: Usuario 1 / `codex/adaptive-rag`
- Exact coordination-baseline SHA: pending C-02
- Owned phases: inventory and classification; research and selection of the RAG
  types the agent can implement; automatic storage design; indexing;
  retrieval/query boundary.
- Additional responsibility: agent/runtime, application boundary, shared
  integration, sequential merge, and real-provider proof.
- Decision authority: document classification approach; RAG strategy space and
  selection criteria; storage topology; indexing and retrieval methods; agent
  workflow; tools; service/transport; integration and core validation.
- Why it matters: this workstream decides how the characteristics and purpose of
  each corpus become a justified, queryable RAG implementation.
- Allowed files/directories: existing `app.py`,
  `src/agentsprint_starter/*.py`, existing `tests/test_*.py`, new
  `src/agentsprint_starter/rag/**`, `src/agentsprint_starter/service/**`,
  `tests/rag/**`, `tests/service/**`, and coordinator control/integration files.
- Forbidden/shared files: Usuario 2 and Usuario 3 owned paths; raw inbox;
  unrelated user changes.
- Frozen boundaries: produces `SourceInventory`, consumes
  `NormalizedKnowledgePackage`, produces `RagStrategyPlan`/`QueryableIndex`,
  and exposes `KnowledgeAnswer`.
- Available sources/credentials: `SRC-001`; real SICK sources and DeepSeek key
  are still missing.
- Research mandate: characterize the corpus and target questions, investigate
  viable RAG families and their trade-offs, test the riskiest selection
  assumption, and choose which approaches the agent should support and when.
  No RAG type, store, or indexing technology is prescribed by this packet.
- Completion criteria: the selected approach is evidence-backed; stage schemas
  pass; storage/index are reproducible; the bounded real-provider path calls a
  real knowledge tool and returns a cited result or honest failure.
- Required small check: owner-designed RAG comparison/experiment plus
  deterministic stage/query boundary smoke.
- Expected commit(s): research decision and experiment; implementation;
  integration/boundary evidence.
- Handoff file/evidence: `04_workstreams/handoffs/PERSON_1.md`.
- Deadline: research T+45; branch outcome T+100; integration T+125.
- Blocker/kill behavior: choose the smallest supported strategy when evidence
  does not justify complexity; raise contract/dependency changes rather than
  editing another owner's paths.
