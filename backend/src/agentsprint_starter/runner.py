from __future__ import annotations

import json
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FutureTimeoutError
from datetime import UTC, datetime
from typing import Annotated, Any, Literal, TypedDict

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from pydantic import ValidationError

from .config import Settings
from .schemas import DecisionResult, RunOutcome, RunTrace, TraceEvent, Usage
from .tools import ToolExecutionError, ToolRegistry


class AgentRunError(RuntimeError):
    """Base class for an honest, UI-visible graph failure."""


class StepLimitError(AgentRunError):
    pass


class OutputValidationError(AgentRunError):
    pass


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    step_count: int
    retries: int
    tool_was_called: bool
    exposed_ids: set[str]
    usage: Usage
    events: list[TraceEvent]
    result: DecisionResult | None
    validation_issue: str | None


SYSTEM_PROMPT = """You are an evidence-grounded decision agent.
Use the supplied tools before making any material claim. Return only one JSON
object for the final answer, with exactly these fields:
{
  "answer": "concise grounded recommendation or honest decline",
  "citations": [{"evidence_id": "EVID-...", "claim": "claim supported by it"}],
  "confidence": "low|medium|high",
  "evidence_grade": "insufficient|partial|strong",
  "unresolved_risk": "remaining uncertainty, or 'None identified'",
  "next_action": "specific next step",
  "sufficient_evidence": true
}
Never invent evidence IDs. If evidence is missing or contradictory, set
sufficient_evidence to false, confidence to low, explain the limitation, and
recommend the next evidence-gathering action. Do not expose private reasoning."""


