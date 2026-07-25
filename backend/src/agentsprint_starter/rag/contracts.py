from __future__ import annotations

from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class SourceStatus(StrEnum):
    ACCEPTED = "accepted"
    UNSUPPORTED = "unsupported"
    FAILED = "failed"


class DocumentClass(StrEnum):
    DATASHEET = "datasheet"
    OPERATING_INSTRUCTION = "operating_instruction"
    TECHNICAL_INFORMATION = "technical_information"
    KNOWLEDGE_ARTICLE = "knowledge_article"
    PRODUCT_OVERVIEW = "product_overview"
    GUIDE = "guide"
    REPOSITORY_METADATA = "repository_metadata"
    STRUCTURED_DATA = "structured_data"
    SOFTWARE_DOCUMENTATION = "software_documentation"
    GENERAL_DOCUMENT = "general_document"
    UNSUPPORTED = "unsupported"


class StorageTopology(StrEnum):
    RELATIONAL = "relational"
    VECTOR = "vector"
    SIMPLE_GRAPH = "simple_graph"
    COMPLEX_GRAPH = "complex_graph"


class SearchAlgorithm(StrEnum):
    SQL_FILTER_BM25 = "sql_filter_bm25"
    TFIDF_COSINE = "tfidf_cosine"
    BREADTH_FIRST = "breadth_first_search"
    PERSONALIZED_PAGERANK = "personalized_pagerank"


