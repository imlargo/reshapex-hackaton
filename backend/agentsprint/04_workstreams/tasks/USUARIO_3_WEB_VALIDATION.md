# Task Packet — Usuario 3: Web and Validation

- User / branch: Usuario 3 / `codex/web-validation`
- Exact coordination-baseline SHA: pending C-02
- Owned phases: web intake of supplied information; knowledge-base validation;
  query-ready sign-off; web query experience.
- Additional responsibility: make build decisions, provenance, quality,
  citations, agent activity, limitations, and failure states understandable
  without revealing hidden chain-of-thought.
- Decision authority: web stack, application structure, interaction and visual
  model, validation/readiness strategy, state management, visualization,
  responsive/accessibility approach, and tests for this workstream.
- Why it matters: this workstream proves both that the generated base is ready
  and that users can understand and trust the result.
- Allowed files/directories: `web/**`,
  `src/agentsprint_starter/quality/**`, `tests/quality/**`, own handoff file,
  and pre-integration UI evidence under `web/evidence/**`.
- Forbidden/shared files: core/RAG/service, semantic processing, root
  dependencies, shared contracts/control files, and raw inbox.
- Frozen boundaries: provides source input; consumes `RagStrategyPlan` and
  `QueryableIndex`; produces `ValidationReport`; consumes `KnowledgeAnswer`.
- Available sources/credentials: `SRC-001`; official SICK brand assets are not
  supplied and must not be invented.
- Research mandate: investigate the primary user's flow and the failure modes
  that determine readiness, compare validation and experience approaches, test
  the riskiest comprehension/integration assumption, and select the method. No
  web framework, validation framework, or visual pattern is prescribed.
- Completion criteria: validation can classify ready/conditional/not-ready with
  evidence; production web build passes; fixtures cover the primary journey and
  honest partial/failure states; trust information is comprehensible and
  accessible.
- Required small check: owner-selected validation experiment plus production
  build, contract-fixture journey, and accessibility evidence.
- Expected commit(s): research/validation/experience decision; implementation;
  build and validation evidence.
- Handoff file/evidence: `04_workstreams/handoffs/PERSON_3.md`.
- Deadline: research T+45; branch outcome T+100.
- Blocker/kill behavior: protect the primary journey and readiness gate; cut
  secondary visuals before changing contracts or delaying the build.
