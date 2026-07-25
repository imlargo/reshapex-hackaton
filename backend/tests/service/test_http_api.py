from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from agentsprint_starter.config import Settings
from agentsprint_starter.service.http import create_app


@pytest.fixture(scope="module")
def corpus_dir() -> Path:
    path = Path(__file__).resolve().parents[2] / "contents"
    if not path.exists():
        pytest.skip("SICK contents corpus not available")
    return path


@pytest.fixture(scope="module")
def client(corpus_dir: Path) -> TestClient:
    repo_root = corpus_dir.parent
    app = create_app(settings=Settings(_env_file=None), workspace_root=repo_root)
    with TestClient(app) as test_client:
        yield test_client


def test_health_before_build(client: TestClient) -> None:
    response = client.get("/api/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["knowledge_base_ready"] is False
    assert payload["provider_configured"] is False


def test_build_and_query_flow(client: TestClient) -> None:
    build = client.post(
        "/api/knowledge/build",
        json={"corpus_dir": "contents", "representative_only": True},
    )
    assert build.status_code == 200
    build_payload = build.json()
    assert "build" in build_payload
    assert build_payload["build"]["readiness"] in {"ready", "conditional", "not_ready"}

    state = client.get("/api/knowledge/state")
    assert state.status_code == 200
    assert state.json()["query_contract"]["index_id"]

    health = client.get("/api/health")
    assert health.status_code == 200
    assert health.json()["index_id"] == build_payload["query_contract"]["index_id"]

    query = client.post(
        "/api/knowledge/query",
        json={
            "question": "Which order number matches WTB4S-3N2131?",
            "deterministic": True,
        },
    )
    assert query.status_code == 200
    answer = query.json()
    assert answer["answer"]["answer"]
    assert answer["index_id"] == build_payload["query_contract"]["index_id"]


def test_query_requires_build(client: TestClient) -> None:
    isolated_app = create_app(settings=Settings(_env_file=None))
    with TestClient(isolated_app) as isolated_client:
        response = isolated_client.post(
            "/api/knowledge/query",
            json={"question": "What is WTB4?", "deterministic": True},
        )
    assert response.status_code == 404
