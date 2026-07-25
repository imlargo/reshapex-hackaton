# Mission

Build the smallest stable, evidence-grounded agent journey that maximizes the
AgentSprint rubric. Read `agentsprint/START_HERE.md` before competition-day
work and keep `agentsprint/CONTROL.md` current.

# Non-negotiable rules

- Existing user and repository instructions take precedence over the
  AgentSprint playbook.
- Treat `agentsprint/00_inbox/raw/` as append-only.
- Do not expose or commit secrets.
- Do not present an uncited material claim as grounded.
- Keep shared contracts single-writer and freeze them before branch fan-out.
- Use branch fan-out only for independent outcomes with non-overlapping writes.
- Stop feature work at the recorded demo-freeze time.

# Starter commands

```powershell
uv sync --locked
uv run streamlit run app.py
uv run python scripts/smoke.py
uv run pytest
uv run ruff check .
```

# Completion

Do not claim the judge path is ready until a real DeepSeek call, a real tool
call, a validated result, an honest error path, and the exact manual journey
have been verified and recorded in `agentsprint/06_validation/`.
