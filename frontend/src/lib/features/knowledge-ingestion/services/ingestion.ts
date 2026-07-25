import { PipelinePhase, PhaseStatus } from '$lib/types/knowledge';
import type { KnowledgeSourceInput, PipelinePhaseState, PipelineRunResult } from '$lib/types/knowledge';
import { PIPELINE_PHASE_ORDER } from '$lib/config';

function delay(ms: number) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

function randomBetween(min: number, max: number): number {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

function phaseMetric(
	phase: PipelinePhase,
	sourcesCount: number,
	candidateFacts: number,
	conflictsFound: number,
	retainedForReview: number
): string {
	switch (phase) {
		case PipelinePhase.INGEST:
			return `${sourcesCount} fuentes registradas`;
		case PipelinePhase.PARSE:
			return `${sourcesCount} documentos convertidos a texto estructurado`;
		case PipelinePhase.EXTRACT:
			return `${candidateFacts} hechos candidatos identificados`;
		case PipelinePhase.NORMALIZE:
			return `Unidades y nombres unificados en ${candidateFacts} hechos`;
		case PipelinePhase.RECONCILE:
			return conflictsFound > 0
				? `${conflictsFound} conflictos detectados entre fuentes — quedan marcados, no se resuelven solos`
				: 'Sin conflictos entre fuentes';
		case PipelinePhase.VALIDATE:
			return `${candidateFacts - retainedForReview} hechos con confianza suficiente, ${retainedForReview} retenidos para revisión`;
		case PipelinePhase.PUBLISH:
			return `${candidateFacts - retainedForReview} hechos publicados en la capa de conocimiento`;
	}
}

// TODO: reemplazar por una conexión real al pipeline (SSE/WebSocket contra
// POST /knowledge/pipeline/run vía BaseService) cuando exista el backend.
// Por ahora simula el avance fase por fase para poder construir la
// retroalimentación visual del pipeline.
export async function simulatePipelineRun(
	sources: KnowledgeSourceInput[],
	onPhaseUpdate: (update: PipelinePhaseState) => void
): Promise<PipelineRunResult> {
	const startedAt = new Date().toISOString();
	const candidateFacts = randomBetween(sources.length * 18, sources.length * 30);
	let conflictsFound = 0;
	let retainedForReview = 0;

	for (const phase of PIPELINE_PHASE_ORDER) {
		onPhaseUpdate({ phase, status: PhaseStatus.RUNNING, progress: 0, startedAt: new Date().toISOString() });

		const steps = 4;
		for (let step = 1; step <= steps; step++) {
			await delay(120 + randomBetween(0, 140));
			onPhaseUpdate({ phase, status: PhaseStatus.RUNNING, progress: Math.round((step / steps) * 100) });
		}

		if (phase === PipelinePhase.RECONCILE) {
			conflictsFound = randomBetween(1, Math.max(2, Math.round(candidateFacts * 0.08)));
		}
		if (phase === PipelinePhase.VALIDATE) {
			retainedForReview = randomBetween(1, Math.max(1, Math.round(candidateFacts * 0.05)));
		}

		onPhaseUpdate({
			phase,
			status: PhaseStatus.DONE,
			progress: 100,
			metric: phaseMetric(phase, sources.length, candidateFacts, conflictsFound, retainedForReview),
			finishedAt: new Date().toISOString()
		});
	}

	return {
		id: `run-${Date.now()}`,
		startedAt,
		finishedAt: new Date().toISOString(),
		sourcesCount: sources.length,
		factsCreated: candidateFacts - retainedForReview,
		conflictsFound,
		escalated: retainedForReview,
		avgConfidence: Math.round((0.82 + Math.random() * 0.12) * 100) / 100
	};
}
