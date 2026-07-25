<script lang="ts">
	import type { IndexStatsData } from '../types';

	let { stats }: { stats: IndexStatsData } = $props();

	const items = $derived(
		[
			{ label: 'Unidades indexadas', value: stats.unitsIndexed.toLocaleString() },
			stats.dimensions > 0 ? { label: 'Dimensiones', value: stats.dimensions.toLocaleString() } : null,
			stats.graphEdges > 0 ? { label: 'Aristas de grafo', value: stats.graphEdges.toLocaleString() } : null
		].filter((item) => item !== null)
	);
</script>

<div class="flex flex-wrap gap-4">
	{#each items as item (item.label)}
		<div class="flex flex-col">
			<span class="text-lg font-semibold tabular-nums">{item.value}</span>
			<span class="text-xs text-muted-foreground">{item.label}</span>
		</div>
	{/each}
</div>
