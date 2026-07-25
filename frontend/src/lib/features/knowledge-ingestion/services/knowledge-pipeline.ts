import { PIPELINE_PHASE_ORDER } from '$lib/config';
import { PhaseStatus } from '$lib/types/knowledge';
import type { KnowledgeSourceInput, PipelinePhaseState, PipelineRunResult } from '$lib/types/knowledge';
import type { PipelineDecisionEvent } from '../types';
import { buildDecisionEvents, mapBackendToPipelineResult } from './build-mapper';

const SAMPLE_QUESTION = 'Which order number matches WTB4S-3N2131?';

function delay(ms: number) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

async function ensureBackendReady(): Promise<void> {
	const response = await fetch('/api/knowledge/health');
	if (!response.ok) {
		throw new Error(
			'Knowledge backend no disponible. Ejecuta scripts/run-knowledge-api.sh desde la raíz del monorepo.'
		);
	}
}

async function markPhase(
	onPhaseUpdate: (update: PipelinePhaseState) => void,
	phase: PipelinePhaseState['phase'],
	status: PhaseStatus,
	progress: number
) {
	onPhaseUpdate({ phase, status, progress });
	await delay(120);
}

export async function runKnowledgePipeline(
	sources: KnowledgeSourceInput[],
	onPhaseUpdate: (update: PipelinePhaseState) => void,
	onDecision: (event: PipelineDecisionEvent) => void
): Promise<PipelineRunResult> {
	await ensureBackendReady();

	for (const phase of PIPELINE_PHASE_ORDER) {
		await markPhase(onPhaseUpdate, phase, PhaseStatus.RUNNING, 10);
	}

	const buildResponse = await fetch('/api/knowledge/build', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ representative_only: true })
	});
	if (!buildResponse.ok) {
		const errorBody = (await buildResponse.json().catch(() => ({}))) as { message?: string };
		throw new Error(errorBody.message ?? 'Falló el build del knowledge base');
	}
	const buildPayload = await buildResponse.json();

	const queryResponse = await fetch('/api/knowledge/query', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ question: SAMPLE_QUESTION, deterministic: false })
	});
	if (!queryResponse.ok) {
		const errorBody = (await queryResponse.json().catch(() => ({}))) as { message?: string };
		throw new Error(errorBody.message ?? 'Falló la consulta de verificación');
	}
	const queryPayload = await queryResponse.json();

	const decisions = buildDecisionEvents(buildPayload);
	for (const decision of decisions) {
		onDecision({ ...decision, timestamp: new Date().toISOString() });
		await delay(80);
	}

	for (const phase of PIPELINE_PHASE_ORDER) {
		onPhaseUpdate({
			phase,
			status: PhaseStatus.DONE,
			progress: 100,
			finishedAt: new Date().toISOString()
		});
	}

	return mapBackendToPipelineResult(buildPayload, queryPayload, sources.length);
}
