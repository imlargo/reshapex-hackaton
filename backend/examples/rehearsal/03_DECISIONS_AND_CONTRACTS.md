# Rehearsal Decisions and Contracts

## Recorded decisions

- Journey: asset-specific evidence-grade triage.
- Differentiator: an evidence sufficiency gate that retries once and declines
  unsafe/unsupported actions.
- Orchestration: one bounded LangGraph with model, tool, validation, and repair
  nodes.
- UI/model: Streamlit; LangChain `ChatDeepSeek` using DeepSeek V4 Flash in a
  non-thinking tool loop.
- Execution: main-only.

Three participants are available, but the slice is small and UI/runner
contracts may move during the first real call. Others perform source review,
manual failure tests, and pitch rehearsal without concurrent feature edits.

Request: `{asset_id, symptom}` plus indexed evidence.

Result: `{answer, citations, confidence, evidence_grade, unresolved_risk,
next_action, sufficient_evidence}`.

Acceptance: exact asset and source tools are visible; citation IDs came from
tools; unsupported inputs decline; trace has model/tool/tokens/latency; exact
UI journey passes twice.
