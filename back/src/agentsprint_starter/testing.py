from __future__ import annotations

import json
import uuid
from collections.abc import Callable, Sequence
from typing import Any

from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage, ToolMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_core.tools import BaseTool
from pydantic import PrivateAttr


class DeterministicChatModel(BaseChatModel):
    """LangChain smoke model that always traverses the compiled LangGraph."""

    model_name: str = "deterministic-langchain-smoke"
    _calls: int = PrivateAttr(default=0)
    _final_factory: Callable[[set[str]], dict[str, Any]] = PrivateAttr()

    def __init__(
        self,
        *,
        final_factory: Callable[[set[str]], dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self._final_factory = final_factory or _default_final

    @property
    def calls(self) -> int:
        return self._calls

    @property
    def _llm_type(self) -> str:
        return "deterministic-langchain-smoke"

    def bind_tools(
        self,
        tools: Sequence[dict[str, Any] | type | Callable[..., Any] | BaseTool],
        *,
        tool_choice: str | None = None,
        **kwargs: Any,
    ) -> DeterministicChatModel:
        del tools, tool_choice, kwargs
        return self

    def _generate(
        self,
        messages: list[BaseMessage],
        stop: list[str] | None = None,
        run_manager: CallbackManagerForLLMRun | None = None,
        **kwargs: Any,
    ) -> ChatResult:
        del stop, run_manager, kwargs
        self._calls += 1
        if self._calls == 1:
            message = AIMessage(
                content="",
                tool_calls=[
                    {
                        "id": "smoke-tool-1",
                        "name": "search_evidence",
                        "args": {"query": "inspection threshold", "limit": 4},
                        "type": "tool_call",
                    }
                ],
                usage_metadata={
                    "input_tokens": 20,
                    "output_tokens": 8,
                    "total_tokens": 28,
                },
            )
        else:
            evidence_ids = _ids_from_tool_messages(messages)
            message = AIMessage(
                content=json.dumps(self._final_factory(evidence_ids)),
                usage_metadata={
                    "input_tokens": 32,
                    "output_tokens": 45,
                    "total_tokens": 77,
                },
            )
        return ChatResult(generations=[ChatGeneration(message=message)])


class ScriptedChatModel(BaseChatModel):
    """LangChain model that returns a fixed AIMessage sequence for graph tests."""

    model_name: str = "scripted-langchain-model"
    _responses: list[AIMessage] = PrivateAttr()
    _index: int = PrivateAttr(default=0)

    def __init__(
        self,
        *,
        responses: list[AIMessage],
        model_name: str = "scripted-langchain-model",
        **kwargs: Any,
    ) -> None:
        super().__init__(model_name=model_name, **kwargs)
        if not responses:
            raise ValueError("ScriptedChatModel requires at least one response.")
        self._responses = responses

    @property
    def _llm_type(self) -> str:
        return "scripted-langchain-model"

    def bind_tools(
        self,
        tools: Sequence[dict[str, Any] | type | Callable[..., Any] | BaseTool],
        *,
        tool_choice: str | None = None,
        **kwargs: Any,
    ) -> ScriptedChatModel:
        del tools, tool_choice, kwargs
        return self

    def _generate(
        self,
        messages: list[BaseMessage],
        stop: list[str] | None = None,
        run_manager: CallbackManagerForLLMRun | None = None,
        **kwargs: Any,
    ) -> ChatResult:
        del messages, stop, run_manager, kwargs
        template = self._responses[min(self._index, len(self._responses) - 1)]
        self._index += 1
        response = template.model_copy(
            deep=True,
            update={"id": f"scripted-{uuid.uuid4().hex}"},
        )
        return ChatResult(generations=[ChatGeneration(message=response)])


def tool_call_message(
    *,
    name: str,
    arguments: dict[str, Any],
    call_id: str,
) -> AIMessage:
    return AIMessage(
        content="",
        tool_calls=[
            {
                "id": call_id,
                "name": name,
                "args": arguments,
                "type": "tool_call",
            }
        ],
    )


def _ids_from_tool_messages(messages: list[BaseMessage]) -> set[str]:
    found: set[str] = set()
    for message in messages:
        if not isinstance(message, ToolMessage):
            continue
        try:
            payload = json.loads(str(message.content))
        except json.JSONDecodeError:
            continue
        for item in payload.get("evidence", []):
            evidence_id = item.get("evidence_id")
            if evidence_id:
                found.add(evidence_id)
    return found


def _default_final(evidence_ids: set[str]) -> dict[str, Any]:
    evidence_id = sorted(evidence_ids)[0] if evidence_ids else ""
    return {
        "answer": "Schedule an inspection because the recorded threshold has been reached.",
        "citations": [
            {
                "evidence_id": evidence_id,
                "claim": "The inspection threshold is 500 operating hours.",
            }
        ]
        if evidence_id
        else [],
        "confidence": "high" if evidence_id else "low",
        "evidence_grade": "partial" if evidence_id else "insufficient",
        "unresolved_risk": "The current meter reading should be confirmed.",
        "next_action": "Confirm the meter and create the inspection work order.",
        "sufficient_evidence": bool(evidence_id),
    }
