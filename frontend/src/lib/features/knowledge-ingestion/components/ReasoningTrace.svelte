<script lang="ts">
	import { ThinkingOrb, OrbState } from '$lib/components/common/thinking-orb';
	import { Badge } from '$lib/components/ui/badge/index.js';
	import DecisionCard from './DecisionCard.svelte';
	import RelationsGraph from './RelationsGraph.svelte';
	import ConflictCard from './ConflictCard.svelte';
	import { PIPELINE_PHASE_LABELS } from '$lib/config';
	import { PhaseStatus, PipelinePhase } from '$lib/types/knowledge';
	import type { PipelinePhaseState } from '$lib/types/knowledge';
	import type { PipelineTraceEvent } from '../types';
	import ChevronDownIcon from '@lucide/svelte/icons/chevron-down';
	import ChevronRightIcon from '@lucide/svelte/icons/chevron-right';
	import { fade, slide } from 'svelte/transition';

	let {
		events,
		phases
	}: {
		events: PipelineTraceEvent[];
		phases: PipelinePhaseState[];
	} = $props();

	// Cada fase "piensa" distinto — mapeo puramente visual, no un concepto de negocio.
	const PHASE_ORB_STATE: Record<PipelinePhase, OrbState> = {
		[PipelinePhase.INVENTORY]: OrbState.SEARCHING,
		[PipelinePhase.EXTRACTION]: OrbState.SOLVING,
		[PipelinePhase.NORMALIZATION]: OrbState.COMPOSING,
		[PipelinePhase.ENTITY_RELATIONS]: OrbState.SOLVING,
		[PipelinePhase.RAG_STRATEGY]: OrbState.SHAPING,
		[PipelinePhase.INDEXING]: OrbState.COMPOSING,
		[PipelinePhase.VALIDATION]: OrbState.SOLVING
	};

	// Agrupa eventos consecutivos por fase para poder colapsarlos por separado.
	const grouped = $derived.by(() => {
		const groups: { phase: PipelinePhase; items: PipelineTraceEvent[] }[] = [];
		for (const event of events) {
			const current = groups.at(-1);
			if (current && current.phase === event.phase) current.items.push(event);
			else groups.push({ phase: event.phase, items: [event] });
		}
		return groups;
	});

	function phaseStatus(phase: PipelinePhase): PhaseStatus {
		return phases.find((p) => p.phase === phase)?.status ?? PhaseStatus.PENDING;
	}

	// undefined = sin override del usuario -> abierta mientras corre, se
	// compacta sola al terminar. Un click siempre puede volver a abrirla/cerrarla.
	let overrides = $state<Partial<Record<PipelinePhase, boolean>>>({});

	function isOpen(phase: PipelinePhase): boolean {
		return overrides[phase] ?? phaseStatus(phase) === PhaseStatus.RUNNING;
	}

	function toggle(phase: PipelinePhase) {
		overrides = { ...overrides, [phase]: !isOpen(phase) };
	}
</script>

<div class="flex flex-col gap-4">
	{#each grouped as group (group.phase)}
		<div class="flex flex-col gap-2">
			<button
				type="button"
				class="flex w-fit items-center gap-2 rounded-md py-0.5 text-left hover:opacity-80"
				onclick={() => toggle(group.phase)}
			>
				<ThinkingOrb
					state={PHASE_ORB_STATE[group.phase]}
					size={20}
					paused={phaseStatus(group.phase) !== PhaseStatus.RUNNING}
				/>
				<Badge variant="secondary">{PIPELINE_PHASE_LABELS[group.phase]}</Badge>
				<span class="text-xs text-muted-foreground">
					{group.items.length} paso{group.items.length === 1 ? '' : 's'}
				</span>
				<ChevronDownIcon
					class="size-3.5 text-muted-foreground transition-transform duration-200"
					style={isOpen(group.phase) ? '' : 'transform: rotate(-90deg);'}
				/>
			</button>

			{#if isOpen(group.phase)}
				<div transition:slide={{ duration: 200 }} class="flex flex-col gap-2 pl-7">
					{#each group.items as event (event.id)}
						<div in:fade={{ duration: 220 }}>
							{#if event.kind === 'log'}
								<div class="flex items-start gap-2 text-sm leading-relaxed">
									<ChevronRightIcon class="mt-0.5 size-3 shrink-0 text-muted-foreground" />
									<span class="text-foreground/90">{event.text}</span>
								</div>
							{:else if event.kind === 'decision'}
								<DecisionCard
									question={event.question}
									options={event.options}
									chosen={event.chosen}
									rationale={event.rationale}
								/>
							{:else if event.kind === 'relations'}
								<RelationsGraph samples={event.samples} />
							{:else if event.kind === 'conflict'}
								<ConflictCard sample={event.sample} />
							{/if}
						</div>
					{/each}
				</div>
			{/if}
		</div>
	{/each}
</div>
