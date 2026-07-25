# Technical Checklist

For each selected component capture purpose, justification, source, proof,
latency/token tradeoff, and production change.

| Component | Purpose / justification | Source | Proof | Tradeoff | Production change |
| --- | --- | --- | --- | --- | --- |
| Bounded LangGraph | explicit model/tools/validate/repair control flow | `src/agentsprint_starter/runner.py` | compiled-graph test + node traces | graph dependency | add checkpointer/interrupts |
| LangChain model/tools | standard DeepSeek, message, and tool interfaces | `provider.py`, `tools.py` | integration tests + tool schemas | provider integration package | callbacks/LangSmith if justified |
| Typed evidence tools | grounded knowledge path | `tools.py` | tool tests + UI citations | lexical baseline | case-selected retrieval |
| Result/citation validation | reject invented IDs/schema drift | `schemas.py`, `runner.py` | repair/failure tests | one retry | evaluation thresholds |
| Judge UI | visible result and evidence | `ui.py` | manual run | Streamlit-only | deploy/auth as required |
