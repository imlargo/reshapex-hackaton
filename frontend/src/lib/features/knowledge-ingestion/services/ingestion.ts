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
import type { PipelineTraceEvent, EntityRelationSample } from '../types';
import { PIPELINE_PHASE_ORDER, SOURCE_TYPE_LABELS } from '$lib/config';

function delay(ms: number) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

function randomBetween(min: number, max: number): number {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Pausa "orgánica": casi siempre corta, a veces una pausa larga de deliberación.
// Las decisiones y comparaciones piensan un poco más que una línea suelta.
function thinkingDelay(weight: 'line' | 'decision' = 'line'): Promise<unknown> {
	if (weight === 'decision') return delay(randomBetween(1200, 2200));
	const long = Math.random() < 0.16;
	return delay(long ? randomBetween(1400, 2600) : randomBetween(450, 1300));
}

let eventIdSeq = 0;
function nextEventId(): string {
	eventIdSeq += 1;
	return `event-${eventIdSeq}`;
}

const RELATION_TYPES = [
	'compatible_con',
	'reemplaza_a',
	'requiere_accesorio',
	'pertenece_a_familia',
	'cumple_norma'
];

const ENTITY_POOL = [
	'S300',
	'W4S-3',
	'microScan3',
	'UE410',
	'Cable M12x4',
	'Soporte de montaje',
	'Serie S300',
	'Fuente 24V DC',
	'Cortina óptica C4000'
];

function pick<T>(items: T[]): T {
	return items[randomBetween(0, items.length - 1)];
}

function sampleRelations(relationTypes: string[]): EntityRelationSample[] {
	const count = randomBetween(3, 5);
	const samples: EntityRelationSample[] = [];
	for (let i = 0; i < count; i++) {
		const subject = pick(ENTITY_POOL);
		let object = pick(ENTITY_POOL);
		while (object === subject) object = pick(ENTITY_POOL);
		samples.push({ subject, predicate: pick(relationTypes), object });
	}
	return samples;
}

function corpusProfile(sources: KnowledgeSourceInput[]): string {
	const counts = new Map<SourceType, number>();
	for (const source of sources) counts.set(source.type, (counts.get(source.type) ?? 0) + 1);
	const parts = [...counts.entries()].map(
		([type, count]) => `${count} ${SOURCE_TYPE_LABELS[type]}${count > 1 ? 's' : ''}`
	);
	return `${sources.length} fuentes clasificadas: ${parts.join(', ')}.`;
}

// Omit distributivo: Omit normal colapsa la unión discriminada a sus campos
// comunes y pierde `text`/`options`/`samples`/`sample` por variante.
type DistributiveOmit<T, K extends keyof T> = T extends unknown ? Omit<T, K> : never;
type PendingEvent = DistributiveOmit<PipelineTraceEvent, 'id' | 'timestamp'>;

function log(phase: PipelinePhase, text: string): PendingEvent {
	return { kind: 'log', phase, text };
}

interface RunContext {
	sources: KnowledgeSourceInput[];
	candidateUnits: number;
	entitiesDetected: number;
	relationshipsDetected: number;
	relationTypes: string[];
	relationSamples: EntityRelationSample[];
	conflictsFound: number;
	retainedForReview: number;
	ragStrategyName: string;
	storageTopology: string;
	ragOptions: { name: string; summary: string; score: number }[];
	ragRationale: string;
}

function phaseEvents(phase: PipelinePhase, ctx: RunContext): PendingEvent[] {
	const { sources } = ctx;
	switch (phase) {
		case PipelinePhase.INVENTORY: {
			const events: PendingEvent[] = [
				log(phase, `Clasificando ${sources.length} fuentes por tipo, idioma y calidad…`)
			];
			for (const source of sources.slice(0, 4)) {
				events.push(
					log(
						phase,
						`${source.name} → ${SOURCE_TYPE_LABELS[source.type]}${source.sizeLabel ? `, ${source.sizeLabel}` : ''}`
					)
				);
			}
			if (sources.length > 4) events.push(log(phase, `… y ${sources.length - 4} fuente(s) más`));
			events.push(log(phase, 'Detectado idioma dominante: español'));
			events.push(log(phase, corpusProfile(sources)));
			return events;
		}
		case PipelinePhase.EXTRACTION:
			return [
				log(phase, 'Aplicando extracción por tablas a documentos PDF…'),
				log(phase, 'Aplicando extracción por filas a hojas de cálculo…'),
				log(phase, 'Aplicando extracción por encabezados a Markdown…'),
				log(phase, 'Conservando ubicación de origen (página, fila o sección) por unidad'),
				log(phase, `${ctx.candidateUnits} unidades de contenido extraídas`)
			];
		case PipelinePhase.NORMALIZATION:
			return [
				log(phase, 'Unificando unidades de medida (mm, kg, IP, PL/SIL)…'),
				log(phase, 'Normalizando nombres de producto y variantes de type code…'),
				log(phase, 'Resolviendo sinónimos entre ficha técnica y listado de distribuidor…'),
				log(phase, `${ctx.candidateUnits} unidades normalizadas a un esquema común`)
			];
		case PipelinePhase.ENTITY_RELATIONS:
			return [
				log(phase, 'Detectando entidades: productos, accesorios y normas aplicables…'),
				{ kind: 'relations', phase, samples: ctx.relationSamples },
				log(
					phase,
					`${ctx.entitiesDetected} entidades y ${ctx.relationshipsDetected} relaciones con procedencia trazada`
				)
			];
		case PipelinePhase.RAG_STRATEGY:
			return [
				log(phase, 'Evaluando la forma del corpus (texto libre vs. datos tabulares)…'),
				{
					kind: 'decision',
					phase,
					question: '¿Qué estrategia de recuperación usar?',
					options: ctx.ragOptions,
					chosen: ctx.ragStrategyName,
					rationale: ctx.ragRationale
				},
				log(phase, `Topología de almacenamiento: ${ctx.storageTopology}`)
			];
		case PipelinePhase.INDEXING:
			return [
				log(phase, 'Construyendo índice de recuperación…'),
				log(phase, 'Indexando relaciones en el grafo de entidades…'),
				log(phase, `Índice listo sobre ${ctx.candidateUnits} unidades de contenido`)
			];
		case PipelinePhase.VALIDATION: {
			const events: PendingEvent[] = [log(phase, 'Verificando cobertura de citación por hecho…')];
			if (ctx.conflictsFound > 0) {
				events.push(
					log(
						phase,
						`⚠ ${ctx.conflictsFound} hecho(s) con fuentes discrepantes — se marcan, no se resuelven automáticamente`
					)
				);
				events.push({
					kind: 'conflict',
					phase,
					sample: {
						fact: 'Distancia mínima de montaje',
						sourceA: { name: sources[0]?.name ?? 'ficha técnica', value: '150 mm' },
						sourceB: {
							name: sources[1]?.name ?? sources[0]?.name ?? 'listado de distribuidor',
							value: '120 mm'
						}
					}
				});
			} else {
				events.push(log(phase, 'Sin discrepancias entre las fuentes suministradas'));
			}
			events.push(log(phase, 'Calculando confianza por hecho…'));
			if (ctx.retainedForReview > 0) {
				events.push(
					log(phase, `${ctx.retainedForReview} unidad(es) bajo el umbral de confianza, retenidas para revisión`)
				);
			}
			return events;
		}
	}
}

// TODO: reemplazar por una conexión real al pipeline (contra el boundary
// Usuario1 -> Usuario3 descrito en analisis/agentsprint/03_contracts/INTERFACES.md)
// cuando exista el backend. Por ahora simula el avance fase por fase, evento por
// evento, para poder construir la retroalimentación visual del pipeline.
export async function simulatePipelineRun(
	sources: KnowledgeSourceInput[],
	onPhaseUpdate: (update: PipelinePhaseState) => void,
	onTraceEvent: (event: PipelineTraceEvent) => void
): Promise<PipelineRunResult> {
	const startedAt = new Date().toISOString();
	const candidateUnits = randomBetween(sources.length * 12, sources.length * 22);
	const entitiesDetected = randomBetween(sources.length * 4, sources.length * 9);
	const relationshipsDetected = randomBetween(entitiesDetected, Math.round(entitiesDetected * 1.6));
	const conflictsFound = randomBetween(0, Math.max(1, Math.round(sources.length * 0.6)));
	const retainedForReview = randomBetween(0, Math.max(1, Math.round(candidateUnits * 0.05)));
	const relationTypes = RELATION_TYPES.slice(0, randomBetween(3, RELATION_TYPES.length));

	const hasApiSource = sources.some((source) => source.type === SourceType.API);
	const hasTabularSource = sources.some((source) => source.type === SourceType.EXCEL);
	const favorsHybrid = hasApiSource || hasTabularSource;

	const hybridOption = {
		name: 'Retrieval híbrido (léxico + embeddings)',
		summary: 'Combina búsqueda léxica y semántica sobre un grafo de entidades.',
		score: favorsHybrid ? randomBetween(78, 92) / 100 : randomBetween(35, 52) / 100
	};
	const denseOption = {
		name: 'Recuperación densa por embeddings',
		summary: 'Un único índice vectorial por familia de producto, más simple de mantener.',
		score: favorsHybrid ? randomBetween(35, 52) / 100 : randomBetween(78, 90) / 100
	};
	const ragOptions = [hybridOption, denseOption];

	const ragStrategy = favorsHybrid
		? {
				name: hybridOption.name,
				storageTopology: 'Índice vectorial + grafo de entidades producto-accesorio',
				rationale:
					'El corpus mezcla texto libre con datos tabulares o de API, así que conviene combinar recuperación léxica y semántica sobre un grafo que preserve las relaciones entre productos.'
			}
		: {
				name: denseOption.name,
				storageTopology: 'Índice vectorial único por familia de producto',
				rationale:
					'El corpus es homogéneo (solo documentos de texto libre), así que un índice vectorial simple cubre la mayoría de las consultas sin costo adicional de mantener un grafo.'
			};

	const ctx: RunContext = {
		sources,
		candidateUnits,
		entitiesDetected,
		relationshipsDetected,
		relationTypes,
		relationSamples: sampleRelations(relationTypes),
		conflictsFound,
		retainedForReview,
		ragStrategyName: ragStrategy.name,
		storageTopology: ragStrategy.storageTopology,
		ragOptions,
		ragRationale: ragStrategy.rationale
	};

	for (const phase of PIPELINE_PHASE_ORDER) {
		onPhaseUpdate({ phase, status: PhaseStatus.RUNNING, progress: 0, startedAt: new Date().toISOString() });

		const events = phaseEvents(phase, ctx);
		for (let i = 0; i < events.length; i++) {
			await thinkingDelay(events[i].kind === 'log' ? 'line' : 'decision');
			onTraceEvent({ ...events[i], id: nextEventId(), timestamp: new Date().toISOString() });
			onPhaseUpdate({ phase, status: PhaseStatus.RUNNING, progress: Math.round(((i + 1) / events.length) * 100) });
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
		relationTypes,
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
