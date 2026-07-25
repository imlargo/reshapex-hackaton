import type { PipelinePhase } from '$lib/types/knowledge';

// Traza de razonamiento del pipeline — puramente presentacional (no forma
// parte de los contratos congelados en analisis/agentsprint), por eso vive
// en la feature y no en $lib/types.
export interface PipelineLogLine {
	id: string;
	phase: PipelinePhase;
	text: string;
	timestamp: string;
}
