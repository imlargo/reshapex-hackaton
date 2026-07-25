# Acceptance

## Product journey

- [ ] Real supplied material is inventoried without altering the raw source.
- [ ] Inventory/classification crosses the `SourceInventory` boundary.
- [ ] Specialized extraction, normalization, and relationship detection cross
  the `NormalizedKnowledgePackage` boundary.
- [ ] Usuario 1 selects and explains a RAG/storage/index strategy from evidence.
- [ ] Usuario 3 returns a visible `ValidationReport` before readiness.
- [ ] A reproducible knowledge-base artifact is created or an honest failure is
  returned.
- [ ] At least one representative question invokes a real knowledge tool.
- [ ] A typed, validated result is visible in the web UI.
- [ ] Every material answer claim and relationship shown has returned evidence
  support.
- [ ] Insufficient evidence, unsupported input, and processing failure remain
  understandable to the user.

## Workstream authority evidence

- [ ] Each owner records the challenge, researched options, evidence/experiment,
  selected approach, and rollback condition.
- [ ] Usuario 1 proves inventory, RAG-strategy selection, storage/indexing,
  bounded agent, retrieval, and the application boundary.
- [ ] Usuario 2 proves extraction, normalization, entity/relationship quality,
  and provenance on a representative corpus.
- [ ] Usuario 3 proves the validation/readiness gate and the primary web journey
  plus provenance/quality/trace comprehension and accessibility checks.
- [ ] No owner modifies another owner's files or shared contracts directly.

## Reliability

- [x] The real and deterministic paths traverse the compiled LangGraph.
- [x] Model messages and evidence tools use LangChain interfaces.
- [x] Agent stops at the configured step limit.
- [x] Tool calls time out explicitly.
- [x] At most one final-output repair occurs.
- [x] Invalid/invented citation IDs are rejected.
- [x] Tokens and latency are captured.
- [x] Missing-data, contradiction, and tool-failure cases are recorded.

## Delivery

- [x] Locked restore, smoke, tests, lint, and startup were green at starter
  verification.
- [ ] Boundary checks pass after every merge.
- [ ] Exact judge journey passes twice after feature freeze.
- [ ] Backup result/screenshot/video exists.
- [x] No secrets or fake-provider fallback are committed.
