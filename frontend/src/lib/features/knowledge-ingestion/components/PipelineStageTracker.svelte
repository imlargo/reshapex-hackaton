<script lang="ts">
	import { PIPELINE_PHASE_LABELS } from '$lib/config';
	import { PhaseStatus } from '$lib/types/knowledge';
	import type { PipelinePhaseState } from '$lib/types/knowledge';
	import CircleCheckIcon from '@lucide/svelte/icons/circle-check';
	import LoaderCircleIcon from '@lucide/svelte/icons/loader-circle';

	let { phases }: { phases: PipelinePhaseState[] } = $props();
</script>

<ol class="flex flex-col">
	{#each phases as phase, i (phase.phase)}
		<li class="flex gap-3">
			<div class="flex flex-col items-center">
				<div
					class="flex size-5 shrink-0 items-center justify-center rounded-full"
					style={phase.status === PhaseStatus.PENDING
						? 'background-color: var(--muted);'
						: 'background-color: color-mix(in oklab, var(--chart-source-api) 16%, transparent);'}
				>
					{#if phase.status === PhaseStatus.DONE}
						<CircleCheckIcon class="size-3.5" style="color: var(--success);" />
					{:else if phase.status === PhaseStatus.RUNNING}
						<LoaderCircleIcon class="size-3 animate-spin" style="color: var(--chart-source-api);" />
					{:else}
						<span class="size-1.5 rounded-full bg-muted-foreground"></span>
					{/if}
				</div>
				{#if i < phases.length - 1}
					<div
						class="w-px flex-1"
						style="background-color: {phase.status === PhaseStatus.DONE
							? 'var(--success)'
							: 'var(--border)'}; min-height: 1.25rem;"
					></div>
				{/if}
			</div>
			<div class="pb-4 text-sm">
				<span
					class:text-muted-foreground={phase.status === PhaseStatus.PENDING}
					class:font-medium={phase.status === PhaseStatus.RUNNING}
				>
					{PIPELINE_PHASE_LABELS[phase.phase]}
				</span>
			</div>
		</li>
	{/each}
</ol>
