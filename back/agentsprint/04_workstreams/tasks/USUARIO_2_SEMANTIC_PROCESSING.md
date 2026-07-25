# Task Packet — Usuario 2: Semantic Processing

- User / branch: Usuario 2 / `codex/semantic-processing`
- Exact coordination-baseline SHA: pending C-02
- Owned phases: specialized extraction; normalization; entity detection; and
  relationship detection.
- Additional responsibility: transformation quality, source lineage, and
  representative-corpus evidence.
- Decision authority: extraction methods, format-specific handling,
  normalization rules, intermediate representation, entity strategy,
  relationship taxonomy and extraction, confidence handling, and evaluation.
- Why it matters: this workstream converts heterogeneous material into grounded
  semantic units that different RAG strategies can safely consume.
- Allowed files/directories:
  `src/agentsprint_starter/processing/**`, `tests/processing/**`,
  `agentsprint/05_knowledge/**`, and own handoff file.
- Forbidden/shared files: existing core, RAG/service, web/quality, root
  dependencies, shared contracts/control files, and mutation of
  `00_inbox/raw/**`.
- Frozen boundaries: consumes `SourceInventory`; produces
  `NormalizedKnowledgePackage`.
- Available sources/credentials: `SRC-001`; representative corpus not supplied.
- Research mandate: inspect the actual corpus, identify the difficult extraction
  and semantic problems, compare candidate approaches, test risky assumptions,
  and choose the strongest method. No parser, ontology, entity model, relation
  method, or intermediate format is prescribed internally.
- Completion criteria: a representative inventory produces a schema-valid
  normalized package or honest failure; every content unit and relation retains
  source/evidence lineage; quality limitations are measurable and visible.
- Required small check: owner-designed representative-corpus experiment and
  normalized-package schema check.
- Expected commit(s): research decision/experiment; implementation;
  transformation evaluation evidence.
- Handoff file/evidence: `04_workstreams/handoffs/PERSON_2.md`.
- Deadline: research T+45; branch outcome T+100.
- Blocker/kill behavior: prefer a defensible smaller method when the corpus does
  not support complex extraction; request shared changes instead of editing
  shared files.
