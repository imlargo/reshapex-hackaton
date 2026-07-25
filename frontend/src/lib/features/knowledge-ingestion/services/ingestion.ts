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
import type { PipelineLogLine } from '../types';
import { PIPELINE_PHASE_ORDER, SOURCE_TYPE_LABELS } from '$lib/config';

function delay(ms: number) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

function randomBetween(min: number, max: number): number {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Pausa "orgánica": casi siempre corta, a veces una pausa larga de deliberación.
function thinkingDelay(): Promise<unknown> {
	const long = Math.random() < 0.16;
	return delay(long ? randomBetween(1400, 2600) : randomBetween(450, 1300));
}

let lineIdSeq = 0;
function nextLineId(): string {
	lineIdSeq += 1;
	return `line-${lineIdSeq}`;
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

interface RunContext {
	sources: KnowledgeSourceInput[];
	candidateUnits: number;
	entitiesDetected: number;
	relationshipsDetected: number;
	relationTypes: string[];
	conflictsFound: number;
	retainedForReview: number;
	ragStrategyName: string;
	storageTopology: string;
}

function phaseLogLines(phase: PipelinePhase, ctx: RunContext): string[] {
	const { sources } = ctx;
	switch (phase) {
		case PipelinePhase.INVENTORY: {
			const lines = [`Clasificando ${sources.length} fuentes por tipo, idioma y calidad…`];
			for (const source of sources.slice(0, 4)) {
				lines.push(`${source.name} → ${SOURCE_TYPE_LABELS[source.type]}${source.sizeLabel ? `, ${source.sizeLabel}` : ''}`);
			}
			if (sources.length > 4) lines.push(`… y ${sources.length - 4} fuente(s) más`);
			lines.push('Detectado idioma dominante: español');
			lines.push(corpusProfile(sources));
			return lines;
		}
		case PipelinePhase.EXTRACTION:
			return [
				'Aplicando extracción por tablas a documentos PDF…',
				'Aplicando extracción por filas a hojas de cálculo…',
				'Aplicando extracción por encabezados a Markdown…',
				'Conservando ubicación de origen (página, fila o sección) por unidad',
				`${ctx.candidateUnits} unidades de contenido extraídas`
			];
		case PipelinePhase.NORMALIZATION:
			return [
				'Unificando unidades de medida (mm, kg, IP, PL/SIL)…',
				'Normalizando nombres de producto y variantes de type code…',
				'Resolviendo sinónimos entre ficha técnica y listado de distribuidor…',
				`${ctx.candidateUnits} unidades normalizadas a un esquema común`
			];
		case PipelinePhase.ENTITY_RELATIONS: {
			const lines = ['Detectando entidades: productos, accesorios y normas aplicables…'];
			for (const relation of ctx.relationTypes) {
				lines.push(`Relación candidata encontrada: tipo "${relation}"`);
			}
			lines.push(`${ctx.entitiesDetected} entidades y ${ctx.relationshipsDetected} relaciones con procedencia trazada`);
			return lines;
		}
		case PipelinePhase.RAG_STRATEGY:
			return [
				'Evaluando la forma del corpus (texto libre vs. datos tabulares)…',
				`Estrategia seleccionada: ${ctx.ragStrategyName}`,
				`Topología de almacenamiento: ${ctx.storageTopology}`
			];
		case PipelinePhase.INDEXING:
			return [
				'Construyendo índice de recuperación…',
				'Indexando relaciones en el grafo de entidades…',
				`Índice listo sobre ${ctx.candidateUnits} unidades de contenido`
			];
		case PipelinePhase.VALIDATION: {
			const lines = ['Verificando cobertura de citación por hecho…'];
			if (ctx.conflictsFound > 0) {
				lines.push(
					`⚠ ${ctx.conflictsFound} hecho(s) con fuentes discrepantes — se marcan, no se resuelven automáticamente`
				);
			} else {
				lines.push('Sin discrepancias entre las fuentes suministradas');
			}
			lines.push('Calculando confianza por hecho…');
			if (ctx.retainedForReview > 0) {
				lines.push(`${ctx.retainedForReview} unidad(es) bajo el umbral de confianza, retenidas para revisión`);
			}
			return lines;
		}
	}
}

// TODO: reemplazar por una conexión real al pipeline (contra el boundary
// Usuario1 -> Usuario3 descrito en analisis/agentsprint/03_contracts/INTERFACES.md)
// cuando exista el backend. Por ahora simula el avance fase por fase, línea por
// línea, para poder construir la retroalimentación visual del pipeline.
export async function simulatePipelineRun(
	sources: KnowledgeSourceInput[],
	onPhaseUpdate: (update: PipelinePhaseState) => void,
	onLogLine: (line: PipelineLogLine) => void
): Promise<PipelineRunResult> {
	const startedAt = new Date().toISOString();
	const candidateUnits = randomBetween(sources.length * 12, sources.length * 22);
	const entitiesDetected = randomBetween(sources.length * 4, sources.length * 9);
	const relationshipsDetected = randomBetween(entitiesDetected, Math.round(entitiesDetected * 1.6));
	const conflictsFound = randomBetween(0, Math.max(1, Math.round(sources.length * 0.6)));
	const retainedForReview = randomBetween(0, Math.max(1, Math.round(candidateUnits * 0.05)));

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

	const ctx: RunContext = {
		sources,
		candidateUnits,
		entitiesDetected,
		relationshipsDetected,
		relationTypes: RELATION_TYPES.slice(0, randomBetween(3, RELATION_TYPES.length)),
		conflictsFound,
		retainedForReview,
		ragStrategyName: ragStrategy.name,
		storageTopology: ragStrategy.storageTopology
	};

	for (const phase of PIPELINE_PHASE_ORDER) {
		onPhaseUpdate({ phase, status: PhaseStatus.RUNNING, progress: 0, startedAt: new Date().toISOString() });

		const lines = phaseLogLines(phase, ctx);
		for (let i = 0; i < lines.length; i++) {
			await thinkingDelay();
			onLogLine({ id: nextLineId(), phase, text: lines[i], timestamp: new Date().toISOString() });
			onPhaseUpdate({ phase, status: PhaseStatus.RUNNING, progress: Math.round(((i + 1) / lines.length) * 100) });
		}

		onPhaseUpdate({ phase, status: PhaseStatus.DONE, progress: 100, finishedAt: new Date().toISOString() });
	}

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
		conflictsFound > 0 || retainedForReview > 0 ? ValidationStatus.CONDITIONAL : ValidationStatus.READY;

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
		relationTypes: ctx.relationTypes,
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
