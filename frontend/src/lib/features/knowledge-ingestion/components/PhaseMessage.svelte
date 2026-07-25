<script lang="ts">
	import { ChatBubble } from '$lib/components/common';
	import { ThinkingOrb, OrbState } from '$lib/components/common/thinking-orb';
	import { Progress } from '$lib/components/ui/progress/index.js';
	import { PIPELINE_PHASE_LABELS, PIPELINE_PHASE_DESCRIPTIONS } from '$lib/config';
	import { PhaseStatus, PipelinePhase } from '$lib/types/knowledge';
	import type { PipelinePhaseState } from '$lib/types/knowledge';
	import CircleCheckIcon from '@lucide/svelte/icons/circle-check';
	import CircleAlertIcon from '@lucide/svelte/icons/circle-alert';

	let { phase, isLast }: { phase: PipelinePhaseState; isLast: boolean } = $props();

	// Cada fase "piensa" de una forma distinta — mapeo puramente visual, vive
	// acá y no en config/domain porque no es un concepto de negocio.
	const PHASE_ORB_STATE: Record<PipelinePhase, OrbState> = {
		[PipelinePhase.INVENTORY]: OrbState.SEARCHING,
		[PipelinePhase.EXTRACTION]: OrbState.SOLVING,
		[PipelinePhase.NORMALIZATION]: OrbState.COMPOSING,
		[PipelinePhase.ENTITY_RELATIONS]: OrbState.SOLVING,
		[PipelinePhase.RAG_STRATEGY]: OrbState.SHAPING,
		[PipelinePhase.INDEXING]: OrbState.COMPOSING,
		[PipelinePhase.VALIDATION]: OrbState.SOLVING
	};
</script>

<ChatBubble role="agent" emphasis={isLast && phase.status === PhaseStatus.DONE}>
	{#snippet avatar()}
		{#if phase.status === PhaseStatus.DONE}
			<CircleCheckIcon class="size-4" style="color: var(--success);" />
		{:else if phase.status === PhaseStatus.ERROR}
			<CircleAlertIcon class="size-4 text-destructive" />
		{:else}
			<ThinkingOrb state={PHASE_ORB_STATE[phase.phase]} size={20} paused={phase.status !== PhaseStatus.RUNNING} />
		{/if}
	{/snippet}

	<div class="font-medium">{PIPELINE_PHASE_LABELS[phase.phase]}</div>
	<p class="text-muted-foreground">
		{phase.status === PhaseStatus.DONE ? (phase.metric ?? '') : PIPELINE_PHASE_DESCRIPTIONS[phase.phase]}
	</p>
	{#if phase.status === PhaseStatus.RUNNING}
		<Progress value={phase.progress} class="h-1.5" />
	{/if}
</ChatBubble>
