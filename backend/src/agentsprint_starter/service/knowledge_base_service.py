from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agentsprint_starter.config import Settings, get_settings
from agentsprint_starter.processing import build_inventory_from_directory, process_inventory
from agentsprint_starter.processing.build import DEFAULT_CORPUS_GLOBS, REPRESENTATIVE_GLOBS
from agentsprint_starter.provider import ProviderError, create_chat_model
from agentsprint_starter.quality import ValidationReport, validate_knowledge_base
from agentsprint_starter.rag import (
    AdaptiveRagCompiler,
    CompiledKnowledgeBase,
    KnowledgeBaseRequest,
    NormalizedKnowledgePackage,
    RagStrategyPlan,
    SourceInventory,
    StorageTopology,
)
from agentsprint_starter.runner import AgentRunError
from agentsprint_starter.testing import DeterministicChatModel

from .schemas import (
    BuildKnowledgeBaseResponse,
    ErrorEnvelope,
    QueryKnowledgeBaseResponse,
    knowledge_answer_from_result,
)


@dataclass
class KnowledgeBaseSession:
    inventory: SourceInventory
    package: NormalizedKnowledgePackage
    plan: RagStrategyPlan
    compiled: CompiledKnowledgeBase
    validation: ValidationReport

    def close(self) -> None:
        self.compiled.index.close()


class KnowledgeBaseService:
    """Application boundary for external UI repositories."""

    def __init__(self, *, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self._compiler = AdaptiveRagCompiler()

    def build_from_corpus(
        self,
        corpus_dir: Path,
        *,
        objective: str | None = None,
        representative_only: bool = False,
        preferred_storage: StorageTopology | None = None,
    ) -> KnowledgeBaseSession:
        corpus_dir = corpus_dir.resolve()
        objective_text = objective or (
            "Build a cited SICK knowledge base for SKU lookup, protocol compatibility, "
            "and product-family relationships."
        )
        inventory = build_inventory_from_directory(
            corpus_dir,
            objective=objective_text,
            include_globs=REPRESENTATIVE_GLOBS if representative_only else DEFAULT_CORPUS_GLOBS,
        )
        package = process_inventory(inventory, corpus_dir).package
        request = KnowledgeBaseRequest(
            objective=inventory.objective,
            preferred_storage=preferred_storage,
        )
        compiled = self._compiler.compile(request, inventory, package)
        validation = validate_knowledge_base(inventory, package, compiled.plan)
        return KnowledgeBaseSession(
            inventory=inventory,
            package=package,
            plan=compiled.plan,
            compiled=compiled,
            validation=validation,
        )

    def build_response(self, session: KnowledgeBaseSession) -> BuildKnowledgeBaseResponse:
        return BuildKnowledgeBaseResponse(
            inventory=session.inventory.model_dump(mode="json"),
            package=session.package.model_dump(mode="json"),
            plan=session.plan.model_dump(mode="json"),
            validation=session.validation.model_dump(mode="json"),
            readiness=session.validation.status,
        )

    def query(
        self,
        session: KnowledgeBaseSession,
        question: str,
        *,
        deterministic: bool = False,
    ) -> QueryKnowledgeBaseResponse:
        if session.validation.status == "not_ready":
            raise KnowledgeBaseServiceError(
                code="not_ready",
                message="Knowledge base failed readiness validation.",
                details={"validation": session.validation.model_dump(mode="json")},
            )

        if deterministic:
            model = DeterministicChatModel()
        else:
            try:
                model = create_chat_model(self.settings)
            except (ProviderError, ValueError) as exc:
                raise KnowledgeBaseServiceError(
                    code="provider_not_configured",
                    message=str(exc),
                    retryable=False,
                ) from exc

        runner = session.compiled.create_runner(model, settings=self.settings)
        try:
            outcome = runner.run(question)
        except AgentRunError as exc:
            raise KnowledgeBaseServiceError(
                code="agent_run_failed",
                message=str(exc),
                retryable=False,
            ) from exc

        tool_events = [
            {
                "kind": event.kind,
                "name": event.name,
                "summary": event.summary,
                "duration_ms": event.duration_ms,
            }
            for event in outcome.trace.events
            if event.kind == "tool"
        ]
        answer = knowledge_answer_from_result(
            outcome.result,
            trace_steps=outcome.trace.steps,
            latency_ms=outcome.trace.duration_ms,
            tool_events=tool_events,
        )
        return QueryKnowledgeBaseResponse(
            index_id=session.plan.index.index_id,
            question=question,
            answer=answer,
            validation_status=session.validation.status,
        )

    def export_ui_payload(self, session: KnowledgeBaseSession) -> dict[str, Any]:
        """Single JSON document for an external UI repository."""
        return {
            "build": self.build_response(session).model_dump(mode="json"),
            "query_contract": {
                "index_id": session.plan.index.index_id,
                "validation_status": session.validation.status,
                "supported_question_min_length": 2,
                "supported_question_max_length": 1000,
            },
        }


class KnowledgeBaseServiceError(RuntimeError):
    def __init__(
        self,
        *,
        code: str,
        message: str,
        retryable: bool = False,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.envelope = ErrorEnvelope(
            code=code,
            message=message,
            retryable=retryable,
            details=details or {},
        )
