import {
	CheckStatus,
	ConfidenceLevel,
	PipelinePhase,
	ValidationStatus
} from '$lib/types/knowledge';
import type { PipelineRunResult, ValidationCheck } from '$lib/types/knowledge';
import type { EntityRelationSample, PipelineDecisionEvent } from '../types';
import { ArchitectureStatus } from '../types';

interface BackendBuildPayload {
	build: {
		inventory: {
			objective?: string;
			sources?: Array<{ name?: string; status?: string }>;
			limitations?: string[];
		};
		package: {
			content_units?: unknown[];
			entities?: Array<{ id: string; label: string; type: string }>;
			relationships?: Array<{
				subject_id: string;
				predicate: string;
				object_id: string;
				confidence?: string;
			}>;
			processing_report?: {
				method_summary?: string;
				accepted?: number;
				failed?: number;
				warnings?: string[];
			};
		};
		plan: {
			strategy?: {
				name?: string;
				selection_rationale?: string;
				search_algorithm?: string;
			};
			storage?: { topology?: string; selection_rationale?: string };
			index?: {
				index_id?: string;
				status?: string;
				metrics?: Record<string, string | number | boolean>;
			};
		};
		validation: {
			status?: string;
			checks?: Array<{ name: string; status: string; detail: string }>;
			next_action?: string;
			limitations?: string[];
		};
		readiness?: string;
	};
	query_contract: { index_id: string };
}

interface BackendQueryPayload {
	question: string;
	answer: {
		answer: string;
		citations: Array<{ evidence_id: string; claim?: string }>;
		confidence: string;
		evidence_grade: string;
		unresolved_risk: string;
		next_action: string;
	};
}

function mapValidationStatus(value: string | undefined): ValidationStatus {
	if (value === ValidationStatus.READY) return ValidationStatus.READY;
	if (value === ValidationStatus.NOT_READY) return ValidationStatus.NOT_READY;
	return ValidationStatus.CONDITIONAL;
}

function mapCheckStatus(value: string): CheckStatus {
	if (value === CheckStatus.PASS) return CheckStatus.PASS;
	if (value === CheckStatus.FAIL) return CheckStatus.FAIL;
	return CheckStatus.WARNING;
}

function mapConfidence(value: string): ConfidenceLevel {
	if (value === ConfidenceLevel.HIGH) return ConfidenceLevel.HIGH;
	if (value === ConfidenceLevel.LOW) return ConfidenceLevel.LOW;
	return ConfidenceLevel.MEDIUM;
}

function entityLabelMap(
	entities: Array<{ id: string; label: string }> | undefined
): Map<string, string> {
	return new Map((entities ?? []).map((entity) => [entity.id, entity.label]));
}

function relationSamples(
	relationships: BackendBuildPayload['build']['package']['relationships'],
	labels: Map<string, string>
): EntityRelationSample[] {
	return (relationships ?? []).slice(0, 6).map((relation) => ({
		subject: labels.get(relation.subject_id) ?? relation.subject_id,
		predicate: relation.predicate,
		object: labels.get(relation.object_id) ?? relation.object_id
	}));
}

