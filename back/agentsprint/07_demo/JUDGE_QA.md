# Judge Q&A

## Why is this agentic?

The LangChain model chooses among typed evidence tools inside a compiled
LangGraph. Explicit graph nodes enforce limits, execute tools, validate the
result, and allow one bounded repair.

## How do you prevent hallucinated evidence?

Only IDs actually returned by a tool may survive result validation. An invalid
ID receives one repair attempt, then the run stops visibly.

## Why LangGraph but not runtime multi-agent or vector RAG?

LangGraph and LangChain are mandatory core infrastructure and make the control
flow inspectable. Runtime specialists, vector retrieval, persistence, and
interrupts remain gated by distinct-role, retrieval-quality, or
pause/resume requirements from the revealed case.

## What happens when data is missing or a tool fails?

The system returns a low-confidence insufficient-evidence result or an explicit
error. It never silently switches to a fake model or invents evidence.

## What changes in production?

Replace the lexical store with the case-selected governed retrieval/action
adapter, add auth and persistent audit traces, measure quality/latency, and
require approval for consequential actions.
