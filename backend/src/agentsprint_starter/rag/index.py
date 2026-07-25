from __future__ import annotations

import json
import math
import re
import sqlite3
import threading
import unicodedata
from collections import Counter, defaultdict, deque
from collections.abc import Iterable

from agentsprint_starter.schemas import EvidenceRecord
from agentsprint_starter.tools import EvidenceStore

from .contracts import (
    KnowledgeRelationship,
    NormalizedKnowledgePackage,
    RagStrategyPlan,
    SearchAlgorithm,
    StorageTopology,
)

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_-]+")
CONFIDENCE_WEIGHT = {"low": 0.35, "medium": 0.65, "high": 1.0}


class QueryableIndex(EvidenceStore):
    """A local demo index that preserves the existing typed evidence-tool seam."""

    def __init__(
        self,
        package: NormalizedKnowledgePackage,
        plan: RagStrategyPlan,
    ) -> None:
        if plan.package_id != package.package_id:
            raise ValueError("RAG plan and normalized package IDs do not match.")
        if plan.index.status == "failed" or not package.content_units:
            raise ValueError("Cannot build an index without normalized content units.")

        records, aliases = _records_from_package(package)
        super().__init__(records)
        self.package = package
        self.plan = plan
        self.index_id = plan.index.index_id
        self.algorithm = plan.strategy.search_algorithm
        self._aliases = aliases
        self._document_terms = {
            record.evidence_id: Counter(_tokens(_record_text(record)))
            for record in self.records
        }
        self._idf = _inverse_document_frequency(self._document_terms.values())
        self._entities = {entity.id: entity for entity in package.entities}
        self._adjacency = _adjacency(package.relationships)
        self._sqlite: sqlite3.Connection | None = None
        self._sqlite_lock = threading.Lock()
        if plan.storage.topology is StorageTopology.RELATIONAL:
            self._sqlite = _build_sqlite(self.records)

    def search(self, query: str, limit: int) -> list[EvidenceRecord]:
        bounded_limit = max(1, min(limit, 20))
        if self.algorithm is SearchAlgorithm.SQL_FILTER_BM25:
            return self._relational_search(query, bounded_limit)
        if self.algorithm is SearchAlgorithm.TFIDF_COSINE:
            return self._vector_search(query, bounded_limit)
        if self.algorithm is SearchAlgorithm.BREADTH_FIRST:
            return self._breadth_first_search(query, bounded_limit)
        if self.algorithm is SearchAlgorithm.PERSONALIZED_PAGERANK:
            return self._personalized_pagerank_search(query, bounded_limit)
        raise ValueError(f"Unsupported search algorithm: {self.algorithm}")

    def close(self) -> None:
        if self._sqlite is not None:
            with self._sqlite_lock:
                self._sqlite.close()
                self._sqlite = None

    def _vector_search(self, query: str, limit: int) -> list[EvidenceRecord]:
        query_terms = Counter(_tokens(query))
        if not query_terms:
            return []
        query_vector = _tfidf_vector(query_terms, self._idf)
        ranked: list[tuple[float, str, EvidenceRecord]] = []
        for record in self.records:
            document_vector = _tfidf_vector(
                self._document_terms[record.evidence_id],
                self._idf,
            )
            score = _cosine_similarity(query_vector, document_vector)
            if score > 0:
                ranked.append((score, record.evidence_id, record))
        ranked.sort(key=lambda item: (-item[0], item[1]))
        return [item[2] for item in ranked[:limit]]

    def _relational_search(self, query: str, limit: int) -> list[EvidenceRecord]:
        if self._sqlite is None:
            return []
        terms = _tokens(query)
        if not terms:
            return []
        predicates = " OR ".join(
            "lower(title || ' ' || content || ' ' || metadata_json) LIKE ?"
            for _ in terms
        )
        parameters = [f"%{term}%" for term in terms]
        statement = (
            "SELECT evidence_id FROM evidence WHERE "
            f"{predicates} ORDER BY evidence_id"
        )
        with self._sqlite_lock:
            candidates = [
                row[0]
                for row in self._sqlite.execute(statement, parameters).fetchall()
            ]
        scores = _bm25_scores(
            Counter(terms),
            {
                evidence_id: self._document_terms[evidence_id]
                for evidence_id in candidates
            },
        )
        ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        return [
            record
            for evidence_id, _ in ranked[:limit]
            if (record := self.get(evidence_id)) is not None
        ]

    def _breadth_first_search(
        self,
        query: str,
        limit: int,
    ) -> list[EvidenceRecord]:
        seeds = self._seed_entities(query)
        if not seeds:
            return self._vector_search(query, limit)

        evidence_scores: dict[str, float] = defaultdict(float)
        visited: dict[str, int] = {}
        queue: deque[tuple[str, int]] = deque((seed, 0) for seed in seeds)
        for seed in seeds:
            visited[seed] = 0

        while queue:
            node, distance = queue.popleft()
            if distance >= 2:
                continue
            for neighbor, weight, evidence_ids in self._adjacency.get(node, []):
                edge_score = weight / (distance + 1)
                for evidence_id in evidence_ids:
                    primary_id = self._aliases.get(evidence_id, evidence_id)
                    evidence_scores[primary_id] = max(
                        evidence_scores[primary_id],
                        edge_score,
                    )
                next_distance = distance + 1
                if neighbor not in visited or next_distance < visited[neighbor]:
                    visited[neighbor] = next_distance
                    queue.append((neighbor, next_distance))

        return self._rank_graph_evidence(evidence_scores, query, limit)

    def _personalized_pagerank_search(
        self,
        query: str,
        limit: int,
    ) -> list[EvidenceRecord]:
        seeds = self._seed_entities(query)
        nodes = set(self._entities)
        if not seeds or not nodes:
            return self._vector_search(query, limit)

        personalization = {
            node: (1 / len(seeds) if node in seeds else 0.0) for node in nodes
        }
        rank = personalization.copy()
        damping = 0.85
        for _ in range(24):
            updated = {
                node: (1 - damping) * personalization[node] for node in nodes
            }
            for node in nodes:
                edges = self._adjacency.get(node, [])
                total_weight = sum(weight for _, weight, _ in edges)
                if not edges or total_weight == 0:
                    for target in nodes:
                        updated[target] += damping * rank[node] * personalization[target]
                    continue
                for neighbor, weight, _ in edges:
                    updated[neighbor] += damping * rank[node] * weight / total_weight
            rank = updated

        evidence_scores: dict[str, float] = defaultdict(float)
        for node, edges in self._adjacency.items():
            for neighbor, weight, evidence_ids in edges:
                edge_score = (rank.get(node, 0.0) + rank.get(neighbor, 0.0)) * weight
                for evidence_id in evidence_ids:
                    primary_id = self._aliases.get(evidence_id, evidence_id)
                    evidence_scores[primary_id] = max(
                        evidence_scores[primary_id],
                        edge_score,
                    )
        return self._rank_graph_evidence(evidence_scores, query, limit)

    def _rank_graph_evidence(
        self,
        evidence_scores: dict[str, float],
        query: str,
        limit: int,
    ) -> list[EvidenceRecord]:
        lexical = {
            record.evidence_id: score
            for score, _, record in _vector_rank(
                query,
                self.records,
                self._document_terms,
                self._idf,
            )
        }
        ranked = sorted(
            evidence_scores,
            key=lambda evidence_id: (
                -(
                    evidence_scores[evidence_id]
                    + 0.15 * lexical.get(evidence_id, 0.0)
                ),
                evidence_id,
            ),
        )
        records = [
            record
            for evidence_id in ranked[:limit]
            if (record := self.get(evidence_id)) is not None
        ]
        return records or self._vector_search(query, limit)

    def _seed_entities(self, query: str) -> set[str]:
        query_normalized = _normalize(query)
        query_tokens = set(_tokens(query))
        seeds: set[str] = set()
        for entity_id, entity in self._entities.items():
            label = _normalize(entity.label)
            label_tokens = set(_tokens(label))
            if label in query_normalized or query_tokens & label_tokens:
                seeds.add(entity_id)
        return seeds