export function buildDecisionEvents(payload: BackendBuildPayload): PipelineDecisionEvent[] {
	const { inventory, package: pkg, plan, validation } = payload.build;
	const labels = entityLabelMap(pkg.entities);
	const relations = relationSamples(pkg.relationships, labels);
	const timestamp = new Date().toISOString();

	return [
		{
			id: 'inventory-1',
			phase: PipelinePhase.INVENTORY,
			timestamp,
			question: '¿Qué fuentes del corpus SICK quedan aceptadas para procesamiento?',
			inputs: (inventory.sources ?? []).slice(0, 4).map((source) => source.name ?? 'source'),
			decision: `${inventory.sources?.length ?? 0} fuente(s) inventariadas para el objetivo del knowledge base.`,
			criteria: inventory.objective ?? 'Objetivo de consulta citada sobre productos SICK.',
			artifact: { kind: 'text', content: (inventory.limitations ?? []).join(' ') || 'Sin limitaciones adicionales.' }
		},
		{
			id: 'extraction-1',
			phase: PipelinePhase.EXTRACTION,
			timestamp,
			question: '¿Qué método híbrido se aplicó sobre PDF/HTML?',
			inputs: [`accepted=${pkg.processing_report?.accepted ?? 0}`, `failed=${pkg.processing_report?.failed ?? 0}`],
			decision: pkg.processing_report?.method_summary ?? 'Extracción híbrida completada.',
			criteria: 'Preservar texto utilizable y trazabilidad por fuente.',
			artifact: {
				kind: 'text',
				content: (pkg.processing_report?.warnings ?? []).slice(0, 2).join(' ') || 'Sin warnings críticos.'
			}
		},
		{
			id: 'normalization-1',
			phase: PipelinePhase.NORMALIZATION,
			timestamp,
			question: '¿Cuántas unidades normalizadas quedaron listas para indexar?',
			inputs: [`units=${pkg.content_units?.length ?? 0}`],
			decision: `${pkg.content_units?.length ?? 0} content units normalizados con evidence IDs.`,
			criteria: 'Chunks acotados y referenciables para citación.',
			artifact: { kind: 'text', content: 'Normalización alineada al contrato NormalizedKnowledgePackage.' }
		},
		{
			id: 'relations-1',
			phase: PipelinePhase.ENTITY_RELATIONS,
			timestamp,
			question: '¿Qué entidades y relaciones salieron del corpus?',
			inputs: [`entities=${pkg.entities?.length ?? 0}`, `relationships=${pkg.relationships?.length ?? 0}`],
			decision: `${pkg.entities?.length ?? 0} entidades y ${pkg.relationships?.length ?? 0} relaciones detectadas.`,
			criteria: 'Relaciones ancladas a evidencia cuando existe señal estructural.',
			artifact: { kind: 'relations', samples: relations }
		},
		{
			id: 'rag-1',
			phase: PipelinePhase.RAG_STRATEGY,
			timestamp,
			question: '¿Qué estrategia RAG seleccionó el compilador adaptativo?',
			inputs: [plan.strategy?.search_algorithm ?? 'unknown'],
			decision: plan.strategy?.name ?? 'Estrategia adaptativa',
			criteria: plan.strategy?.selection_rationale ?? 'Señales del paquete normalizado.',
			artifact: {
				kind: 'architecture',
				options: [
					{
						name: plan.strategy?.name ?? 'Adaptive RAG',
						algorithm: plan.strategy?.search_algorithm ?? 'adaptive',
						status: ArchitectureStatus.SELECTED,
						reason: plan.strategy?.selection_rationale ?? 'Selección automática',
						limitations: plan.storage?.topology ?? 'vector'
					}
				]
			}
		},
		{
			id: 'index-1',
			phase: PipelinePhase.INDEXING,
			timestamp,
			question: '¿El índice quedó consultable?',
			inputs: [plan.index?.index_id ?? payload.query_contract.index_id],
			decision: `Index ${plan.index?.index_id ?? payload.query_contract.index_id} status=${plan.index?.status ?? 'partial'}.`,
			criteria: 'Índice materializado sobre el paquete normalizado.',
			artifact: {
				kind: 'index-stats',
				stats: {
					unitsIndexed: pkg.content_units?.length ?? 0,
					dimensions: pkg.entities?.length ?? 0,
					graphEdges: pkg.relationships?.length ?? 0
				}
			}
		},
		{
			id: 'validation-1',
			phase: PipelinePhase.VALIDATION,
			timestamp,
			question: '¿La base quedó lista para consultas citadas?',
			inputs: [(validation.checks ?? []).map((check) => check.name).join(', ')],
			decision: `Readiness=${validation.status ?? payload.build.readiness ?? 'conditional'}.`,
			criteria: validation.next_action ?? 'Validar checks de readiness antes de exponer queries.',
			artifact: {
				kind: 'readiness',
				summary: {
					evidenceRetrieved: (validation.checks ?? []).length,
					evidenceGrade: validation.status ?? 'conditional',
					confidence: validation.status === 'ready' ? 'alta' : 'media',
					status: validation.status ?? 'conditional',
					unresolvedRisk: (validation.limitations ?? []).join(' ') || 'Ver checks con warning.',
					nextAction: validation.next_action ?? 'Revisar limitaciones antes de publicar.'
				}
			}
		}
	];
}

export function mapBackendToPipelineResult(
	buildPayload: BackendBuildPayload,
	queryPayload: BackendQueryPayload,
	sourcesCount: number
): PipelineRunResult {
	const { inventory, package: pkg, plan, validation } = buildPayload.build;
	const relationTypes = [...new Set((pkg.relationships ?? []).map((relation) => relation.predicate))];
	const validationChecks: ValidationCheck[] = (validation.checks ?? []).map((check) => ({
		name: check.name,
		status: mapCheckStatus(check.status),
		detail: check.detail
	}));
	const firstCitation = queryPayload.answer.citations[0];

	return {
		id: payloadRunId(buildPayload),
		startedAt: new Date().toISOString(),
		finishedAt: new Date().toISOString(),
		sourcesCount,
		corpusProfile: inventory.objective ?? 'Corpus SICK representativo',
		transformationPlan: pkg.processing_report?.method_summary ?? 'Pipeline híbrido U2 + compilador RAG U1',
		entitiesDetected: pkg.entities?.length ?? 0,
		relationshipsDetected: pkg.relationships?.length ?? 0,
		relationTypes,
		ragStrategy: {
			name: plan.strategy?.name ?? 'Adaptive RAG',
			storageTopology: plan.storage?.topology ?? 'vector',
			rationale: plan.strategy?.selection_rationale ?? plan.storage?.selection_rationale ?? ''
		},
		validationStatus: mapValidationStatus(validation.status ?? buildPayload.build.readiness),
		validationChecks,
		nextAction: validation.next_action ?? queryPayload.answer.next_action,
		sampleAnswer: {
			question: queryPayload.question,
			answer: queryPayload.answer.answer,
			citation: firstCitation?.evidence_id ?? 'sin-cita',
			confidence: mapConfidence(queryPayload.answer.confidence)
		}
	};
}

function payloadRunId(payload: BackendBuildPayload): string {
	return payload.query_contract.index_id;
}
