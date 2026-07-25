from __future__ import annotations

from pathlib import Path

import pytest

from agentsprint_starter.config import Settings
from agentsprint_starter.service import KnowledgeBaseService, KnowledgeBaseServiceError


@pytest.fixture(scope="module")
def corpus_dir() -> Path:
    path = Path(__file__).resolve().parents[2] / "contents"
    if not path.exists():
        pytest.skip("SICK contents corpus not available")
    return path


@pytest.fixture(scope="module")
def built_session(corpus_dir: Path):
    service = KnowledgeBaseService(settings=Settings(_env_file=None))
    session = service.build_from_corpus(corpus_dir, representative_only=True)
    yield session
    session.close()


def test_build_from_corpus_returns_ready_session(built_session) -> None:
    assert built_session.inventory.sources
    assert built_session.package.content_units
    assert built_session.plan.index.index_id.startswith("INDEX-")
    assert built_session.validation.status in {"ready", "conditional", "not_ready"}


def test_build_response_matches_contract(built_session) -> None:
    service = KnowledgeBaseService(settings=Settings(_env_file=None))
    payload = service.build_response(built_session)

    assert payload.readiness == built_session.validation.status
    assert payload.inventory["inventory_id"] == built_session.inventory.inventory_id
    assert payload.package["package_id"] == built_session.package.package_id
    assert payload.plan["plan_id"] == built_session.plan.plan_id


def test_export_ui_payload_has_build_and_query_contract(built_session) -> None:
    service = KnowledgeBaseService(settings=Settings(_env_file=None))
    payload = service.export_ui_payload(built_session)

    assert "build" in payload
    assert "query_contract" in payload
    assert payload["query_contract"]["index_id"] == built_session.plan.index.index_id


def test_query_deterministic_returns_cited_answer(built_session) -> None:
    service = KnowledgeBaseService(settings=Settings(_env_file=None))
    response = service.query(
        built_session,
        "Which order number matches WTB4S-3N2131?",
        deterministic=True,
    )

    assert response.index_id == built_session.plan.index.index_id
    assert response.answer.answer
    assert response.validation_status == built_session.validation.status


def test_query_without_provider_requires_deterministic_or_key(built_session) -> None:
    service = KnowledgeBaseService(settings=Settings(_env_file=None))
    with pytest.raises(KnowledgeBaseServiceError) as exc:
        service.query(built_session, "What is WTB4?", deterministic=False)
    assert exc.value.envelope.code == "provider_not_configured"
