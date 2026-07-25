# Repository Context

| Field | Current value |
| --- | --- |
| Repository mode | neutral starter being adapted to the SICK case |
| Repository root | `.` |
| Existing agent instructions | `AGENTS.md`; organizer instructions not yet supplied |
| Languages/frameworks | Python 3.12, Streamlit, LangChain, LangGraph, Pydantic; web stack delegated to Usuario 3 |
| Manifests/lockfiles | `pyproject.toml`, `uv.lock`; future `web/**` manifest owned by Usuario 3 |
| Install command | `uv sync --locked` |
| Run command | `uv run streamlit run app.py` for the current fallback |
| Test/build/lint | `uv run pytest`; `uv run ruff check .`; `uv run python scripts/smoke.py` |
| Application entry point | current fallback `app.py`; new service/web entry points selected by Usuarios 1 and 3 |
| API/UI boundary | framework-neutral JSON schemas frozen in `03_contracts/INTERFACES.md` |
| Model/tool integrations | LangChain `ChatDeepSeek`; LangGraph `StateGraph`; typed knowledge tools |
| Data/document locations | raw event files under `agentsprint/00_inbox/raw/`; Usuario 2 derived artifacts under `agentsprint/05_knowledge/` |
| Protected paths | `.git/`, `documents/`, raw inbox, `.env`, organizer files, unrelated user changes |
| Working-tree state | SICK planning edits in progress; pre-existing deletion of `.env copy.example` remains user-owned and untouched |
| Baseline failures | real-provider preflight blocked until `LLM_API_KEY`; case work blocked until representative SICK sources arrive |
| Contracts to freeze | boundary v0.1 prepared; final confirmation pending C-01 |
| Allowed write zones | Usuario 1 core/RAG/service; Usuario 2 processing/knowledge; Usuario 3 web/quality; shared files Usuario 1 only |
| Integration owner | Usuario 1; name pending |

Re-run the repository adapter after copying this folder into any other
repository. Do not carry these detected values into a different host.
