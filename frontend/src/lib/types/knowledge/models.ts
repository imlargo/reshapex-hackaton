import type {
	ActivitySeverity,
	CheckStatus,
	ConfidenceLevel,
	FactStatus,
	PhaseStatus,
	PipelinePhase,
	SourceType,
	ValidationStatus
} from './pipeline';

export interface KnowledgeSourceInput {
	id: string;
	name: string;
	type: SourceType;
	sizeLabel?: string;
	addedAt: string;
}

export interface PipelinePhaseState {
	phase: PipelinePhase;
	status: PhaseStatus;
	progress: number;
	metric?: string;
	detail?: string;
	startedAt?: string;
	finishedAt?: string;
}

// Espeja RagStrategyPlan.strategy + .storage (backend/agentsprint INTERFACES.md)
export interface RagStrategyRecommendation {
	name: string;
	storageTopology: string;
	rationale: string;
}

// Espeja ValidationReport.checks[]
export interface ValidationCheck {
	name: string;
	status: CheckStatus;
	detail: string;
}

// Espeja KnowledgeAnswer, recortado a lo que la demo necesita mostrar
export interface SampleAnswer {
	question: string;
	answer: string;
	citation: string;
	confidence: ConfidenceLevel;
}

export interface PipelineRunResult {
	id: string;
	startedAt: string;
	finishedAt: string;
	sourcesCount: number;
	// SourceInventory: perfil del corpus recién clasificado
	corpusProfile: string;
	// NormalizedKnowledgePackage.processing_report.method_summary
	transformationPlan: string;
	entitiesDetected: number;
	relationshipsDetected: number;
	relationTypes: string[];
	ragStrategy: RagStrategyRecommendation;
	validationStatus: ValidationStatus;
	validationChecks: ValidationCheck[];
	nextAction: string;
	sampleAnswer: SampleAnswer;
}

export interface FactStatusBreakdown {
	status: FactStatus;
	count: number;
}

export interface SourceBreakdownItem {
	type: SourceType;
	count: number;
}

export interface FactsTrendPoint {
	label: string;
	facts: number;
}

export interface ActivityEvent {
	id: string;
	message: string;
	timestamp: string;
	severity: ActivitySeverity;
}

export interface KnowledgeStats {
	totalFacts: number;
	statusBreakdown: FactStatusBreakdown[];
	avgConfidence: number;
	escalationsPending: number;
	sourcesIngested: number;
	sourceBreakdown: SourceBreakdownItem[];
	factsTrend: FactsTrendPoint[];
	lastRunAt: string | null;
	recentActivity: ActivityEvent[];
}
