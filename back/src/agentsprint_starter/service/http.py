from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, Field

from agentsprint_starter.config import Settings, get_settings

from .knowledge_base_service import (
    KnowledgeBaseService,
    KnowledgeBaseServiceError,
    KnowledgeBaseSession,
)


class BuildKnowledgeBaseRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    corpus_dir: str = "contents"
    representative_only: bool = True
    objective: str | None = Field(default=None, max_length=1000)


class QueryKnowledgeBaseRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: str = Field(min_length=2, max_length=1000)
    deterministic: bool = False


def create_app(
    *,
    settings: Settings | None = None,
    workspace_root: Path | None = None,
) -> FastAPI:
    resolved_settings = settings or get_settings()
    service = KnowledgeBaseService(settings=resolved_settings)
    root = (workspace_root or Path.cwd()).resolve()
    session_holder: dict[str, KnowledgeBaseSession | None] = {"session": None}

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        yield
        session = session_holder["session"]
        if session is not None:
            session.close()
            session_holder["session"] = None

    app = FastAPI(
        title="ReshapeX Knowledge Base API",
        version="0.1.0",
        lifespan=lifespan,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    def _resolve_corpus(path_text: str) -> Path:
        candidate = Path(path_text)
        if candidate.is_absolute():
            return candidate.resolve()
        return (root / candidate).resolve()

    @app.get("/api/health")
    def health() -> dict[str, Any]:
        session = session_holder["session"]
        knowledge_base_ready = (
            session is not None and session.validation.status != "not_ready"
        )
        return {
            "status": "ok",
            "provider_configured": resolved_settings.provider_is_configured,
            "knowledge_base_ready": knowledge_base_ready,
            "index_id": session.plan.index.index_id if session else None,
            "readiness": session.validation.status if session else None,
        }

    @app.post("/api/knowledge/build")
    def build_knowledge_base(body: BuildKnowledgeBaseRequest) -> dict[str, Any]:
        target = _resolve_corpus(body.corpus_dir)
        if not target.exists():
            raise HTTPException(status_code=404, detail=f"Corpus directory not found: {target}")

        existing = session_holder["session"]
        if existing is not None:
            existing.close()

        try:
            session_holder["session"] = service.build_from_corpus(
                target,
                objective=body.objective,
                representative_only=body.representative_only,
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

        session = session_holder["session"]
        assert session is not None
        return service.export_ui_payload(session)

    @app.get("/api/knowledge/state")
    def knowledge_state() -> dict[str, Any]:
        session = session_holder["session"]
        if session is None:
            raise HTTPException(status_code=404, detail="Knowledge base not built yet.")
        return service.export_ui_payload(session)

    @app.post("/api/knowledge/query")
    def query_knowledge_base(body: QueryKnowledgeBaseRequest) -> dict[str, Any]:
        session = session_holder["session"]
        if session is None:
            raise HTTPException(status_code=404, detail="Knowledge base not built yet.")
        try:
            response = service.query(session, body.question, deterministic=body.deterministic)
        except KnowledgeBaseServiceError as exc:
            raise HTTPException(
                status_code=422,
                detail=exc.envelope.model_dump(mode="json"),
            ) from exc
        return response.model_dump(mode="json")

    return app


app = create_app()


def main() -> None:
    import uvicorn

    uvicorn.run("agentsprint_starter.service.http:app", host="0.0.0.0", port=8000, reload=False)
