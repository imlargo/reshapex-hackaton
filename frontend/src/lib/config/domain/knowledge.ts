import { PipelinePhase, SourceType, FactStatus } from '$lib/types/knowledge';

// ─── Pipeline phases ──────────────────────────────────────────────────────────
// Orden fijo de las fases del pipeline de la capa de conocimiento (ver CONTEXT.md).
export const PIPELINE_PHASE_ORDER: PipelinePhase[] = [
	PipelinePhase.INGEST,
	PipelinePhase.PARSE,
	PipelinePhase.EXTRACT,
	PipelinePhase.NORMALIZE,
	PipelinePhase.RECONCILE,
	PipelinePhase.VALIDATE,
	PipelinePhase.PUBLISH
];

export const PIPELINE_PHASE_LABELS: Record<PipelinePhase, string> = {
	[PipelinePhase.INGEST]: 'Ingesta',
	[PipelinePhase.PARSE]: 'Parseo',
	[PipelinePhase.EXTRACT]: 'Extracción',
	[PipelinePhase.NORMALIZE]: 'Normalización',
	[PipelinePhase.RECONCILE]: 'Reconciliación',
	[PipelinePhase.VALIDATE]: 'Validación',
	[PipelinePhase.PUBLISH]: 'Publicación'
};

export const PIPELINE_PHASE_DESCRIPTIONS: Record<PipelinePhase, string> = {
	[PipelinePhase.INGEST]: 'Registra cada archivo, API o página tal como llega, sin transformarla.',
	[PipelinePhase.PARSE]: 'Convierte cada fuente a texto y estructura legible.',
	[PipelinePhase.EXTRACT]: 'Identifica hechos candidatos y guarda su procedencia.',
	[PipelinePhase.NORMALIZE]: 'Unifica unidades, nombres y formatos entre fuentes.',
	[PipelinePhase.RECONCILE]: 'Cruza fuentes equivalentes y marca los hechos en conflicto.',
	[PipelinePhase.VALIDATE]: 'Calcula confianza por hecho y retiene lo insuficiente para revisión.',
	[PipelinePhase.PUBLISH]: 'Escribe la nueva versión de la capa de conocimiento.'
};

// ─── Source types ─────────────────────────────────────────────────────────────
export const SOURCE_TYPE_LABELS: Record<SourceType, string> = {
	[SourceType.PDF]: 'PDF',
	[SourceType.EXCEL]: 'Excel',
	[SourceType.MARKDOWN]: 'Markdown',
	[SourceType.FILE]: 'Archivo',
	[SourceType.API]: 'API'
};

// Extensiones de archivo aceptadas por el intake, mapeadas a su SourceType.
export const SOURCE_FILE_EXTENSIONS: Record<string, SourceType> = {
	pdf: SourceType.PDF,
	xlsx: SourceType.EXCEL,
	xls: SourceType.EXCEL,
	csv: SourceType.EXCEL,
	md: SourceType.MARKDOWN,
	markdown: SourceType.MARKDOWN
};

export const SOURCE_INTAKE_ACCEPT =
	'.pdf,.xlsx,.xls,.csv,.md,.markdown,application/pdf,text/markdown,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';

// ─── Fact status ──────────────────────────────────────────────────────────────
export const FACT_STATUS_LABELS: Record<FactStatus, string> = {
	[FactStatus.VERIFIED]: 'Verificado',
	[FactStatus.CONFLICT]: 'En conflicto',
	[FactStatus.UNREVIEWED]: 'Sin revisar'
};

// Reutiliza los tokens de estado ya definidos en el theme (routes/layout.css).
export const FACT_STATUS_COLORS: Record<FactStatus, string> = {
	[FactStatus.VERIFIED]: 'var(--success)',
	[FactStatus.CONFLICT]: 'var(--destructive)',
	[FactStatus.UNREVIEWED]: 'var(--warning)'
};

// ─── Chart colors (identidad fija por tipo de fuente, nunca por ranking) ──────
export const SOURCE_TYPE_COLORS: Record<SourceType, string> = {
	[SourceType.PDF]: 'var(--chart-source-pdf)',
	[SourceType.API]: 'var(--chart-source-api)',
	[SourceType.EXCEL]: 'var(--chart-source-excel)',
	[SourceType.MARKDOWN]: 'var(--chart-source-markdown)',
	[SourceType.FILE]: 'var(--chart-source-file)'
};
