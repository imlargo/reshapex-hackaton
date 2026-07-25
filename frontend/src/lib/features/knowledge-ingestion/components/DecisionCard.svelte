<script lang="ts">
	import type { DecisionOption } from '../types';
	import CircleCheckIcon from '@lucide/svelte/icons/circle-check';

	let {
		question,
		options,
		chosen,
		rationale
	}: {
		question: string;
		options: DecisionOption[];
		chosen: string;
		rationale: string;
	} = $props();
</script>

<div class="flex flex-col gap-2.5 rounded-lg border bg-card/60 p-3">
	<p class="text-sm font-medium">{question}</p>
	<div class="flex flex-col gap-2">
		{#each options as option (option.name)}
			{@const isChosen = option.name === chosen}
			<div class="flex flex-col gap-0.5">
				<div class="flex items-center gap-2 text-sm">
					<span class="min-w-0 flex-1 truncate" class:font-medium={isChosen}>{option.name}</span>
					<div class="h-2 w-24 shrink-0 overflow-hidden rounded-full bg-muted">
						<div
							class="h-full rounded-full"
							style="width: {Math.round(option.score * 100)}%; background-color: {isChosen
								? 'var(--success)'
								: 'var(--muted-foreground)'};"
						></div>
					</div>
					<span class="w-9 shrink-0 text-right text-xs text-muted-foreground tabular-nums">
						{Math.round(option.score * 100)}%
					</span>
					{#if isChosen}
						<CircleCheckIcon class="size-4 shrink-0" style="color: var(--success);" />
					{:else}
						<span class="size-4 shrink-0"></span>
					{/if}
				</div>
				<p class="pl-0 text-xs text-muted-foreground">{option.summary}</p>
			</div>
		{/each}
	</div>
	<p class="border-t pt-2 text-xs text-muted-foreground">
		<span class="font-medium text-foreground">Por qué:</span>
		{rationale}
	</p>
</div>