class SourceDescriptor(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_id: str = Field(pattern=r"^SRC-[A-Z0-9_-]{3,96}$")
    name: str = Field(min_length=1, max_length=500)
    media_type: str = Field(min_length=1, max_length=160)
    size_bytes: int = Field(ge=0)
    checksum: str = Field(pattern=r"^[A-F0-9]{64}$")
    status: SourceStatus
    message: str = Field(default="", max_length=500)


class SourceClassification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_id: str
    document_class: DocumentClass
    language: str = Field(default="unknown", min_length=2, max_length=32)
    signals: dict[str, str | int | float | bool] = Field(default_factory=dict)
    evidence_ids: list[str] = Field(default_factory=list)


class SourceInventory(BaseModel):
    model_config = ConfigDict(extra="forbid")

    inventory_id: str = Field(pattern=r"^INV-[A-F0-9]{12}$")
    objective: str = Field(min_length=3, max_length=1000)
    sources: list[SourceDescriptor]
    classes: list[SourceClassification]
    limitations: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def classifications_reference_sources(self) -> SourceInventory:
        source_ids = {source.source_id for source in self.sources}
        class_ids = [item.source_id for item in self.classes]
        if len(class_ids) != len(set(class_ids)):
            raise ValueError("Source classifications must be unique by source_id.")
        missing = set(class_ids) - source_ids
        if missing:
            raise ValueError(f"Classifications reference unknown sources: {sorted(missing)}")
        unclassified = source_ids - set(class_ids)
        if unclassified:
            raise ValueError(f"Sources are missing classifications: {sorted(unclassified)}")
        return self


class ContentUnit(BaseModel):
    model_config = ConfigDict(extra="forbid")

    unit_id: str = Field(min_length=3, max_length=100)
    source_id: str = Field(min_length=3, max_length=100)
    content: str = Field(min_length=1, max_length=12000)
    location: str = Field(default="", max_length=240)
    metadata: dict[str, str | int | float | bool] = Field(default_factory=dict)
    evidence_ids: list[str] = Field(min_length=1, max_length=12)


class KnowledgeEntity(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1, max_length=160)
    label: str = Field(min_length=1, max_length=240)
    type: str = Field(min_length=1, max_length=120)


class KnowledgeRelationship(BaseModel):
    model_config = ConfigDict(extra="forbid")

    subject_id: str = Field(min_length=1, max_length=160)
    predicate: str = Field(min_length=1, max_length=160)
    object_id: str = Field(min_length=1, max_length=160)
    evidence_ids: list[str] = Field(min_length=1, max_length=12)
    confidence: Literal["low", "medium", "high"]


class ProcessingReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    accepted: int = Field(ge=0)
    failed: int = Field(ge=0)
    warnings: list[str] = Field(default_factory=list)
    method_summary: str = Field(min_length=1, max_length=1000)


class NormalizedKnowledgePackage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    package_id: str = Field(min_length=3, max_length=100)
    inventory_id: str = Field(min_length=3, max_length=100)
    content_units: list[ContentUnit]
    entities: list[KnowledgeEntity] = Field(default_factory=list)
    relationships: list[KnowledgeRelationship] = Field(default_factory=list)
    processing_report: ProcessingReport

    @model_validator(mode="after")
    def validate_lineage_and_relationships(self) -> NormalizedKnowledgePackage:
        unit_ids = [unit.unit_id for unit in self.content_units]
        if len(unit_ids) != len(set(unit_ids)):
            raise ValueError("Content unit IDs must be unique.")

        primary_evidence_ids = [unit.evidence_ids[0] for unit in self.content_units]
        if len(primary_evidence_ids) != len(set(primary_evidence_ids)):
            raise ValueError("Each content unit needs a unique primary evidence ID.")

        entity_ids = [entity.id for entity in self.entities]
        if len(entity_ids) != len(set(entity_ids)):
            raise ValueError("Entity IDs must be unique.")

        known_entities = set(entity_ids)
        known_evidence = {
            evidence_id
            for unit in self.content_units
            for evidence_id in unit.evidence_ids
        }
        for relationship in self.relationships:
            endpoints = {relationship.subject_id, relationship.object_id}
            missing_entities = endpoints - known_entities
            if missing_entities:
                raise ValueError(
                    "Relationship references unknown entities: "
                    f"{sorted(missing_entities)}"
                )
            missing_evidence = set(relationship.evidence_ids) - known_evidence
            if missing_evidence:
                raise ValueError(
                    "Relationship references unknown evidence: "
                    f"{sorted(missing_evidence)}"
                )
        return self


class SelectionSignals(BaseModel):
    model_config = ConfigDict(extra="forbid")

    content_units: int = Field(ge=0)
    entities: int = Field(ge=0)
    relationships: int = Field(ge=0)
    structured_ratio: float = Field(ge=0, le=1)
    relationship_density: float = Field(ge=0, le=1)
    edges_per_entity: float = Field(ge=0)
    cycle_surplus: int = Field(ge=0)
    relationship_intent: bool
    multihop_intent: bool
    structured_intent: bool


class StrategyDescription(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1, max_length=100)
    capabilities: list[str]
    selection_rationale: str = Field(min_length=1, max_length=2000)
    evidence_ids: list[str] = Field(default_factory=list, max_length=12)
    limitations: list[str] = Field(default_factory=list)
    search_algorithm: SearchAlgorithm


class StorageDescription(BaseModel):
    model_config = ConfigDict(extra="forbid")

    topology: StorageTopology
    components: list[str]
    selection_rationale: str = Field(min_length=1, max_length=1000)


class IndexDescription(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index_id: str = Field(pattern=r"^INDEX-[A-F0-9]{12}$")
    status: Literal["ready", "partial", "failed"]
    location: str = Field(min_length=1, max_length=500)
    metrics: dict[str, str | int | float | bool] = Field(default_factory=dict)


class RagStrategyPlan(BaseModel):
    model_config = ConfigDict(extra="forbid")

    plan_id: str = Field(pattern=r"^RAG-PLAN-[A-F0-9]{12}$")
    package_id: str
    strategy: StrategyDescription
    storage: StorageDescription
    index: IndexDescription
    decision_mode: Literal["automatic", "requested"]
    selection_signals: SelectionSignals


class KnowledgeBaseRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    objective: str = Field(min_length=3, max_length=1000)
    preferred_storage: StorageTopology | None = None


class KnowledgeQueryRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index_id: str = Field(pattern=r"^INDEX-[A-F0-9]{12}$")
    question: str = Field(min_length=2, max_length=1000)
