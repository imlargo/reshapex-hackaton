import type { PipelinePhase } from '$lib/types/knowledge';

// Traza de razonamiento del pipeline — puramente presentacional (no forma
// parte de los contratos congelados en analisis/agentsprint), por eso vive
// en la feature y no en $lib/types. Formato de "decisión" por fase (entrada,
// pregunta, decisión, criterio, artefacto) según el handoff de la demo visual.

export interface EntityRelationSample {
	subject: string;
	predicate: string;
	object: string;
}

export interface SourceConflictSample {
	fact: string;
	sourceA: { name: string; value: string };
	sourceB: { name: string; value: string };
}

export interface ClassificationRow {
	source: string;
	documentClass: string;
	language: string;
	authority: string;
}

export interface ExtractionMethodRow {
	sourceLabel: string;
	method: string;
	rationale: string;
}

export interface NormalizationExample {
	field: string;
	before: string;
	after: string;
}

export interface IndexStatsData {
	unitsIndexed: number;
	dimensions: number;
	graphEdges: number;
	buildTimeMs: number;
}

export enum ArchitectureStatus {
	SELECTED = 'selected',
	AVAILABLE = 'available',
	BLOCKED = 'blocked'
}

export interface ArchitectureOption {
	name: string;
	algorithm: string;
	status: ArchitectureStatus;
	reason: string;
	gate?: string;
	limitations: string;
}

export interface ReadinessSummary {
	evidenceRetrieved: number;
	evidenceGrade: string;
	confidence: string;
	status: string;
	unresolvedRisk: string;
	nextAction: string;
}

export type DecisionArtifact =
	| { kind: 'text'; content: string }
	| { kind: 'classification'; rows: ClassificationRow[] }
	| { kind: 'extraction-methods'; rows: ExtractionMethodRow[] }
	| { kind: 'normalization'; examples: NormalizationExample[] }
	| { kind: 'relations'; samples: EntityRelationSample[] }
	| { kind: 'architecture'; options: ArchitectureOption[] }
	| { kind: 'index-stats'; stats: IndexStatsData }
	| { kind: 'conflict'; sample: SourceConflictSample }
	| { kind: 'readiness'; summary: ReadinessSummary };

export interface PipelineDecisionEvent {
	id: string;
	phase: PipelinePhase;
	timestamp: string;
	question: string;
	inputs: string[];
	decision: string;
	criteria: string;
	artifact: DecisionArtifact;
}
