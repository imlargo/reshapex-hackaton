import { ViewState } from '$lib/core/helpers/view-state.svelte';
import { PhaseStatus, SourceType } from '$lib/types/knowledge';
import type { KnowledgeSourceInput, PipelinePhaseState, PipelineRunResult } from '$lib/types/knowledge';
import type { PipelineTraceEvent } from '../types';
import { PIPELINE_PHASE_ORDER, SOURCE_FILE_EXTENSIONS } from '$lib/config';
import { formatFileSize } from '$lib/utils/number';
import { simulatePipelineRun } from '../services/ingestion';

function initialPhases(): PipelinePhaseState[] {
	return PIPELINE_PHASE_ORDER.map((phase) => ({ phase, status: PhaseStatus.PENDING, progress: 0 }));
}

function detectSourceType(fileName: string): SourceType {
	const extension = fileName.split('.').pop()?.toLowerCase() ?? '';
	return SOURCE_FILE_EXTENSIONS[extension] ?? SourceType.FILE;
}

let apiSourceIdSeq = 0;
function nextApiSourceId(): string {
	apiSourceIdSeq += 1;
	return `api-source-${apiSourceIdSeq}`;
}

export class IngestionStore {
	readonly view = new ViewState();
	fileSources: KnowledgeSourceInput[] = $state([]);
	apiSources: KnowledgeSourceInput[] = $state([]);
	phases: PipelinePhaseState[] = $state(initialPhases());
	traceEvents: PipelineTraceEvent[] = $state([]);
	result: PipelineRunResult | null = $state(null);
	// Se incrementa en reset() para forzar el remount de <FileInput>, que gestiona
	// su propia lista interna de archivos y no la sincroniza si se limpia por fuera.
	resetToken = $state(0);

	readonly sources = $derived([...this.fileSources, ...this.apiSources]);
	readonly canRun = $derived(this.sources.length > 0 && !this.view.isLoading);
	readonly isRunning = $derived(this.view.isLoading);

	// Refleja 1:1 la lista que ya gestiona <FileInput> (agregar/quitar incluido),
	// en vez de duplicar esa lógica acá.
	setFiles(files: File[]) {
		this.fileSources = files.map((file) => ({
			id: `file-${file.name}-${file.size}-${file.lastModified}`,
			name: file.name,
			type: detectSourceType(file.name),
			sizeLabel: formatFileSize(file.size),
			addedAt: new Date().toISOString()
		}));
	}

	addApiSource(url: string) {
		const trimmed = url.trim();
		if (!trimmed) return;
		this.apiSources = [
			...this.apiSources,
			{ id: nextApiSourceId(), name: trimmed, type: SourceType.API, addedAt: new Date().toISOString() }
		];
	}

	removeApiSource(id: string) {
		this.apiSources = this.apiSources.filter((source) => source.id !== id);
	}

	async run() {
		if (this.sources.length === 0) return;
		this.result = null;
		this.phases = initialPhases();
		this.traceEvents = [];

		const outcome = await this.view.run(() =>
			simulatePipelineRun(
				this.sources,
				(update) => {
					this.phases = this.phases.map((phase) =>
						phase.phase === update.phase ? { ...phase, ...update } : phase
					);
				},
				(event) => {
					this.traceEvents = [...this.traceEvents, event];
				}
			)
		);

		if (outcome) this.result = outcome;
	}

	reset() {
		this.fileSources = [];
		this.apiSources = [];
		this.phases = initialPhases();
		this.traceEvents = [];
		this.result = null;
		this.resetToken += 1;
		this.view.reset();
	}
}
