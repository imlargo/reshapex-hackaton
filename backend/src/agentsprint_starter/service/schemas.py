from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from agentsprint_starter.schemas import Citation, DecisionResult


class KnowledgeAnswerTrace(BaseModel):
    model_config = ConfigDict(extra="forbid")

    steps: int = Field(ge=0)
    tool_events: list[dict[str, Any]] = Field(default_factory=list)
    latency_ms: int = Field(ge=0)


class KnowledgeAnswer(BaseModel):
    model_config = ConfigDict(extra="forbid")

    answer: str = Field(min_length=1, max_length=5000)
    citations: list[Citation] = Field(default_factory=list, max_length=12)
    confidence: Literal["low", "medium", "high"]
    evidence_grade: Literal["insufficient", "partial", "strong"]
    unresolved_risk: str = Field(min_length=1, max_length=1000)
    next_action: str = Field(min_length=1, max_length=1000)
    sufficient_evidence: bool
    trace: KnowledgeAnswerTrace


class ErrorEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str = Field(min_length=1, max_length=80)
    message: str = Field(min_length=1, max_length=1000)
    retryable: bool = False
    details: dict[str, Any] = Field(default_factory=dict)


class BuildKnowledgeBaseResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    inventory: dict[str, Any]
    package: dict[str, Any]
    plan: dict[str, Any]
    validation: dict[str, Any]
    readiness: Literal["ready", "conditional", "not_ready"]


class QueryKnowledgeBaseResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index_id: str
    question: str
    answer: KnowledgeAnswer
    validation_status: Literal["ready", "conditional", "not_ready"]


def knowledge_answer_from_result(
    result: DecisionResult,
    *,
    trace_steps: int,
    latency_ms: int,
    tool_events: list[dict[str, Any]],
) -> KnowledgeAnswer:
    return KnowledgeAnswer(
        answer=result.answer,
        citations=result.citations,
        confidence=result.confidence,
        evidence_grade=result.evidence_grade,
        unresolved_risk=result.unresolved_risk,
        next_action=result.next_action,
        sufficient_evidence=result.sufficient_evidence,
        trace=KnowledgeAnswerTrace(
            steps=trace_steps,
            tool_events=tool_events,
            latency_ms=latency_ms,
        ),
    )