def build_queryable_index(
    package: NormalizedKnowledgePackage,
    plan: RagStrategyPlan,
) -> QueryableIndex:
    return QueryableIndex(package, plan)


def _records_from_package(
    package: NormalizedKnowledgePackage,
) -> tuple[list[EvidenceRecord], dict[str, str]]:
    records: list[EvidenceRecord] = []
    aliases: dict[str, str] = {}
    for unit in package.content_units:
        primary_id = unit.evidence_ids[0]
        for evidence_id in unit.evidence_ids:
            aliases[evidence_id] = primary_id
        metadata = dict(unit.metadata)
        metadata["unit_id"] = unit.unit_id
        records.append(
            EvidenceRecord(
                evidence_id=primary_id,
                source_id=unit.source_id,
                title=str(unit.metadata.get("title", unit.unit_id)),
                content=unit.content,
                location=unit.location,
                metadata=metadata,
            )
        )
    return records, aliases


def _build_sqlite(records: list[EvidenceRecord]) -> sqlite3.Connection:
    connection = sqlite3.connect(":memory:", check_same_thread=False)
    connection.execute(
        """
        CREATE TABLE evidence (
            evidence_id TEXT PRIMARY KEY,
            source_id TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            location TEXT NOT NULL,
            metadata_json TEXT NOT NULL
        )
        """
    )
    connection.executemany(
        """
        INSERT INTO evidence (
            evidence_id, source_id, title, content, location, metadata_json
        ) VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (
                record.evidence_id,
                record.source_id,
                record.title,
                record.content,
                record.location,
                json.dumps(record.metadata, ensure_ascii=False, sort_keys=True),
            )
            for record in records
        ],
    )
    connection.commit()
    return connection


def _adjacency(
    relationships: list[KnowledgeRelationship],
) -> dict[str, list[tuple[str, float, tuple[str, ...]]]]:
    adjacency: dict[str, list[tuple[str, float, tuple[str, ...]]]] = defaultdict(list)
    for relationship in relationships:
        weight = CONFIDENCE_WEIGHT[relationship.confidence]
        evidence = tuple(relationship.evidence_ids)
        adjacency[relationship.subject_id].append(
            (relationship.object_id, weight, evidence)
        )
        adjacency[relationship.object_id].append(
            (relationship.subject_id, weight, evidence)
        )
    for edges in adjacency.values():
        edges.sort(key=lambda edge: (edge[0], edge[2]))
    return dict(adjacency)


def _vector_rank(
    query: str,
    records: list[EvidenceRecord],
    document_terms: dict[str, Counter[str]],
    idf: dict[str, float],
) -> list[tuple[float, str, EvidenceRecord]]:
    query_vector = _tfidf_vector(Counter(_tokens(query)), idf)
    ranked: list[tuple[float, str, EvidenceRecord]] = []
    for record in records:
        score = _cosine_similarity(
            query_vector,
            _tfidf_vector(document_terms[record.evidence_id], idf),
        )
        if score > 0:
            ranked.append((score, record.evidence_id, record))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return ranked


def _inverse_document_frequency(
    documents: Iterable[Counter[str]],
) -> dict[str, float]:
    document_list = list(documents)
    document_frequency = Counter(
        term for document in document_list for term in document
    )
    count = len(document_list)
    return {
        term: math.log((1 + count) / (1 + frequency)) + 1
        for term, frequency in document_frequency.items()
    }


def _tfidf_vector(
    terms: Counter[str],
    idf: dict[str, float],
) -> dict[str, float]:
    total = sum(terms.values()) or 1
    return {
        term: count / total * idf.get(term, 1.0)
        for term, count in terms.items()
    }


def _cosine_similarity(
    left: dict[str, float],
    right: dict[str, float],
) -> float:
    common = set(left) & set(right)
    numerator = sum(left[term] * right[term] for term in common)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if not left_norm or not right_norm:
        return 0.0
    return numerator / (left_norm * right_norm)


def _bm25_scores(
    query: Counter[str],
    documents: dict[str, Counter[str]],
) -> dict[str, float]:
    if not documents:
        return {}
    average_length = sum(sum(document.values()) for document in documents.values()) / len(
        documents
    )
    document_frequency = Counter(
        term for document in documents.values() for term in document
    )
    document_count = len(documents)
    k1 = 1.5
    b = 0.75
    scores: dict[str, float] = {}
    for evidence_id, document in documents.items():
        length = sum(document.values())
        score = 0.0
        for term, query_count in query.items():
            frequency = document[term]
            if not frequency:
                continue
            inverse_frequency = math.log(
                1
                + (
                    document_count
                    - document_frequency[term]
                    + 0.5
                )
                / (document_frequency[term] + 0.5)
            )
            denominator = frequency + k1 * (
                1 - b + b * length / max(average_length, 1)
            )
            score += query_count * inverse_frequency * frequency * (k1 + 1) / denominator
        if score:
            scores[evidence_id] = score
    return scores


def _record_text(record: EvidenceRecord) -> str:
    metadata = " ".join(f"{key} {value}" for key, value in record.metadata.items())
    return f"{record.title} {record.content} {metadata}"


def _tokens(text: str) -> list[str]:
    return TOKEN_RE.findall(_normalize(text))


def _normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    return "".join(character for character in decomposed if not unicodedata.combining(character))
