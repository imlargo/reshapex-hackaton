from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

StorageMode = Literal["vector", "relational", "simple_graph", "complex_graph"]


class SourceEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    evidence_id: str = Field(pattern=r"^EVID-[A-Z0-9-]+$")
    source_id: str
    title: str
    location: str
    excerpt: str
    url: str
    supports: str


class DemoCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    case_id: str = Field(pattern=r"^[a-z0-9-]+$")
    short_name: str
    title: str
    eyebrow: str
    objective: str
    question: str
    description: str
    expected_storage: StorageMode
    selection_reason: str
    documents: list[str]
    document_count: int = Field(ge=1)
    simulated_chunks: int = Field(ge=1)
    simulated_entities: int = Field(ge=0)
    simulated_relations: int = Field(ge=0)
    answer: str
    caveat: str
    evidence: list[SourceEvidence]
    artifact_rows: list[dict[str, str]]


class CandidatePlan(BaseModel):
    model_config = ConfigDict(extra="forbid")

    requested_storage: StorageMode
    resolved_storage: StorageMode
    label: str
    algorithm: str
    eligible: bool
    status: Literal["selected", "available", "gated"]
    gate_note: str


class DemoStage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    number: int = Field(ge=1)
    name: str
    summary: str
    artifact: str


class DemoOutcome(BaseModel):
    model_config = ConfigDict(extra="forbid")

    case: DemoCase
    selected_plan: CandidatePlan
    candidates: list[CandidatePlan]
    stages: list[DemoStage]
    confidence: Literal["media", "alta"]
    validation_status: Literal["APROBADO PARA DEMO"]
    inventory_id: str
    plan_id: str
    index_id: str
    index_location: str
    decision_mode: Literal["automatic"]
    selection_signals: dict[str, int | float | bool]
    retrieved_evidence_ids: list[str]
    plan_dump: dict[str, Any]
