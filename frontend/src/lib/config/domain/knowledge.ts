import { PipelinePhase, SourceType, FactStatus } from '$lib/types/knowledge';

// ─── Pipeline phases ──────────────────────────────────────────────────────────
// Flujo congelado de 9 etapas — ver backend/agentsprint/03_contracts/PRIMARY_JOURNEY.md.
// "Información suministrada" y "Base de conocimiento lista" son el intake y el
// resultado final (no fases con progreso propio); estas 7 son las intermedias.
export const PIPELINE_PHASE_ORDER: PipelinePhase[] = [
	PipelinePhase.INVENTORY,
	PipelinePhase.EXTRACTION,
	PipelinePhase.NORMALIZATION,
	PipelinePhase.ENTITY_RELATIONS,
	PipelinePhase.RAG_STRATEGY,
	PipelinePhase.INDEXING,
	PipelinePhase.VALIDATION
];

export const PIPELINE_PHASE_LABELS: Record<PipelinePhase, string> = {
	[PipelinePhase.INVENTORY]: 'Inventario y clasificación',
	[PipelinePhase.EXTRACTION]: 'Extracción especializada',
	[PipelinePhase.NORMALIZATION]: 'Normalización',
	[PipelinePhase.ENTITY_RELATIONS]: 'Entidades y relaciones',
	[PipelinePhase.RAG_STRATEGY]: 'Estrategia RAG y almacenamiento',
	[PipelinePhase.INDEXING]: 'Indexación',
	[PipelinePhase.VALIDATION]: 'Validación'
};

export const PIPELINE_PHASE_DESCRIPTIONS: Record<PipelinePhase, string> = {
	[PipelinePhase.INVENTORY]: 'Clasifica cada fuente por tipo, idioma y calidad antes de tocar el contenido.',
	[PipelinePhase.EXTRACTION]: 'Aplica el método de extracción adecuado según la clase de cada documento.',
	[PipelinePhase.NORMALIZATION]: 'Unifica formato, unidades y estructura entre fuentes.',
	[PipelinePhase.ENTITY_RELATIONS]: 'Detecta entidades y sus relaciones, con procedencia trazable a la fuente.',
	[PipelinePhase.RAG_STRATEGY]:
		'Elige la estrategia de recuperación y la topología de almacenamiento según la forma del corpus.',
	[PipelinePhase.INDEXING]: 'Construye el índice de recuperación sobre el paquete normalizado.',
	[PipelinePhase.VALIDATION]:
		'Corre chequeos de calidad — los conflictos entre fuentes nunca se resuelven solos: quedan marcados y escalables.'
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
