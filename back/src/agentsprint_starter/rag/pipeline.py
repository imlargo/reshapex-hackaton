from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from agentsprint_starter.config import Settings
from agentsprint_starter.runner import AgentRunner
from agentsprint_starter.tools import ToolRegistry

from .contracts import (
    KnowledgeBaseRequest,
    NormalizedKnowledgePackage,
    RagStrategyPlan,
    SourceInventory,
)
from .index import QueryableIndex, build_queryable_index
from .inventory import inventory_from_uploads
from .strategy import select_rag_strategy


@dataclass(frozen=True, slots=True)
class CompiledKnowledgeBase:
    inventory: SourceInventory
    plan: RagStrategyPlan
    index: QueryableIndex

    @property
    def tools(self) -> ToolRegistry:
        return ToolRegistry(self.index)

    def create_runner(
        self,
        model: Any,
        *,
        settings: Settings | None = None,
    ) -> AgentRunner:
        return AgentRunner(
            model=model,
            tools=self.tools,
            settings=settings or Settings(),
        )


class AdaptiveRagCompiler:
    """Objective-first boundary for Usuario 1's inventory and RAG stages."""

    def inventory(
        self,
        request: KnowledgeBaseRequest,
        files: list[tuple[str, bytes]],
    ) -> SourceInventory:
        return inventory_from_uploads(files, request.objective)

    def compile(
        self,
        request: KnowledgeBaseRequest,
        inventory: SourceInventory,
        package: NormalizedKnowledgePackage,
    ) -> CompiledKnowledgeBase:
        if inventory.objective != request.objective:
            raise ValueError("Request objective changed after inventory.")
        if package.inventory_id != inventory.inventory_id:
            raise ValueError(
                "Normalized package does not reference the supplied inventory."
            )
        plan = select_rag_strategy(
            package,
            request.objective,
            preferred_storage=request.preferred_storage,
        )
        index = build_queryable_index(package, plan)
        return CompiledKnowledgeBase(
            inventory=inventory,
            plan=plan,
            index=index,
        )
