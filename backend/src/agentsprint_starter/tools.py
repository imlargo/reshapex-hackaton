from __future__ import annotations

import re
from collections import Counter
from typing import Any

from langchain_core.tools import BaseTool, StructuredTool
from pydantic import ValidationError

from .schemas import (
    EvidenceRecord,
    GetEvidenceArgs,
    ListSourcesArgs,
    SearchEvidenceArgs,
)

TOKEN_RE = re.compile(r"[a-záéíóúñ0-9][a-záéíóúñ0-9_-]+", re.IGNORECASE)


class ToolExecutionError(RuntimeError):
    """Safe, model-visible tool failure."""


class EvidenceStore:
    def __init__(self, records: list[EvidenceRecord]) -> None:
        ids = [record.evidence_id for record in records]
        if len(ids) != len(set(ids)):
            raise ValueError("Evidence IDs must be unique.")
        self._records = {record.evidence_id: record for record in records}

    @property
    def records(self) -> list[EvidenceRecord]:
        return list(self._records.values())

    def get(self, evidence_id: str) -> EvidenceRecord | None:
        return self._records.get(evidence_id)

    def search(self, query: str, limit: int) -> list[EvidenceRecord]:
        query_terms = Counter(_tokens(query))
        ranked: list[tuple[int, str, EvidenceRecord]] = []
        for record in self._records.values():
            title_terms = Counter(_tokens(record.title))
            body_terms = Counter(_tokens(record.content))
            score = sum(
                min(count, title_terms[term]) * 4 + min(count, body_terms[term])
                for term, count in query_terms.items()
            )
            if score:
                ranked.append((score, record.evidence_id, record))
        ranked.sort(key=lambda item: (-item[0], item[1]))
        return [item[2] for item in ranked[:limit]]

    def source_summary(self) -> list[dict[str, Any]]:
        grouped: dict[str, dict[str, Any]] = {}
        for record in self._records.values():
            entry = grouped.setdefault(
                record.source_id,
                {"source_id": record.source_id, "chunks": 0, "titles": []},
            )
            entry["chunks"] += 1
            if record.title not in entry["titles"]:
                entry["titles"].append(record.title)
        return list(grouped.values())


class ToolRegistry:
    def __init__(self, store: EvidenceStore) -> None:
        self.store = store
        self._langchain_tools = self._build_langchain_tools()
        self._tools_by_name = {tool.name: tool for tool in self._langchain_tools}

    @property
    def langchain_tools(self) -> list[BaseTool]:
        return self._langchain_tools

    def get_langchain_tool(self, name: str) -> BaseTool | None:
        return self._tools_by_name.get(name)

    def _build_langchain_tools(self) -> list[BaseTool]:
        return [
            StructuredTool.from_function(
                func=self._search_evidence,
                name="search_evidence",
                description=(
                    "Search the supplied evidence. Use this before making material claims."
                ),
                args_schema=SearchEvidenceArgs,
            ),
            StructuredTool.from_function(
                func=self._get_evidence,
                name="get_evidence",
                description="Get one complete evidence chunk by its exact evidence ID.",
                args_schema=GetEvidenceArgs,
            ),
            StructuredTool.from_function(
                func=self._list_sources,
                name="list_sources",
                description=(
                    "List available source IDs and chunk counts without returning "
                    "full documents."
                ),
                args_schema=ListSourcesArgs,
            ),
        ]

    def _search_evidence(self, query: str, limit: int = 4) -> dict[str, Any]:
        return self.execute("search_evidence", {"query": query, "limit": limit})

    def _get_evidence(self, evidence_id: str) -> dict[str, Any]:
        return self.execute("get_evidence", {"evidence_id": evidence_id})

    def _list_sources(self) -> dict[str, Any]:
        return self.execute("list_sources", {})

    def execute(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        try:
            if name == "search_evidence":
                args = SearchEvidenceArgs.model_validate(arguments)
                matches = self.store.search(args.query, args.limit)
                return {
                    "query": args.query,
                    "count": len(matches),
                    "evidence": [record.model_dump() for record in matches],
                }
            if name == "get_evidence":
                args = GetEvidenceArgs.model_validate(arguments)
                record = self.store.get(args.evidence_id)
                return {
                    "found": record is not None,
                    "evidence": record.model_dump() if record else None,
                }
            if name == "list_sources":
                ListSourcesArgs.model_validate(arguments)
                return {"sources": self.store.source_summary()}
        except ValidationError as exc:
            raise ToolExecutionError(f"Invalid arguments for {name}: {exc}") from exc
        raise ToolExecutionError(f"Unknown tool: {name}")


def _tokens(text: str) -> list[str]:
    return [token.casefold() for token in TOKEN_RE.findall(text)]
