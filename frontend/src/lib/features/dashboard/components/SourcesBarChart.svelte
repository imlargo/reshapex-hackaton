<script lang="ts">
	import { SOURCE_TYPE_LABELS, SOURCE_TYPE_COLORS } from '$lib/config';
	import type { SourceBreakdownItem } from '$lib/types/knowledge';

	let { breakdown }: { breakdown: SourceBreakdownItem[] } = $props();

	const sorted = $derived([...breakdown].sort((a, b) => b.count - a.count));
	const max = $derived(Math.max(1, ...breakdown.map((item) => item.count)));
</script>

<div class="flex flex-col gap-3">
	{#each sorted as item (item.type)}
		{@const pct = (item.count / max) * 100}
		<div class="grid grid-cols-[5rem_1fr_2rem] items-center gap-3 text-sm">
			<span class="truncate text-muted-foreground">{SOURCE_TYPE_LABELS[item.type]}</span>
			<div class="h-2.5 w-full overflow-hidden rounded-full bg-muted">
				<div
					class="h-full rounded-full"
					style="width: {pct}%; background-color: {SOURCE_TYPE_COLORS[item.type]};"
				></div>
			</div>
			<span class="text-right font-medium tabular-nums">{item.count}</span>
		</div>
	{/each}
</div>
