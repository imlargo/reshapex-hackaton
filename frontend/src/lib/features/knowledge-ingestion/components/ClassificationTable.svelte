<script lang="ts">
	import type { ClassificationRow } from '../types';

	let { rows }: { rows: ClassificationRow[] } = $props();
</script>

<div class="flex flex-col gap-1.5">
	{#each rows as row (row.source)}
		<div class="grid grid-cols-[1fr_auto] items-center gap-x-3 gap-y-0.5 text-xs">
			<span class="truncate font-medium">{row.source}</span>
			<span class="rounded-full bg-muted px-2 py-0.5 text-muted-foreground">{row.authority}</span>
			<span class="col-span-2 text-muted-foreground">{row.documentClass} · {row.language}</span>
		</div>
	{/each}
</div>
