<script lang="ts">
	import { PageHeader, ChatBubble } from '$lib/components/common';
	import { ThinkingOrb, OrbState } from '$lib/components/common/thinking-orb';
	import { Button } from '$lib/components/ui/button/index.js';
	import { IngestionStore } from '../stores/ingestion.svelte';
	import SourceIntake from './SourceIntake.svelte';
	import PhaseMessage from './PhaseMessage.svelte';
	import PipelineResultSummary from './PipelineResultSummary.svelte';
	import { PhaseStatus } from '$lib/types/knowledge';
	import { SOURCE_TYPE_LABELS } from '$lib/config';
	import SendIcon from '@lucide/svelte/icons/send';
	import RotateCcwIcon from '@lucide/svelte/icons/rotate-ccw';
	import { fade } from 'svelte/transition';

	const store = new IngestionStore();

	const hasStarted = $derived(store.phases.some((phase) => phase.status !== PhaseStatus.PENDING));
	const activePhases = $derived(store.phases.filter((phase) => phase.status !== PhaseStatus.PENDING));

	let bottomAnchor: HTMLDivElement | undefined = $state();

	$effect(() => {
		// Se re-ejecuta con cada fase nueva o al llegar el resultado final.
		activePhases.length;
		store.result;
		bottomAnchor?.scrollIntoView({ behavior: 'smooth', block: 'end' });
	});
</script>

<div class="mx-auto flex w-full max-w-3xl flex-col gap-6">
	<PageHeader
		title="Crear base de conocimiento"
		description="Sube fuentes y conversa con el pipeline mientras avanza fase por fase, en vivo."
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

	<div class="flex flex-col gap-5">
		<ChatBubble role="agent">
			{#snippet avatar()}
				<ThinkingOrb state={OrbState.LISTENING} size={20} />
			{/snippet}
			<p>
				Cuéntame qué fuentes quieres incorporar: archivos PDF, Excel o Markdown, o un endpoint de
				API. Cuando estés listo, envíalas y te muestro cada fase del pipeline a medida que avanza.
			</p>
		</ChatBubble>

		{#if !hasStarted}
			<ChatBubble role="agent">
				{#snippet avatar()}
					<ThinkingOrb state={OrbState.LISTENING} size={20} />
				{/snippet}
				<SourceIntake {store} />
				<div class="flex justify-end">
					<Button size="sm" onclick={() => store.run()} disabled={!store.canRun}>
						<SendIcon class="size-4" />
						{store.sources.length > 0
							? `Procesar ${store.sources.length} fuente${store.sources.length === 1 ? '' : 's'}`
							: 'Procesar fuentes'}
					</Button>
				</div>
			</ChatBubble>
		{:else}
			<ChatBubble role="user">
				<p class="font-medium">
					{store.sources.length} fuente{store.sources.length === 1 ? '' : 's'} enviada{store.sources
						.length === 1
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

			{#each activePhases as phase, i (phase.phase)}
				<div in:fade={{ duration: 180 }}>
					<PhaseMessage {phase} isLast={i === activePhases.length - 1 && !store.result} />
				</div>
			{/each}

			{#if store.result}
				<div in:fade={{ duration: 180 }}>
					<PipelineResultSummary result={store.result} onReset={() => store.reset()} />
				</div>
			{/if}
		{/if}

		<div bind:this={bottomAnchor}></div>
	</div>
</div>
