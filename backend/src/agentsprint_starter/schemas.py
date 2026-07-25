from __future__ import annotations

from datetime import UTC, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class EvidenceRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    evidence_id: str = Field(pattern=r"^[A-Z0-9][A-Z0-9_-]{2,63}$")
    source_id: str = Field(min_length=1, max_length=100)
    title: str = Field(min_length=1, max_length=240)
    content: str = Field(min_length=1, max_length=12000)
    location: str = Field(default="", max_length=240)
    metadata: dict[str, str | int | float | bool] = Field(default_factory=dict)


class Citation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    evidence_id: str
    claim: str = Field(min_length=1, max_length=400)


class DecisionResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    answer: str = Field(min_length=1, max_length=5000)
    citations: list[Citation] = Field(default_factory=list, max_length=12)
    confidence: Literal["low", "medium", "high"]
    evidence_grade: Literal["insufficient", "partial", "strong"]
    unresolved_risk: str = Field(min_length=1, max_length=1000)
    next_action: str = Field(min_length=1, max_length=1000)
    sufficient_evidence: bool

    @model_validator(mode="after")
    def cited_when_sufficient(self) -> DecisionResult:
        if self.sufficient_evidence and not self.citations:
            raise ValueError("A sufficient result must include at least one citation.")
        return self


class Usage(BaseModel):
    input_tokens: int = Field(default=0, ge=0)
    output_tokens: int = Field(default=0, ge=0)
    total_tokens: int = Field(default=0, ge=0)

    def add(self, other: Usage) -> None:
        self.input_tokens += other.input_tokens
        self.output_tokens += other.output_tokens
        self.total_tokens += other.total_tokens


class TraceEvent(BaseModel):
    at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    kind: Literal["model", "tool", "validation", "error"]
    name: str
    summary: str
    duration_ms: int | None = Field(default=None, ge=0)
    details: dict[str, Any] = Field(default_factory=dict)


class RunTrace(BaseModel):
    run_id: str
    model: str
    started_at: datetime
    completed_at: datetime
    duration_ms: int = Field(ge=0)
    steps: int = Field(ge=0)
    retries: int = Field(ge=0)
    usage: Usage
    events: list[TraceEvent]


class RunOutcome(BaseModel):
    result: DecisionResult
    evidence: list[EvidenceRecord]
    trace: RunTrace


class SearchEvidenceArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(min_length=2, max_length=500)
    limit: int = Field(default=4, ge=1, le=6)


class GetEvidenceArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    evidence_id: str = Field(min_length=3, max_length=64)


class ListSourcesArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")
