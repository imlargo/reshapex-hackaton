<script lang="ts">
	import { PageHeader, ChatBubble } from '$lib/components/common';
	import { ThinkingOrb, OrbState } from '$lib/components/common/thinking-orb';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import { IngestionStore } from '../stores/ingestion.svelte';
	import SourceIntake from './SourceIntake.svelte';
	import ReasoningTrace from './ReasoningTrace.svelte';
	import PipelineStageTracker from './PipelineStageTracker.svelte';
	import PipelineResultSummary from './PipelineResultSummary.svelte';
	import { PhaseStatus } from '$lib/types/knowledge';
	import { SOURCE_TYPE_LABELS } from '$lib/config';
	import SendIcon from '@lucide/svelte/icons/send';
	import RotateCcwIcon from '@lucide/svelte/icons/rotate-ccw';

	const store = new IngestionStore();

	const hasStarted = $derived(store.phases.some((phase) => phase.status !== PhaseStatus.PENDING));

	let bottomAnchor: HTMLDivElement | undefined = $state();

	$effect(() => {
		// Se re-ejecuta con cada evento nuevo o al llegar el resultado final.
		store.traceEvents.length;
		store.result;
		bottomAnchor?.scrollIntoView({ behavior: 'smooth', block: 'end' });
	});
</script>

<div class="flex flex-col gap-6">
	<PageHeader
		title="Crear base de conocimiento"
		description="Sube fuentes y mira al agente avanzar fase por fase, en vivo."
	>
		{#snippet actions()}
			{#if hasStarted}
				<Button variant="ghost" size="sm" onclick={() => store.reset()} disabled={store.isRunning}>
					<RotateCcwIcon class="size-4" />
					Reiniciar
				</Button>
			{/if}
		{/snippet}
	</PageHeader>

	<div class="flex flex-col gap-6 lg:flex-row lg:items-start">
		<Card.Root class="lg:sticky lg:top-4 lg:w-64 lg:shrink-0">
			<Card.Header>
				<Card.Title class="text-sm">Plan del pipeline</Card.Title>
				<Card.Description>
					{store.phases.filter((p) => p.status === PhaseStatus.DONE).length} / {store.phases.length} completadas
				</Card.Description>
			</Card.Header>
			<Card.Content>
				<PipelineStageTracker phases={store.phases} />
			</Card.Content>
		</Card.Root>

		<div class="mx-auto flex w-full max-w-2xl min-w-0 flex-1 flex-col gap-5">
			<ChatBubble role="agent">
				{#snippet avatar()}
					<ThinkingOrb state={OrbState.LISTENING} size={20} />
				{/snippet}
				<p>
					Cuéntame qué fuentes quieres incorporar: archivos PDF, Excel o Markdown, o un endpoint de
					API. Cuando estés listo, envíalas y te muestro cada fase a medida que avanza.
				</p>
			</ChatBubble>

			{#if hasStarted}
				<ChatBubble role="user">
					<p class="font-medium">
						{store.sources.length} fuente{store.sources.length === 1 ? '' : 's'} enviada{store
							.sources.length === 1
							? ''
							: 's'}
					</p>
					<div class="flex flex-wrap gap-1.5">
						{#each store.sources as source (source.id)}
							<span class="rounded-full bg-primary-foreground/15 px-2 py-0.5 text-xs">
								{SOURCE_TYPE_LABELS[source.type]} · {source.name}
							</span>
						{/each}
					</div>
				</ChatBubble>

				<ReasoningTrace events={store.traceEvents} phases={store.phases} />

				{#if store.result}
					<PipelineResultSummary result={store.result} onReset={() => store.reset()} />
				{/if}
			{/if}

			<div bind:this={bottomAnchor}></div>

			{#if !hasStarted}
				<Card.Root class="sticky bottom-4 gap-3 py-3 shadow-lg">
					<Card.Content class="flex flex-col gap-4">
						<SourceIntake {store} />
						<div class="flex items-center justify-between border-t pt-3">
							<p class="text-xs text-muted-foreground">
								{store.sources.length}
								{store.sources.length === 1 ? 'fuente lista' : 'fuentes listas'}
							</p>
							<Button size="sm" onclick={() => store.run()} disabled={!store.canRun}>
								<SendIcon class="size-4" />
								Procesar
							</Button>
						</div>
					</Card.Content>
				</Card.Root>
			{/if}
		</div>
	</div>
</div>
