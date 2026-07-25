from __future__ import annotations

import json
import time
from typing import Any

import pytest
from langchain_core.messages import AIMessage

from agentsprint_starter.config import Settings
from agentsprint_starter.runner import AgentRunner, OutputValidationError, StepLimitError
from agentsprint_starter.schemas import EvidenceRecord
from agentsprint_starter.testing import (
    DeterministicChatModel,
    ScriptedChatModel,
    tool_call_message,
)
from agentsprint_starter.tools import EvidenceStore, ToolRegistry


@pytest.fixture
def evidence() -> list[EvidenceRecord]:
    return [
        EvidenceRecord(
            evidence_id="EVID-001",
            source_id="SRC-001",
            title="Inspection rule",
            content="Inspection threshold is 500 operating hours.",
        )
    ]


def _runner(
    model: Any,
    evidence: list[EvidenceRecord],
    retries: int = 1,
    *,
    max_steps: int = 6,
    tool_timeout: float = 1,
) -> AgentRunner:
    return AgentRunner(
        model=model,
        tools=ToolRegistry(EvidenceStore(evidence)),
        settings=Settings(
            _env_file=None,
            agent_max_steps=max_steps,
            agent_max_retries=retries,
            tool_timeout_seconds=tool_timeout,
        ),
    )


def _result_json(evidence_id: str, *, sufficient: bool = True) -> str:
    return json.dumps(
        {
            "answer": "Inspect now." if sufficient else "Evidence is insufficient.",
            "citations": [
                {"evidence_id": evidence_id, "claim": "500-hour threshold."}
            ]
            if evidence_id
            else [],
            "confidence": "high" if sufficient else "low",
            "evidence_grade": "partial" if sufficient else "insufficient",
            "unresolved_risk": "Meter not confirmed.",
            "next_action": "Confirm the meter.",
            "sufficient_evidence": sufficient,
        }
    )


def test_smoke_runner_traverses_langgraph_and_returns_grounded_result(
    evidence: list[EvidenceRecord],
) -> None:
    runner = _runner(DeterministicChatModel(), evidence)
    outcome = runner.run("Is inspection due?")
    graph_nodes = set(runner.graph.get_graph().nodes)

    assert {"model", "tools", "validate", "repair"} <= graph_nodes
    assert outcome.result.sufficient_evidence
    assert outcome.result.evidence_grade == "partial"
    assert [item.evidence_id for item in outcome.evidence] == ["EVID-001"]
    assert any(event.kind == "tool" for event in outcome.trace.events)
    assert all("graph_node" in event.details for event in outcome.trace.events)
    assert outcome.trace.usage.total_tokens == 105


def _repairing_model(*, succeeds: bool) -> ScriptedChatModel:
    responses = [
        tool_call_message(
            name="search_evidence",
            arguments={"query": "inspection threshold", "limit": 2},
            call_id="call-1",
        ),
        AIMessage(content=_result_json("EVID-INVENTED")),
    ]
    if succeeds:
        responses.append(
            AIMessage(
                content=_result_json("EVID-001"),
                usage_metadata={
                    "input_tokens": 1,
                    "output_tokens": 1,
                    "total_tokens": 2,
                },
            )
        )
    return ScriptedChatModel(responses=responses, model_name="repairing-langchain-model")


def test_runner_repairs_an_invented_citation_once(
    evidence: list[EvidenceRecord],
) -> None:
    outcome = _runner(_repairing_model(succeeds=True), evidence).run("Is inspection due?")

    assert outcome.trace.retries == 1
    assert outcome.result.citations[0].evidence_id == "EVID-001"
    assert any(event.name == "bounded-repair" for event in outcome.trace.events)


def test_runner_stops_after_the_configured_repair(
    evidence: list[EvidenceRecord],
) -> None:
    with pytest.raises(OutputValidationError, match="not returned by a tool"):
        _runner(_repairing_model(succeeds=False), evidence).run("Is inspection due?")


def test_tool_failure_can_end_in_honest_insufficient_result(
    evidence: list[EvidenceRecord],
) -> None:
    model = ScriptedChatModel(
        model_name="tool-failure-langchain-model",
        responses=[
            tool_call_message(name="unknown_tool", arguments={}, call_id="bad-call"),
            AIMessage(content=_result_json("", sufficient=False)),
        ],
    )
    outcome = _runner(model, evidence).run("What should happen?")

    assert not outcome.result.sufficient_evidence
    assert outcome.result.evidence_grade == "insufficient"
    assert any("Unknown tool" in event.summary for event in outcome.trace.events)


def test_missing_evidence_returns_an_honest_insufficient_result() -> None:
    outcome = _runner(DeterministicChatModel(), []).run("Is inspection due?")

    assert not outcome.result.sufficient_evidence
    assert outcome.result.confidence == "low"
    assert outcome.result.evidence_grade == "insufficient"
    assert outcome.evidence == []


def test_contradictory_evidence_stays_visible_and_low_confidence() -> None:
    records = [
        EvidenceRecord(
            evidence_id="EVID-001",
            source_id="SRC-A",
            title="Inspection threshold A",
            content="The inspection threshold is 500 operating hours.",
        ),
        EvidenceRecord(
            evidence_id="EVID-002",
            source_id="SRC-B",
            title="Inspection threshold B",
            content="The inspection threshold is 750 operating hours.",
        ),
    ]

    def contradiction_result(ids: set[str]) -> dict[str, Any]:
        return {
            "answer": "The sources conflict, so the threshold cannot be selected safely.",
            "citations": [
                {"evidence_id": evidence_id, "claim": "Conflicting threshold source."}
                for evidence_id in sorted(ids)
            ],
            "confidence": "low",
            "evidence_grade": "strong",
            "unresolved_risk": "The authoritative inspection interval is unresolved.",
            "next_action": "Ask the source owner which revision controls.",
            "sufficient_evidence": False,
        }

    outcome = _runner(
        DeterministicChatModel(final_factory=contradiction_result),
        records,
    ).run("What is the inspection threshold?")

    assert not outcome.result.sufficient_evidence
    assert outcome.result.confidence == "low"
    assert {item.evidence_id for item in outcome.evidence} == {"EVID-001", "EVID-002"}


def test_tool_timeout_is_returned_to_the_agent(
    evidence: list[EvidenceRecord],
) -> None:
    registry = ToolRegistry(EvidenceStore(evidence))
    original_execute = registry.execute

    def slow_execute(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        time.sleep(0.05)
        return original_execute(name, arguments)

    registry.execute = slow_execute  # type: ignore[method-assign]
    runner = AgentRunner(
        model=DeterministicChatModel(),
        tools=registry,
        settings=Settings(
            _env_file=None,
            agent_max_steps=4,
            agent_max_retries=1,
            tool_timeout_seconds=0.01,
        ),
    )

    outcome = runner.run("Is inspection due?")

    assert not outcome.result.sufficient_evidence
    assert any("timeout" in event.summary for event in outcome.trace.events)


def test_agent_stops_at_the_step_limit(evidence: list[EvidenceRecord]) -> None:
    endless_tool_call = tool_call_message(
        name="list_sources",
        arguments={},
        call_id="endless",
    )
    model = ScriptedChatModel(
        responses=[endless_tool_call],
        model_name="endless-langchain-model",
    )

    with pytest.raises(StepLimitError, match="2-step limit"):
        _runner(model, evidence, max_steps=2).run("Keep searching.")
