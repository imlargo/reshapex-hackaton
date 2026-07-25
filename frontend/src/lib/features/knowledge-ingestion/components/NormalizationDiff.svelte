<script lang="ts">
	import type { NormalizationExample } from '../types';
	import ArrowRightIcon from '@lucide/svelte/icons/arrow-right';

	let { examples }: { examples: NormalizationExample[] } = $props();
</script>

<div class="flex flex-col gap-1.5">
	{#each examples as example (example.field)}
		<div class="flex items-center gap-2 text-xs">
			<span class="w-32 shrink-0 truncate text-muted-foreground">{example.field}</span>
			<span class="text-muted-foreground line-through">{example.before}</span>
			<ArrowRightIcon class="size-3 shrink-0 text-muted-foreground" />
			<span class="font-medium">{example.after}</span>
		</div>
	{/each}
</div>
