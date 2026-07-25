from __future__ import annotations

import json
import sys

from agentsprint_starter.config import Settings
from agentsprint_starter.provider import create_chat_model
from agentsprint_starter.runner import AgentRunner
from agentsprint_starter.schemas import EvidenceRecord
from agentsprint_starter.tools import EvidenceStore, ToolRegistry


def main() -> int:
    settings = Settings()
    if not settings.provider_is_configured:
        print(
            "BLOCKED: LLM_API_KEY is unset. Configure the ignored .env file, "
            "then rerun this command."
        )
        return 2
    if settings.llm_thinking:
        print("BLOCKED: Set LLM_THINKING=false for the required non-thinking preflight.")
        return 2

    evidence = [
        EvidenceRecord(
            evidence_id="EVID-PREFLIGHT-001",
            source_id="SRC-PREFLIGHT",
            title="Inspection interval",
            content="Standard inspection is due every 500 operating hours.",
            location="rule 1",
        ),
        EvidenceRecord(
            evidence_id="EVID-PREFLIGHT-002",
            source_id="SRC-PREFLIGHT",
            title="Work-order requirement",
            content="A due inspection requires a work order with the current meter reading.",
            location="rule 2",
        ),
    ]
    outcome = AgentRunner(
        model=create_chat_model(settings),
        tools=ToolRegistry(EvidenceStore(evidence)),
        settings=settings,
    ).run(
        "The meter reads 500 operating hours. Based only on the supplied evidence, "
        "state the next action and remaining risk."
    )
    tool_events = [event for event in outcome.trace.events if event.kind == "tool"]
    if not tool_events:
        print("FAILED: the provider returned no accepted tool call.")
        return 1

    print(
        json.dumps(
            {
                "status": "ok",
                "model": outcome.trace.model,
                "orchestration": "langgraph",
                "model_integration": f"langchain-{settings.llm_provider}",
                "non_thinking": True,
                "tool_calls": [event.name for event in tool_events],
                "structured_result": True,
                "evidence_grade": outcome.result.evidence_grade,
                "citations": [
                    citation.evidence_id for citation in outcome.result.citations
                ],
                "usage": outcome.trace.usage.model_dump(),
                "latency_ms": outcome.trace.duration_ms,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
