from __future__ import annotations

import json

from agentsprint_starter.config import Settings
from agentsprint_starter.runner import AgentRunner
from agentsprint_starter.schemas import EvidenceRecord
from agentsprint_starter.testing import DeterministicChatModel
from agentsprint_starter.tools import EvidenceStore, ToolRegistry


def main() -> None:
    evidence = [
        EvidenceRecord(
            evidence_id="EVID-001",
            source_id="SRC-SMOKE",
            title="Neutral maintenance rule",
            content=(
                "A routine inspection is required every 500 operating hours. "
                "The work order must record the current meter reading."
            ),
            location="paragraph 1",
        )
    ]
    settings = Settings(
        _env_file=None,
        agent_max_steps=6,
        agent_max_retries=1,
        tool_timeout_seconds=2,
    )
    runner = AgentRunner(
        model=DeterministicChatModel(),
        tools=ToolRegistry(EvidenceStore(evidence)),
        settings=settings,
    )
    outcome = runner.run(
        "The asset has reached 500 operating hours. What grounded action should happen?"
    )

    assert outcome.result.sufficient_evidence
    assert outcome.result.citations[0].evidence_id == "EVID-001"
    assert any(event.kind == "tool" for event in outcome.trace.events)
    assert outcome.trace.usage.total_tokens == 105
    print(
        json.dumps(
            {
                "status": "ok",
                "run_id": outcome.trace.run_id,
                "model": outcome.trace.model,
                "orchestration": "langgraph",
                "steps": outcome.trace.steps,
                "tool_events": sum(
                    event.kind == "tool" for event in outcome.trace.events
                ),
                "evidence_grade": outcome.result.evidence_grade,
                "citations": [
                    citation.evidence_id for citation in outcome.result.citations
                ],
                "usage": outcome.trace.usage.model_dump(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
