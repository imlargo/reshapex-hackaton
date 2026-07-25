import { PipelinePhase, PhaseStatus, SourceType, ValidationStatus, ConfidenceLevel } from '$lib/types/knowledge';
import type { KnowledgeSourceInput, PipelinePhaseState, PipelineRunResult, ValidationCheck } from '$lib/types/knowledge';
import { CheckStatus } from '$lib/types/knowledge';
import {
	ArchitectureStatus,
	type ArchitectureOption,
	type EntityRelationSample,
	type PipelineDecisionEvent
} from '../types';
import { PIPELINE_PHASE_ORDER, SOURCE_TYPE_LABELS } from '$lib/config';

function delay(ms: number) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

function randomBetween(min: number, max: number): number {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

function pick<T>(items: T[]): T {
	return items[randomBetween(0, items.length - 1)];
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

interface DocumentProfile {
	documentClass: string;
	authority: string;
}

const DOCUMENT_PROFILES: Record<SourceType, DocumentProfile> = {
	[SourceType.PDF]: { documentClass: 'Ficha técnica', authority: 'Fabricante' },
	[SourceType.EXCEL]: { documentClass: 'Catálogo tabular', authority: 'Distribuidor' },
	[SourceType.MARKDOWN]: { documentClass: 'Nota técnica', authority: 'Interno' },
	[SourceType.API]: { documentClass: 'Catálogo dinámico', authority: 'Distribuidor' },
	[SourceType.FILE]: { documentClass: 'Documento genérico', authority: 'Sin verificar' }
};

const EXTRACTION_METHODS: Record<SourceType, { method: string; rationale: string }> = {
	[SourceType.PDF]: {
		method: 'Extracción por tablas (layout-aware)',
		rationale: 'Preserva la relación parámetro–valor de las fichas técnicas.'
	},
	[SourceType.EXCEL]: {
		method: 'Extracción por filas',
		rationale: 'Cada fila ya es una unidad comparable (SKU, spec, valor).'
	},
	[SourceType.MARKDOWN]: {
		method: 'Extracción por encabezados',
		rationale: 'La jerarquía de encabezados refleja la estructura del contenido.'
	},
	[SourceType.API]: {
		method: 'Extracción por esquema de respuesta',
		rationale: 'El JSON ya trae campos tipados; no requiere heurística de layout.'
	},
	[SourceType.FILE]: {
		method: 'Extracción de texto plano',
		rationale: 'Sin estructura reconocible; se trata como texto corrido.'
	}
};

function uniqueTypes(sources: KnowledgeSourceInput[]): SourceType[] {
	return [...new Set(sources.map((s) => s.type))];
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
	architectureOptions: ArchitectureOption[];
	chosenArchitecture: ArchitectureOption;
	ragStorageTopology: string;
}

function chooseArchitecture(ctx: {
	hasApiOrTabular: boolean;
	hasOnlyProse: boolean;
	density: number;
	entitiesDetected: number;
}): ArchitectureOption[] {
	const complexGateMet = ctx.density > 1.3 && ctx.entitiesDetected >= 6;

	let winner: 'vectorial' | 'relacional' | 'grafo-simple' | 'grafo-complejo';
	if (ctx.hasOnlyProse) winner = 'vectorial';
	else if (ctx.hasApiOrTabular && ctx.density <= 1.3) winner = 'relacional';
	else if (complexGateMet) winner = 'grafo-complejo';
	else winner = 'grafo-simple';

	const status = (key: typeof winner, blocked = false): ArchitectureStatus =>
		key === winner
			? ArchitectureStatus.SELECTED
			: blocked
				? ArchitectureStatus.BLOCKED
				: ArchitectureStatus.AVAILABLE;

	return [
		{
			name: 'Vectorial',
			algorithm: 'Embeddings densos + búsqueda por vecinos cercanos',
			status: status('vectorial'),
			reason:
				winner === 'vectorial'
					? 'El corpus es sobre todo prosa libre — preguntas semánticas sobre texto, sin necesidad de estructura relacional.'
					: 'Cubriría las preguntas semánticas, pero perdería los filtros exactos y las relaciones que este corpus sí tiene.',
			limitations: 'No resuelve filtros exactos ni recorridos de varios saltos entre entidades.'
		},
		{
			name: 'Relacional',
			algorithm: 'Índice de campos + filtros y comparaciones exactas',
			status: status('relacional'),
			reason:
				winner === 'relacional'
					? 'Hay datos tabulares o de API con campos bien definidos — conviene filtrar y comparar por campo exacto.'
					: 'Útil para catálogos tabulares, pero este corpus depende más de relaciones entre entidades que de filtros por campo.',
			limitations: 'No captura relaciones implícitas entre productos ni preguntas abiertas sobre texto libre.'
		},
		{
			name: 'Grafo simple',
			algorithm: 'Grafo de entidades, relaciones a un salto',
			status: status('grafo-simple'),
			reason:
				winner === 'grafo-simple'
					? 'Hay relaciones directas entre productos y accesorios que conviene navegar como grafo, sin necesitar recorridos largos.'
					: 'Serviría para relaciones directas, pero no es la opción más simple que ya resuelve el caso.',
			limitations: 'No modela dependencias densas ni recorridos de más de un salto.'
		},
		{
			name: 'Grafo complejo',
			algorithm: 'Grafo multi-salto + ranking de caminos',
			status: status('grafo-complejo', !complexGateMet),
			reason: complexGateMet
				? winner === 'grafo-complejo'
					? `Densidad de relaciones alta (${ctx.density.toFixed(1)}x) sobre ${ctx.entitiesDetected} entidades — hay evidencia suficiente para justificar recorridos multi-salto.`
					: 'El corpus lo soportaría, pero un grafo simple ya resuelve el caso sin la complejidad extra.'
				: 'No se habilita: la complejidad extra solo se activa si el caso la necesita y hay evidencia suficiente.',
			gate: complexGateMet
				? undefined
				: `Requiere densidad de relaciones > 1.3 y ≥ 6 entidades — este corpus mide ${ctx.density.toFixed(1)}x sobre ${ctx.entitiesDetected}.`,
			limitations: 'Mayor costo de mantenimiento; solo se justifica con dependencias realmente densas.'
		}
	];
}

function buildContext(sources: KnowledgeSourceInput[]): RunContext {
	const candidateUnits = randomBetween(sources.length * 12, sources.length * 22);
	const entitiesDetected = randomBetween(sources.length * 4, sources.length * 9);
	const relationshipsDetected = randomBetween(entitiesDetected, Math.round(entitiesDetected * 1.6));
	const conflictsFound = randomBetween(0, Math.max(1, Math.round(sources.length * 0.6)));
	const retainedForReview = randomBetween(0, Math.max(1, Math.round(candidateUnits * 0.05)));
	const relationTypes = RELATION_TYPES.slice(0, randomBetween(3, RELATION_TYPES.length));

	const hasApiSource = sources.some((s) => s.type === SourceType.API);
	const hasTabularSource = sources.some((s) => s.type === SourceType.EXCEL);
	const hasOnlyProse = !hasApiSource && !hasTabularSource;
	const density = relationshipsDetected / Math.max(1, entitiesDetected);

	const architectureOptions = chooseArchitecture({
		hasApiOrTabular: hasApiSource || hasTabularSource,
		hasOnlyProse,
		density,
		entitiesDetected
	});
	const chosenArchitecture = architectureOptions.find((o) => o.status === ArchitectureStatus.SELECTED)!;

	const ragStorageTopology =
		chosenArchitecture.name === 'Vectorial'
			? 'Índice vectorial único por familia de producto'
			: chosenArchitecture.name === 'Relacional'
				? 'Tablas indexadas por campo, sin grafo'
				: chosenArchitecture.name === 'Grafo simple'
					? 'Grafo de entidades a un salto + índice vectorial de apoyo'
					: 'Grafo multi-salto con ranking de caminos + índice vectorial de apoyo';

	return {
		sources,
		candidateUnits,
		entitiesDetected,
		relationshipsDetected,
		relationTypes,
		relationSamples: sampleRelations(relationTypes),
		conflictsFound,
		retainedForReview,
		architectureOptions,
		chosenArchitecture,
		ragStorageTopology
	};
}

type PendingDecision = Omit<PipelineDecisionEvent, 'id' | 'timestamp'>;

function decisionsForPhase(phase: PipelinePhase, ctx: RunContext): PendingDecision[] {
	const { sources } = ctx;
	switch (phase) {
		case PipelinePhase.INVENTORY:
			return [
				{
					phase,
					question: '¿Qué documentos existen y qué autoridad aporta cada tipo?',
					inputs: sources.slice(0, 6).map((s) => `${s.name} (${SOURCE_TYPE_LABELS[s.type]})`),
					decision: `${sources.length} fuente${sources.length === 1 ? '' : 's'} aceptada${sources.length === 1 ? '' : 's'}, clasificada${sources.length === 1 ? '' : 's'} por tipo, idioma y autoridad.`,
					criteria:
						'Se distingue una ficha oficial del fabricante de un listado de distribuidor — no se interpretan igual.',
					artifact: {
						kind: 'classification',
						rows: sources.map((s) => ({
							source: s.name,
							documentClass: DOCUMENT_PROFILES[s.type].documentClass,
							language: 'Español',
							authority: DOCUMENT_PROFILES[s.type].authority
						}))
					}
				}
			];
		case PipelinePhase.EXTRACTION: {
			const types = uniqueTypes(sources);
			return [
				{
					phase,
					question: '¿Cómo convertir cada formato heterogéneo en unidades comparables?',
					inputs: types.map((t) => `${SOURCE_TYPE_LABELS[t]} presente en el corpus`),
					decision: 'Un método de extracción distinto por tipo de fuente, no un parser único.',
					criteria: 'El método preserva la relación parámetro–valor; nunca inventa estructura donde no la hay.',
					artifact: {
						kind: 'extraction-methods',
						rows: types.map((t) => ({
							sourceLabel: SOURCE_TYPE_LABELS[t],
							method: EXTRACTION_METHODS[t].method,
							rationale: EXTRACTION_METHODS[t].rationale
						}))
					}
				}
			];
		}
		case PipelinePhase.NORMALIZATION:
			return [
				{
					phase,
					question: '¿Cómo unificar unidades, nombres y formatos entre fuentes?',
					inputs: [`${ctx.candidateUnits} unidades de contenido extraídas`, 'Unidades mixtas: mm, cm, IP, PL/SIL'],
					decision: `${ctx.candidateUnits} unidades normalizadas a un esquema común.`,
					criteria: 'Dos valores se unifican solo si representan la misma magnitud verificable, no por parecido textual.',
					artifact: {
						kind: 'normalization',
						examples: [
							{ field: 'Distancia de montaje', before: '15 cm', after: '150 mm' },
							{ field: 'Grado de protección', before: 'IP 65', after: 'IP65' },
							{ field: 'Type code', before: 'S30A-6011GA', after: 'S300 / S30A-6011GA' }
						]
					}
				}
			];
		case PipelinePhase.ENTITY_RELATIONS:
			return [
				{
					phase,
					question: '¿Qué conceptos deben convertirse en registros o nodos?',
					inputs: [`${ctx.candidateUnits} unidades normalizadas`, `Tipos de relación candidatos: ${ctx.relationTypes.join(', ')}`],
					decision: `${ctx.entitiesDetected} entidades y ${ctx.relationshipsDetected} relaciones con procedencia trazada.`,
					criteria: 'Una relación se conserva solo si al menos una fuente la sustenta explícitamente — nunca se infiere sin evidencia.',
					artifact: { kind: 'relations', samples: ctx.relationSamples }
				}
			];
		case PipelinePhase.RAG_STRATEGY:
			return [
				{
					phase,
					question: '¿Qué estrategia de almacenamiento y búsqueda encaja mejor con este corpus?',
					inputs: [
						`${ctx.entitiesDetected} entidades, ${ctx.relationshipsDetected} relaciones`,
						`Fuentes: ${uniqueTypes(sources).map((t) => SOURCE_TYPE_LABELS[t]).join(', ')}`
					],
					decision: `${ctx.chosenArchitecture.name}: ${ctx.chosenArchitecture.algorithm}.`,
					criteria: 'Se elige la arquitectura más simple que resuelve el caso — la complejidad extra solo se habilita si hay evidencia suficiente.',
					artifact: { kind: 'architecture', options: ctx.architectureOptions }
				}
			];
		case PipelinePhase.INDEXING:
			return [
				{
					phase,
					question: '¿Cómo construir el índice consultable sobre el paquete normalizado?',
					inputs: [`Arquitectura elegida: ${ctx.chosenArchitecture.name}`, `${ctx.candidateUnits} unidades a indexar`],
					decision: `Índice listo: ${ctx.ragStorageTopology}.`,
					criteria: 'Cada resultado del índice debe conservar un ID de evidencia citable, no solo el texto.',
					artifact: {
						kind: 'index-stats',
						stats: {
							unitsIndexed: ctx.candidateUnits,
							dimensions: ctx.chosenArchitecture.name === 'Vectorial' ? 768 : 0,
							graphEdges: ctx.chosenArchitecture.name.startsWith('Grafo') ? ctx.relationshipsDetected : 0
						}
					}
				}
			];
		case PipelinePhase.VALIDATION: {
			const decisions: PendingDecision[] = [
				{
					phase,
					question: '¿Qué impide afirmar que la base está completa?',
					inputs: [`${ctx.conflictsFound} discrepancia(s) entre fuentes`, `${ctx.retainedForReview} unidad(es) bajo el umbral de confianza`],
					decision:
						ctx.conflictsFound > 0
							? `${ctx.conflictsFound} contradicción(es) detectada(s) entre fuentes.`
							: 'No se detectaron contradicciones entre las fuentes suministradas.',
					criteria: 'Una discrepancia se marca como conflicto solo si dos fuentes independientes afirman valores distintos para el mismo hecho — nunca se promedia ni se elige una.',
					artifact:
						ctx.conflictsFound > 0
							? {
									kind: 'conflict',
									sample: {
										fact: 'Distancia mínima de montaje',
										sourceA: { name: sources[0]?.name ?? 'ficha técnica', value: '150 mm' },
										sourceB: {
											name: sources[1]?.name ?? sources[0]?.name ?? 'listado de distribuidor',
											value: '120 mm'
										}
									}
								}
							: { kind: 'text', content: 'Sin vacíos ni contradicciones detectadas en este corpus.' }
				}
			];

			const status =
				ctx.conflictsFound > 0 || ctx.retainedForReview > 0 ? ValidationStatus.CONDITIONAL : ValidationStatus.READY;
			decisions.push({
				phase,
				question: '¿La base recupera evidencia suficiente para responder?',
				inputs: [`${ctx.candidateUnits} unidades indexadas`, `Estado de conflictos: ${ctx.conflictsFound > 0 ? 'con discrepancias' : 'sin discrepancias'}`],
				decision:
					status === ValidationStatus.READY
						? 'Lista para responder sin revisión adicional.'
						: 'Condicional — puede responder, con limitaciones marcadas para revisión humana.',
				criteria: 'Se exige al menos una cita verificable por afirmación; si no alcanza, la respuesta se retiene en vez de inventarse.',
				artifact: {
					kind: 'readiness',
					summary: {
						evidenceRetrieved: ctx.candidateUnits,
						evidenceGrade: status === ValidationStatus.READY ? 'fuerte' : 'parcial',
						confidence: ctx.conflictsFound > 0 ? 'baja' : status === ValidationStatus.READY ? 'alta' : 'media',
						status: status === ValidationStatus.READY ? 'Lista' : 'Condicional',
						unresolvedRisk:
							ctx.conflictsFound > 0
								? 'Hechos con fuentes discrepantes sin confirmar por un humano.'
								: ctx.retainedForReview > 0
									? 'Unidades bajo el umbral de confianza, pendientes de revisión.'
									: 'Ninguno identificado en esta corrida.',
						nextAction:
							status === ValidationStatus.READY
								? 'Publicar capacidades de consulta.'
								: 'Revisar los hechos marcados antes de exponer respuestas automáticas.'
					}
				}
			});
			return decisions;
		}
	}
}

// TODO: reemplazar por una conexión real al pipeline (contra el boundary
// Usuario1 -> Usuario3 descrito en analisis/agentsprint/03_contracts/INTERFACES.md)
// cuando exista el backend. Por ahora simula el avance fase por fase, decisión
// por decisión, para poder construir la retroalimentación visual del pipeline.
// Ver también el handoff de demo visual: esto es una traza de decisiones y
// datos observables, nunca chain-of-thought del modelo.
export async function simulatePipelineRun(
	sources: KnowledgeSourceInput[],
	onPhaseUpdate: (update: PipelinePhaseState) => void,
	onDecision: (event: PipelineDecisionEvent) => void
): Promise<PipelineRunResult> {
	const startedAt = new Date().toISOString();
	const ctx = buildContext(sources);

	for (const phase of PIPELINE_PHASE_ORDER) {
		onPhaseUpdate({ phase, status: PhaseStatus.RUNNING, progress: 0, startedAt: new Date().toISOString() });

		const decisions = decisionsForPhase(phase, ctx);
		for (let i = 0; i < decisions.length; i++) {
			const ticks = randomBetween(3, 5);
			for (let t = 1; t <= ticks; t++) {
				await delay(randomBetween(280, 650));
				onPhaseUpdate({
					phase,
					status: PhaseStatus.RUNNING,
					progress: Math.round(((i + t / ticks) / decisions.length) * 100)
				});
			}
			onDecision({ ...decisions[i], id: nextEventId(), timestamp: new Date().toISOString() });
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
			status: ctx.conflictsFound > 0 ? CheckStatus.FAIL : CheckStatus.PASS,
			detail:
				ctx.conflictsFound > 0
					? `${ctx.conflictsFound} hechos con fuentes discrepantes — no se resolvieron automáticamente.`
					: 'Sin discrepancias entre las fuentes suministradas.'
		},
		{
			name: 'Confianza mínima',
			status: ctx.retainedForReview > 0 ? CheckStatus.WARNING : CheckStatus.PASS,
			detail:
				ctx.retainedForReview > 0
					? `${ctx.retainedForReview} unidades por debajo del umbral de confianza, retenidas para revisión.`
					: 'Todas las unidades superan el umbral de confianza.'
		}
	];

	const validationStatus =
		ctx.conflictsFound > 0 || ctx.retainedForReview > 0 ? ValidationStatus.CONDITIONAL : ValidationStatus.READY;

	const nextAction =
		validationStatus === ValidationStatus.READY
			? 'Lista para responder consultas sin revisión adicional.'
			: 'Revisar los hechos marcados antes de exponer respuestas automáticas.';

	return {
		id: `run-${Date.now()}`,
		startedAt,
		finishedAt: new Date().toISOString(),
		sourcesCount: sources.length,
		corpusProfile: `${sources.length} fuentes clasificadas por tipo y autoridad.`,
		transformationPlan:
			'Extracción por tablas para fichas técnicas en PDF, por filas para catálogos en Excel y por encabezados para Markdown; toda unidad conserva su ubicación de origen.',
		entitiesDetected: ctx.entitiesDetected,
		relationshipsDetected: ctx.relationshipsDetected,
		relationTypes: ctx.relationTypes,
		ragStrategy: {
			name: ctx.chosenArchitecture.name,
			storageTopology: ctx.ragStorageTopology,
			rationale: ctx.chosenArchitecture.reason
		},
		validationStatus,
		validationChecks,
		nextAction,
		sampleAnswer: {
			question: '¿Cuál es la distancia mínima de montaje recomendada?',
			answer:
				ctx.conflictsFound > 0
					? 'Las fuentes discrepan en este valor — la respuesta queda retenida hasta que un humano confirme cuál es correcta.'
					: 'Según la ficha técnica ingerida, la distancia mínima de montaje cumple con ISO 13855 para el punto de operación evaluado.',
			citation: sources[0]?.name ?? 'fuente ingerida',
			confidence: ctx.conflictsFound > 0 ? ConfidenceLevel.LOW : ConfidenceLevel.HIGH
		}
	};
}