class AgentRunner:
    def __init__(
        self,
        *,
        model: BaseChatModel,
        tools: ToolRegistry,
        settings: Settings,
    ) -> None:
        self.model = model
        self.tools = tools
        self.settings = settings
        self.model_name = str(
            getattr(model, "model_name", None)
            or getattr(model, "model", None)
            or model._llm_type
        )
        self._model_with_tools = model.bind_tools(
            tools.langchain_tools,
            tool_choice="auto",
        )
        self.graph = self._build_graph()

    def _build_graph(self) -> Any:
        builder = StateGraph(AgentState)
        builder.add_node("model", self._model_node)
        builder.add_node("tools", self._tools_node)
        builder.add_node("require_tool", self._require_tool_node)
        builder.add_node("validate", self._validate_node)
        builder.add_node("repair", self._repair_node)
        builder.add_edge(START, "model")
        builder.add_conditional_edges(
            "model",
            self._route_after_model,
            {
                "tools": "tools",
                "require_tool": "require_tool",
                "validate": "validate",
            },
        )
        builder.add_edge("tools", "model")
        builder.add_edge("require_tool", "model")
        builder.add_conditional_edges(
            "validate",
            self._route_after_validation,
            {"repair": "repair", "end": END},
        )
        builder.add_edge("repair", "model")
        return builder.compile(name="agentsprint-grounded-agent")

    def run(self, request: str) -> RunOutcome:
        clean_request = request.strip()
        if not clean_request:
            raise ValueError("Request cannot be empty.")

        run_id = f"run-{uuid.uuid4().hex[:12]}"
        started_at = datetime.now(UTC)
        started_clock = time.perf_counter()
        initial_state: AgentState = {
            "messages": [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=clean_request),
            ],
            "step_count": 0,
            "retries": 0,
            "tool_was_called": False,
            "exposed_ids": set(),
            "usage": Usage(),
            "events": [],
            "result": None,
            "validation_issue": None,
        }

        try:
            final_state = self.graph.invoke(
                initial_state,
                config={"recursion_limit": self.settings.agent_max_steps * 4 + 10},
            )
        except (StepLimitError, OutputValidationError, ValueError):
            raise
        except Exception as exc:
            raise AgentRunError(f"LangGraph execution failed: {exc}") from exc

        result = final_state.get("result")
        if result is None:
            raise OutputValidationError("LangGraph ended without a validated result.")

        cited_ids = {citation.evidence_id for citation in result.citations}
        cited_records = [
            record
            for record in self.tools.store.records
            if record.evidence_id in cited_ids
        ]
        completed_at = datetime.now(UTC)
        return RunOutcome(
            result=result,
            evidence=cited_records,
            trace=RunTrace(
                run_id=run_id,
                model=self.model_name,
                started_at=started_at,
                completed_at=completed_at,
                duration_ms=_elapsed_ms(started_clock),
                steps=final_state["step_count"],
                retries=final_state["retries"],
                usage=final_state["usage"],
                events=final_state["events"],
            ),
        )

    def _model_node(self, state: AgentState) -> dict[str, Any]:
        if state["step_count"] >= self.settings.agent_max_steps:
            raise StepLimitError(
                f"Agent reached the configured {self.settings.agent_max_steps}-step limit."
            )

        call_started = time.perf_counter()
        try:
            reply = self._model_with_tools.invoke(state["messages"])
        except Exception as exc:
            raise AgentRunError(f"LangChain model invocation failed: {exc}") from exc
        if not isinstance(reply, AIMessage):
            raise AgentRunError("LangChain model did not return an AIMessage.")

        turn_usage = _usage_from_message(reply)
        usage = state["usage"].model_copy(deep=True)
        usage.add(turn_usage)
        model_name = str(
            reply.response_metadata.get("model_name")
            or reply.response_metadata.get("model")
            or self.model_name
        )
        event = TraceEvent(
            kind="model",
            name=model_name,
            summary=(
                f"Requested {len(reply.tool_calls)} tool call(s)"
                if reply.tool_calls
                else "Returned a final candidate"
            ),
            duration_ms=_elapsed_ms(call_started),
            details={
                "graph_node": "model",
                "input_tokens": turn_usage.input_tokens,
                "output_tokens": turn_usage.output_tokens,
            },
        )
        return {
            "messages": [reply],
            "step_count": state["step_count"] + 1,
            "usage": usage,
            "events": [*state["events"], event],
        }

    def _route_after_model(
        self,
        state: AgentState,
    ) -> Literal["tools", "require_tool", "validate"]:
        last_message = state["messages"][-1]
        if not isinstance(last_message, AIMessage):
            raise AgentRunError("The model node did not append an AIMessage.")
        if last_message.tool_calls:
            return "tools"
        if not state["tool_was_called"]:
            return "require_tool"
        return "validate"

    def _tools_node(self, state: AgentState) -> dict[str, Any]:
        last_message = state["messages"][-1]
        if not isinstance(last_message, AIMessage):
            raise AgentRunError("The tools node requires an AIMessage.")

        tool_messages: list[ToolMessage] = []
        events = list(state["events"])
        exposed_ids = set(state["exposed_ids"])
        for call in last_message.tool_calls:
            name = call["name"]
            arguments = call["args"]
            call_id = call["id"]
            tool_started = time.perf_counter()
            payload = self._execute_tool(name, arguments)
            returned_ids = _collect_evidence_ids(payload)
            exposed_ids.update(returned_ids)
            tool_messages.append(
                ToolMessage(
                    content=json.dumps(payload, ensure_ascii=False),
                    tool_call_id=call_id,
                    name=name,
                )
            )
            events.append(
                TraceEvent(
                    kind="tool",
                    name=name,
                    summary=_tool_summary(payload),
                    duration_ms=_elapsed_ms(tool_started),
                    details={
                        "graph_node": "tools",
                        "evidence_ids": sorted(returned_ids),
                    },
                )
            )
        return {
            "messages": tool_messages,
            "tool_was_called": True,
            "exposed_ids": exposed_ids,
            "events": events,
        }

    def _require_tool_node(self, state: AgentState) -> dict[str, Any]:
        return {
            "messages": [
                HumanMessage(
                    content=(
                        "Do not answer yet. Call at least one evidence tool, then return "
                        "the required JSON object."
                    )
                )
            ],
            "events": [
                *state["events"],
                TraceEvent(
                    kind="validation",
                    name="tool-required",
                    summary="Rejected an ungrounded final candidate.",
                    details={"graph_node": "require_tool"},
                ),
            ],
        }

    def _validate_node(self, state: AgentState) -> dict[str, Any]:
        last_message = state["messages"][-1]
        if not isinstance(last_message, AIMessage):
            raise OutputValidationError("Validation requires a final AIMessage.")
        result, issue = _validate_candidate(
            _message_text(last_message),
            state["exposed_ids"],
        )
        if issue:
            if state["retries"] >= self.settings.agent_max_retries:
                raise OutputValidationError(issue)
            return {
                "result": None,
                "validation_issue": issue,
            }

        assert result is not None
        result = _apply_evidence_grade(result, state["exposed_ids"])
        event = TraceEvent(
            kind="validation",
            name="result-accepted",
            summary=(
                f"Accepted {len(result.citations)} citation(s); "
                f"evidence grade is {result.evidence_grade}."
            ),
            details={"graph_node": "validate"},
        )
        return {
            "result": result,
            "validation_issue": None,
            "events": [*state["events"], event],
        }

    def _route_after_validation(
        self,
        state: AgentState,
    ) -> Literal["repair", "end"]:
        return "end" if state["result"] is not None else "repair"

    def _repair_node(self, state: AgentState) -> dict[str, Any]:
        issue = state["validation_issue"] or "Unknown validation issue"
        return {
            "messages": [
                HumanMessage(
                    content=(
                        "Repair the final JSON and return JSON only. Validation issue: "
                        f"{issue}. Cite only these evidence IDs: "
                        f"{sorted(state['exposed_ids'])}."
                    )
                )
            ],
            "retries": state["retries"] + 1,
            "events": [
                *state["events"],
                TraceEvent(
                    kind="validation",
                    name="bounded-repair",
                    summary=issue,
                    details={"graph_node": "repair"},
                ),
            ],
        }

    def _execute_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        tool = self.tools.get_langchain_tool(name)
        if tool is None:
            return {"ok": False, "error": f"Unknown tool: {name}"}

        executor = ThreadPoolExecutor(max_workers=1)
        future = executor.submit(tool.invoke, arguments)
        try:
            result = future.result(timeout=self.settings.tool_timeout_seconds)
            if not isinstance(result, dict):
                return {"ok": False, "error": f"{name} returned a non-object result."}
            return {"ok": True, **result}
        except FutureTimeoutError:
            future.cancel()
            return {
                "ok": False,
                "error": (
                    f"{name} exceeded the {self.settings.tool_timeout_seconds:g}s timeout."
                ),
            }
        except ToolExecutionError as exc:
            return {"ok": False, "error": str(exc)}
        except Exception as exc:
            return {"ok": False, "error": f"{name} failed: {exc}"}
        finally:
            executor.shutdown(wait=False, cancel_futures=True)


