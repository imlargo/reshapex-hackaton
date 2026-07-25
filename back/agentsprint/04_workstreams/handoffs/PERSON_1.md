# Handoff — Usuario 1: Adaptive RAG and Integration

## Owner decision

- Challenge discovered: the 57-file SICK corpus mixes long prose, tables,
  stable identifiers, product relationships, and repository metadata, while
  the user supplies the intended use before the documents.
- Alternatives researched: fixed local vector index; adaptive four-plan local
  compiler; production multi-store platform; plan-only deployment recipe.
- Evidence or experiment: inventory `INV-BA47AB6D8A72`; 15 focused tests cover
  four strategy decisions, downgrade behavior, four retrieval algorithms,
  typed tools, LangGraph integration, lineage mismatch, and empty-package
  failure.
- Selected approach and why: objective + normalized-corpus signals select
  SQLite/BM25, sparse TF-IDF vectors, adjacency/BFS, or exceptionally a weighted
  graph/PageRank. It maximizes visible adaptation without claiming unprovisioned
  infrastructure.
- Known trade-offs: all stores are local demo adapters; sparse vectors are not
  production embeddings; graph quality is bounded by Usuario 2's grounded
  entities and relationships.
- Rollback/revisit condition: default to vector when structured/relationship
  evidence is missing; replace local adapters only after scale, deployment, or
  residency requirements arrive.

## Delivery

- Branch: `codex/semantic-processing`, by explicit user instruction; writes
  remain inside Usuario 1/coordinator paths.
- Coordination-baseline SHA: `c1e792a`
- Functional commit SHA: `33ccfde`
- Owned outcome completed: inventory/classification, adaptive RAG plan,
  storage/index build, retrieval boundary, typed tools, and bounded runner
  integration.
- Files changed: `src/agentsprint_starter/rag/**`, `tests/rag/**`, compatible
  contract/control/README updates.
- Small test/build result: 15/15 focused tests and 33/33 repository tests pass;
  lint, deterministic smoke, control validation, and secret scan pass.
- Evidence artifact: `agentsprint/06_validation/SCORECARD.md`.
- Assumptions: objective is submitted first; Usuario 2 supplies a contract-valid
  `NormalizedKnowledgePackage`; demo storage remains local.
- Integration notes: public entry points are `KnowledgeBaseRequest`,
  `AdaptiveRagCompiler.inventory`, `AdaptiveRagCompiler.compile`,
  `CompiledKnowledgeBase.plan`, `.index`, `.tools`, and `.create_runner`.
- Contract/dependency change requests: none; no new root dependency.
- Known limitations: no real DeepSeek proof without local key; no production
  database provisioning; UI and real normalized-package integration remain
  owned by Usuarios 3 and 2 respectively.
