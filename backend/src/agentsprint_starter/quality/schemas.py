from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ValidationCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1, max_length=120)
    status: Literal["pass", "warning", "fail"]
    detail: str = Field(min_length=1, max_length=1000)
    evidence_ids: list[str] = Field(default_factory=list, max_length=12)


class ValidationReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    validation_id: str = Field(pattern=r"^VAL-[A-F0-9]{12}$")
    index_id: str = Field(pattern=r"^INDEX-[A-F0-9]{12}$")
    status: Literal["ready", "conditional", "not_ready"]
    checks: list[ValidationCheck]
    limitations: list[str] = Field(default_factory=list)
    next_action: str = Field(min_length=1, max_length=1000)