def _extract_json_payload(content: str) -> str:
    stripped = content.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()
    return stripped


def _validate_candidate(
    content: str | None,
    exposed_ids: set[str],
) -> tuple[DecisionResult | None, str | None]:
    if not content:
        return None, "The provider returned empty final content"
    payload = _extract_json_payload(content)
    try:
        result = DecisionResult.model_validate_json(payload)
    except ValidationError as exc:
        return None, f"The final result does not match the required schema: {exc}"

    cited_ids = {citation.evidence_id for citation in result.citations}
    invalid_ids = cited_ids - exposed_ids
    if invalid_ids:
        return (
            None,
            "The result cited evidence that was not returned by a tool: "
            f"{sorted(invalid_ids)}",
        )
    return result, None


def _apply_evidence_grade(
    result: DecisionResult,
    exposed_ids: set[str],
) -> DecisionResult:
    cited_ids = {citation.evidence_id for citation in result.citations}
    valid_count = len(cited_ids & exposed_ids)
    grade = "strong" if valid_count >= 2 else "partial" if valid_count == 1 else "insufficient"
    confidence = result.confidence
    if grade == "insufficient":
        confidence = "low"
    return result.model_copy(
        update={
            "evidence_grade": grade,
            "confidence": confidence,
            "sufficient_evidence": valid_count > 0 and result.sufficient_evidence,
        }
    )


def _usage_from_message(message: AIMessage) -> Usage:
    metadata = message.usage_metadata or {}
    if not metadata:
        raw = (
            message.response_metadata.get("token_usage")
            or message.response_metadata.get("usage")
            or {}
        )
        metadata = {
            "input_tokens": raw.get("prompt_tokens", 0),
            "output_tokens": raw.get("completion_tokens", 0),
            "total_tokens": raw.get("total_tokens", 0),
        }
    return Usage(
        input_tokens=int(metadata.get("input_tokens", 0) or 0),
        output_tokens=int(metadata.get("output_tokens", 0) or 0),
        total_tokens=int(metadata.get("total_tokens", 0) or 0),
    )


def _message_text(message: AIMessage) -> str | None:
    if isinstance(message.content, str):
        return message.content
    if isinstance(message.content, list):
        parts: list[str] = []
        for block in message.content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and isinstance(block.get("text"), str):
                parts.append(block["text"])
        return "".join(parts)
    return None


def _collect_evidence_ids(payload: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(payload, dict):
        value = payload.get("evidence_id")
        if isinstance(value, str):
            found.add(value)
        for child in payload.values():
            found.update(_collect_evidence_ids(child))
    elif isinstance(payload, list):
        for child in payload:
            found.update(_collect_evidence_ids(child))
    return found


def _tool_summary(payload: dict[str, Any]) -> str:
    if not payload.get("ok"):
        return str(payload.get("error", "Tool failed."))
    if "count" in payload:
        return f"Returned {payload['count']} evidence chunk(s)."
    if "sources" in payload:
        return f"Returned {len(payload['sources'])} source(s)."
    if "found" in payload:
        return "Evidence found." if payload["found"] else "Evidence ID not found."
    return "Tool completed."


def _elapsed_ms(started: float) -> int:
    return max(0, round((time.perf_counter() - started) * 1000))
