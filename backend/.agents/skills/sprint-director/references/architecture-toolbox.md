# Architecture toolbox

## Mandatory core

Use deterministic intake → LangChain `ChatDeepSeek` and 3–6 typed LangChain
tools → one bounded LangGraph `StateGraph` → evidence validation with one repair
→ structured cited result → judge UI.

The minimum graph is:

```text
START -> model
model -> tools -> model
model -> require_tool -> model
model -> validate
validate -> repair -> model
validate -> END
```

Default limits: six model steps, one retry, explicit tool timeout, validated
final structure, concise tool payloads, token/latency trace, no silent provider
fallback.

## Graph expansion ladder

1. Keep the mandatory compact graph when the model only needs to select
   evidence/actions and produce a validated result.
2. Add deterministic business-stage nodes when real domain checkpoints or
   approval stages exist.
3. Add a checkpointer and interrupts when pause/resume, inspection, or
   human-in-the-loop behavior is central.
4. Add parallel graph branches only when distinct runtime roles use distinct
   evidence or tools and a reducer has a clear contract.

Do not confuse mandatory LangGraph usage with permission to build a large
workflow before the case requires it.

## Knowledge ladder

1. Direct source/structured lookup for small exact data.
2. Metadata-aware hybrid retrieval for mixed prose, tables, and IDs.
3. One adaptive retry/rerank when weak retrieval is a central demo risk.

Possible case-selected sidecars: page preview, SQL/spec tool, parent-section
expansion, reranker, or micro-graph. Use a micro-graph only for a named
relationship question that ordinary retrieval answers poorly.

## Trust loop

Retrieve → grade sufficiency → retry once if weak → create structured decision
→ verify returned citation IDs → answer with confidence or decline/escalate.
