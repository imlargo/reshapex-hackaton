import { ActivitySeverity, FactStatus, SourceType } from '$lib/types/knowledge';
import type { KnowledgeStats } from '$lib/types/knowledge';

function delay(ms: number) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

function minutesAgo(minutes: number) {
	return new Date(Date.now() - minutes * 60 * 1000).toISOString();
}

// TODO: reemplazar por una llamada real (GET /knowledge/snapshot vía BaseService)
// cuando el backend de la capa de conocimiento exista. Por ahora simula la
// respuesta para poder construir la UI del dashboard.
export async function getKnowledgeSnapshot(): Promise<KnowledgeStats> {
	await delay(500);

	return {
		totalFacts: 1284,
		statusBreakdown: [
			{ status: FactStatus.VERIFIED, count: 967 },
			{ status: FactStatus.CONFLICT, count: 84 },
			{ status: FactStatus.UNREVIEWED, count: 233 }
		],
		avgConfidence: 0.86,
		escalationsPending: 12,
		sourcesIngested: 47,
		sourceBreakdown: [
			{ type: SourceType.PDF, count: 21 },
			{ type: SourceType.API, count: 12 },
			{ type: SourceType.EXCEL, count: 8 },
			{ type: SourceType.MARKDOWN, count: 4 },
			{ type: SourceType.FILE, count: 2 }
		],
		factsTrend: [
			{ label: 'Sem 1', facts: 210 },
			{ label: 'Sem 2', facts: 430 },
			{ label: 'Sem 3', facts: 640 },
			{ label: 'Sem 4', facts: 890 },
			{ label: 'Sem 5', facts: 1080 },
			{ label: 'Sem 6', facts: 1284 }
		],
		lastRunAt: minutesAgo(42),
		recentActivity: [
			{
				id: 'act-1',
				message:
					'Conflicto detectado: distancia mínima de montaje del S300 difiere entre ficha técnica y listado de distribuidor.',
				timestamp: minutesAgo(12),
				severity: ActivitySeverity.CRITICAL
			},
			{
				id: 'act-2',
				message: 'Publicación completada: 46 hechos nuevos incorporados desde el catálogo W4S-3.',
				timestamp: minutesAgo(42),
				severity: ActivitySeverity.INFO
			},
			{
				id: 'act-3',
				message: 'Escalado a revisión humana: confianza de PL/SIL del microScan3 por debajo del umbral.',
				timestamp: minutesAgo(65),
				severity: ActivitySeverity.WARNING
			},
			{
				id: 'act-4',
				message: 'Reconciliación: 3 hechos del UE410 quedaron sin resolver por falta de una tercera fuente.',
				timestamp: minutesAgo(130),
				severity: ActivitySeverity.WARNING
			},
			{
				id: 'act-5',
				message: 'Ingesta completada: 5 fuentes nuevas (2 PDF, 1 API, 2 Excel) en cola de procesamiento.',
				timestamp: minutesAgo(210),
				severity: ActivitySeverity.INFO
			}
		]
	};
}
