// Flujo congelado de 9 etapas (ver analisis/agentsprint/03_contracts/PRIMARY_JOURNEY.md):
// Información suministrada -> [estas 7 fases] -> Base de conocimiento lista.
export enum PipelinePhase {
	INVENTORY = 'inventory',
	EXTRACTION = 'extraction',
	NORMALIZATION = 'normalization',
	ENTITY_RELATIONS = 'entity_relations',
	RAG_STRATEGY = 'rag_strategy',
	INDEXING = 'indexing',
	VALIDATION = 'validation'
}

export enum PhaseStatus {
	PENDING = 'pending',
	RUNNING = 'running',
	DONE = 'done',
	ERROR = 'error'
}

export enum SourceType {
	PDF = 'pdf',
	EXCEL = 'excel',
	MARKDOWN = 'markdown',
	FILE = 'file',
	API = 'api'
}

export enum FactStatus {
	VERIFIED = 'verified',
	CONFLICT = 'conflict',
	UNREVIEWED = 'unreviewed'
}

export enum ActivitySeverity {
	INFO = 'info',
	WARNING = 'warning',
	CRITICAL = 'critical'
}

// Ver analisis/agentsprint/03_contracts/INTERFACES.md — ValidationReport.status
export enum ValidationStatus {
	READY = 'ready',
	CONDITIONAL = 'conditional',
	NOT_READY = 'not_ready'
}

// ValidationReport.checks[].status
export enum CheckStatus {
	PASS = 'pass',
	WARNING = 'warning',
	FAIL = 'fail'
}

// KnowledgeAnswer.confidence / NormalizedKnowledgePackage.relationships[].confidence
export enum ConfidenceLevel {
	LOW = 'low',
	MEDIUM = 'medium',
	HIGH = 'high'
}
