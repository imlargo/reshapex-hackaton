import pytest
from pydantic import ValidationError

from agentsprint_starter.schemas import DecisionResult


def test_sufficient_result_requires_a_citation() -> None:
    with pytest.raises(ValidationError, match="citation"):
        DecisionResult(
            answer="Proceed.",
            citations=[],
            confidence="high",
            evidence_grade="strong",
            unresolved_risk="None identified.",
            next_action="Proceed.",
            sufficient_evidence=True,
        )
