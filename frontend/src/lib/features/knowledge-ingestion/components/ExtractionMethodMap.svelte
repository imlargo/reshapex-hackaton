<script lang="ts">
	import type { ExtractionMethodRow } from '../types';

	let { rows }: { rows: ExtractionMethodRow[] } = $props();
</script>

<div class="flex flex-col gap-2">
	{#each rows as row (row.sourceLabel)}
		<div class="flex flex-col gap-0.5 text-xs">
			<div class="flex items-center gap-2">
				<span class="rounded-full bg-muted px-2 py-0.5 font-medium text-foreground">{row.sourceLabel}</span>
				<span class="text-muted-foreground">→ {row.method}</span>
			</div>
			<p class="pl-1 text-muted-foreground">{row.rationale}</p>
		</div>
	{/each}
</div>
