<script lang="ts">
	import { FACT_STATUS_LABELS, FACT_STATUS_COLORS } from '$lib/config';
	import type { FactStatusBreakdown } from '$lib/types/knowledge';

	let { breakdown }: { breakdown: FactStatusBreakdown[] } = $props();

	const total = $derived(breakdown.reduce((sum, item) => sum + item.count, 0));
</script>

<div class="flex flex-col gap-4">
	<div class="flex h-3 w-full gap-0.5 overflow-hidden rounded-full bg-muted">
		{#each breakdown as item (item.status)}
			{@const pct = total > 0 ? (item.count / total) * 100 : 0}
			{#if pct > 0}
				<div
					class="h-full first:rounded-l-full last:rounded-r-full"
					style="width: {pct}%; background-color: {FACT_STATUS_COLORS[item.status]};"
					title="{FACT_STATUS_LABELS[item.status]}: {item.count.toLocaleString()}"
				></div>
			{/if}
		{/each}
	</div>
	<div class="flex flex-wrap gap-x-6 gap-y-2">
		{#each breakdown as item (item.status)}
			{@const pct = total > 0 ? Math.round((item.count / total) * 100) : 0}
			<div class="flex items-center gap-2 text-sm">
				<span
					class="size-2.5 shrink-0 rounded-xs"
					style="background-color: {FACT_STATUS_COLORS[item.status]};"
				></span>
				<span class="text-muted-foreground">{FACT_STATUS_LABELS[item.status]}</span>
				<span class="font-medium tabular-nums">{item.count.toLocaleString()}</span>
				<span class="text-xs text-muted-foreground">({pct}%)</span>
			</div>
		{/each}
	</div>
</div>
