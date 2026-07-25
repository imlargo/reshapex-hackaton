import {
	PipelinePhase,
	PhaseStatus,
	SourceType,
	CheckStatus,
	ValidationStatus,
	ConfidenceLevel
} from '$lib/types/knowledge';
import type {
	KnowledgeSourceInput,
	PipelinePhaseState,
	PipelineRunResult,
	ValidationCheck
} from '$lib/types/knowledge';
import { PIPELINE_PHASE_ORDER, SOURCE_TYPE_LABELS } from '$lib/config';

function delay(ms: number) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

function randomBetween(min: number, max: number): number {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

const RELATION_TYPES = [
	'compatible_con',
	'reemplaza_a',
	'requiere_accesorio',
	'pertenece_a_familia',
	'cumple_norma'
];

function corpusProfile(sources: KnowledgeSourceInput[]): string {
	const counts = new Map<SourceType, number>();
	for (const source of sources) counts.set(source.type, (counts.get(source.type) ?? 0) + 1);
	const parts = [...counts.entries()].map(
		([type, count]) => `${count} ${SOURCE_TYPE_LABELS[type]}${count > 1 ? 's' : ''}`
	);
	return `${sources.length} fuentes clasificadas: ${parts.join(', ')}.`;
}

function phaseMetric(
	phase: PipelinePhase,
	sources: KnowledgeSourceInput[],
	candidateUnits: number,
	entitiesDetected: number,
	relationshipsDetected: number,
	conflictsFound: number
): string {
	switch (phase) {
		case PipelinePhase.INVENTORY:
			return corpusProfile(sources);
		case PipelinePhase.EXTRACTION:
			return `${candidateUnits} unidades de contenido extraídas con el método adecuado a cada tipo de fuente`;
		case PipelinePhase.NORMALIZATION:
			return `Unidades, nombres y formatos unificados en ${candidateUnits} unidades de contenido`;
		case PipelinePhase.ENTITY_RELATIONS:
			return `${entitiesDetected} entidades y ${relationshipsDetected} relaciones detectadas, con procedencia trazable`;
		case PipelinePhase.RAG_STRATEGY:
			return 'Estrategia de recuperación y topología de almacenamiento seleccionadas según la forma del corpus';
		case PipelinePhase.INDEXING:
			return `Índice construido sobre ${candidateUnits} unidades de contenido`;
		case PipelinePhase.VALIDATION:
			return conflictsFound > 0
				? `${conflictsFound} hechos con fuentes discrepantes — marcados, no resueltos automáticamente`
				: 'Sin discrepancias entre fuentes';
	}
}

// TODO: reemplazar por una conexión real al pipeline (contra el boundary
// Usuario1 -> Usuario3 descrito en analisis/agentsprint/03_contracts/INTERFACES.md)
// cuando exista el backend. Por ahora simula el avance fase por fase para poder
// construir la retroalimentación visual del pipeline.
export async function simulatePipelineRun(
	sources: KnowledgeSourceInput[],
	onPhaseUpdate: (update: PipelinePhaseState) => void
): Promise<PipelineRunResult> {
	const startedAt = new Date().toISOString();
	const candidateUnits = randomBetween(sources.length * 12, sources.length * 22);
	const entitiesDetected = randomBetween(sources.length * 4, sources.length * 9);
	const relationshipsDetected = randomBetween(entitiesDetected, Math.round(entitiesDetected * 1.6));
	let conflictsFound = 0;
	let retainedForReview = 0;

	for (const phase of PIPELINE_PHASE_ORDER) {
		onPhaseUpdate({ phase, status: PhaseStatus.RUNNING, progress: 0, startedAt: new Date().toISOString() });

		const steps = 4;
		for (let step = 1; step <= steps; step++) {
			await delay(120 + randomBetween(0, 140));
			onPhaseUpdate({ phase, status: PhaseStatus.RUNNING, progress: Math.round((step / steps) * 100) });
		}

		if (phase === PipelinePhase.VALIDATION) {
			conflictsFound = randomBetween(0, Math.max(1, Math.round(sources.length * 0.6)));
			retainedForReview = randomBetween(0, Math.max(1, Math.round(candidateUnits * 0.05)));
		}

		onPhaseUpdate({
			phase,
			status: PhaseStatus.DONE,
			progress: 100,
			metric: phaseMetric(
				phase,
				sources,
				candidateUnits,
				entitiesDetected,
				relationshipsDetected,
				conflictsFound
			),
			finishedAt: new Date().toISOString()
		});
	}

	const hasApiSource = sources.some((source) => source.type === SourceType.API);
	const hasTabularSource = sources.some((source) => source.type === SourceType.EXCEL);

	const ragStrategy =
		hasApiSource || hasTabularSource
			? {
					name: 'Retrieval híbrido (léxico + embeddings)',
					storageTopology: 'Índice vectorial + grafo de entidades producto-accesorio',
					rationale:
						'El corpus mezcla texto libre con datos tabulares o de API, así que conviene combinar recuperación léxica y semántica sobre un grafo que preserve las relaciones entre productos.'
				}
			: {
					name: 'Recuperación densa por embeddings',
					storageTopology: 'Índice vectorial único por familia de producto',
					rationale:
						'El corpus es homogéneo (solo documentos de texto libre), así que un índice vectorial simple cubre la mayoría de las consultas sin costo adicional de mantener un grafo.'
				};

	const validationChecks: ValidationCheck[] = [
		{
			name: 'Cobertura de citación',
			status: CheckStatus.PASS,
			detail: 'Todo hecho publicado conserva al menos una fuente verificable.'
		},
		{
			name: 'Conflictos entre fuentes',
			status: conflictsFound > 0 ? CheckStatus.FAIL : CheckStatus.PASS,
			detail:
				conflictsFound > 0
					? `${conflictsFound} hechos con fuentes discrepantes — no se resolvieron automáticamente.`
					: 'Sin discrepancias entre las fuentes suministradas.'
		},
		{
			name: 'Confianza mínima',
			status: retainedForReview > 0 ? CheckStatus.WARNING : CheckStatus.PASS,
			detail:
				retainedForReview > 0
					? `${retainedForReview} unidades por debajo del umbral de confianza, retenidas para revisión.`
					: 'Todas las unidades superan el umbral de confianza.'
		}
	];

	const validationStatus =
		conflictsFound > 0
			? ValidationStatus.CONDITIONAL
			: retainedForReview > 0
				? ValidationStatus.CONDITIONAL
				: ValidationStatus.READY;

	const nextAction =
		validationStatus === ValidationStatus.READY
			? 'Lista para responder consultas sin revisión adicional.'
			: 'Revisar los hechos marcados antes de exponer respuestas automáticas.';

	return {
		id: `run-${Date.now()}`,
		startedAt,
		finishedAt: new Date().toISOString(),
		sourcesCount: sources.length,
		corpusProfile: corpusProfile(sources),
		transformationPlan:
			'Extracción por tablas para fichas técnicas en PDF, por filas para catálogos en Excel y por encabezados para Markdown; toda unidad conserva su ubicación de origen.',
		entitiesDetected,
		relationshipsDetected,
		relationTypes: RELATION_TYPES.slice(0, randomBetween(3, RELATION_TYPES.length)),
		ragStrategy,
		validationStatus,
		validationChecks,
		nextAction,
		sampleAnswer: {
			question: '¿Cuál es la distancia mínima de montaje recomendada?',
			answer:
				conflictsFound > 0
					? 'Las fuentes discrepan en este valor — la respuesta queda retenida hasta que un humano confirme cuál es correcta.'
					: 'Según la ficha técnica ingerida, la distancia mínima de montaje cumple con ISO 13855 para el punto de operación evaluado.',
			citation: sources[0]?.name ?? 'fuente ingerida',
			confidence: conflictsFound > 0 ? ConfidenceLevel.LOW : ConfidenceLevel.HIGH
		}
	};
}
