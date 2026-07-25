import { ViewState } from '$lib/core/helpers/view-state.svelte';
import type { KnowledgeStats } from '$lib/types/knowledge';
import { getKnowledgeSnapshot } from '../services/dashboard';

export class DashboardStore {
	readonly view = new ViewState();
	snapshot: KnowledgeStats | null = $state(null);

	constructor() {
		// Se carga automáticamente al montar la vista (ver DashboardView), así que
		// arranca en loading en vez de idle para evitar un parpadeo en blanco.
		this.view.setLoading();
	}

	async load() {
		const result = await this.view.run(() => getKnowledgeSnapshot());
		if (result) this.snapshot = result;
	}
}
