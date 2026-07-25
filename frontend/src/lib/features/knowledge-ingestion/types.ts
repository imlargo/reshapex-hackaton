import type { PipelinePhase } from '$lib/types/knowledge';

// Traza de razonamiento del pipeline — puramente presentacional (no forma
// parte de los contratos congelados en analisis/agentsprint), por eso vive
// en la feature y no en $lib/types.

export interface DecisionOption {
	name: string;
	summary: string;
	score: number; // 0–1
}

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

interface TraceEventBase {
	id: string;
	phase: PipelinePhase;
	timestamp: string;
}

export type PipelineTraceEvent =
	| (TraceEventBase & { kind: 'log'; text: string })
	| (TraceEventBase & {
			kind: 'decision';
			question: string;
			options: DecisionOption[];
			chosen: string;
			rationale: string;
	  })
	| (TraceEventBase & { kind: 'relations'; samples: EntityRelationSample[] })
	| (TraceEventBase & { kind: 'conflict'; sample: SourceConflictSample });
