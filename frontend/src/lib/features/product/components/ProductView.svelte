<script lang="ts">
	import { StatTile } from '$lib/components/common';
	import { ThinkingOrb, OrbState } from '$lib/components/common/thinking-orb';
	import * as Card from '$lib/components/ui/card/index.js';
	import {
		config,
		PIPELINE_PHASE_ORDER,
		PIPELINE_PHASE_LABELS,
		PIPELINE_PHASE_DESCRIPTIONS,
		FACT_STATUS_LABELS,
		FACT_STATUS_COLORS,
		SOURCE_TYPE_LABELS
	} from '$lib/config';
	import { FactStatus } from '$lib/types/knowledge';
	import CircleCheckIcon from '@lucide/svelte/icons/circle-check';
	import WorkflowIcon from '@lucide/svelte/icons/workflow';
	import ShieldCheckIcon from '@lucide/svelte/icons/shield-check';
	import DatabaseIcon from '@lucide/svelte/icons/database';
	import CircleAlertIcon from '@lucide/svelte/icons/circle-alert';

	const FACT_STATUS_DESCRIPTIONS: Record<FactStatus, string> = {
		[FactStatus.VERIFIED]: 'Confirmado por al menos dos fuentes coincidentes.',
		[FactStatus.CONFLICT]: 'Dos fuentes se contradicen: queda marcado y escalado.',
		[FactStatus.UNREVIEWED]: 'Extraído, pero todavía sin confirmar del todo.'
	};

	const sourceTypeCount = Object.keys(SOURCE_TYPE_LABELS).length;
</script>

<div class="flex flex-col gap-6">
	<div class="flex items-start gap-4">
		<ThinkingOrb state={OrbState.SHAPING} size={64} class="mt-1 hidden sm:block" />
		<div class="flex flex-1 flex-col gap-2">
			<h1 class="text-3xl font-semibold tracking-tight sm:text-4xl">{config.name}</h1>
			<p class="text-lg text-muted-foreground">
				La base de conocimiento que no inventa lo que no sabe.
			</p>
			<p class="max-w-2xl text-sm text-muted-foreground">
				{config.name} convierte PDFs, hojas de cálculo, markdown y APIs dispersas en hechos verificables
				— cada uno con su fuente, su nivel de confianza y, si hace falta, una alerta para que una
				persona lo revise.
			</p>
		</div>
	</div>

	<section class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
		<StatTile title="Fases del pipeline" value="7" accent="var(--chart-source-api)">
			{#snippet icon({ props })}
				<WorkflowIcon {...props} />
			{/snippet}
		</StatTile>

		<StatTile
			title="Estados por hecho"
			value="3"
			description="Verificado, en conflicto o sin revisar"
			accent="var(--success)"
		>
			{#snippet icon({ props })}
				<ShieldCheckIcon {...props} />
			{/snippet}
		</StatTile>

		<StatTile
			title="Fuentes soportadas"
			value={String(sourceTypeCount)}
			description="PDF, Excel, Markdown, archivo o API"
			accent="var(--chart-source-pdf)"
		>
			{#snippet icon({ props })}
				<DatabaseIcon {...props} />
			{/snippet}
		</StatTile>

		<StatTile
			title="Conflictos resueltos en silencio"
			value="0"
			description="Se escalan a revisión humana, nunca se inventan"
			accent="var(--destructive)"
		>
			{#snippet icon({ props })}
				<CircleAlertIcon {...props} />
			{/snippet}
		</StatTile>
	</section>

	<Card.Root>
		<Card.Header>
			<Card.Title>Cómo funciona</Card.Title>
			<Card.Description>Siete fases, del documento crudo al hecho verificado.</Card.Description>
		</Card.Header>
		<Card.Content>
			<ol class="flex flex-col">
				{#each PIPELINE_PHASE_ORDER as phase, i (phase)}
					<li class="flex gap-3">
						<div class="flex flex-col items-center">
							<div
								class="flex size-5 shrink-0 items-center justify-center rounded-full"
								style="background-color: color-mix(in oklab, var(--success) 16%, transparent);"
							>
								<CircleCheckIcon class="size-3.5" style="color: var(--success);" />
							</div>
							{#if i < PIPELINE_PHASE_ORDER.length - 1}
								<div class="w-px flex-1" style="background-color: var(--success); min-height: 1.5rem;"
								></div>
							{/if}
						</div>
						<div class="pb-5 text-sm">
							<p class="font-medium">{PIPELINE_PHASE_LABELS[phase]}</p>
							<p class="text-muted-foreground">{PIPELINE_PHASE_DESCRIPTIONS[phase]}</p>
						</div>
					</li>
				{/each}
			</ol>
		</Card.Content>
	</Card.Root>

	<Card.Root>
		<Card.Header>
			<Card.Title>Por qué es distinto</Card.Title>
			<Card.Description>Los conflictos no se resuelven solos.</Card.Description>
		</Card.Header>
		<Card.Content class="flex flex-col gap-5">
			<p class="max-w-2xl text-sm text-muted-foreground">
				Cuando dos fuentes se contradicen, la mayoría de los sistemas promedia la diferencia o
				elige la respuesta que suena mejor. {config.name} no: marca el hecho, conserva ambas
				versiones con su procedencia, y lo escala a revisión humana en vez de fabricar un consenso
				donde no lo hay.
			</p>
			<div class="grid gap-4 sm:grid-cols-3">
				{#each Object.values(FactStatus) as status (status)}
					<div class="flex items-start gap-2">
						<span
							class="mt-1.5 size-2.5 shrink-0 rounded-xs"
							style="background-color: {FACT_STATUS_COLORS[status]};"
						></span>
						<div class="text-sm">
							<p class="font-medium">{FACT_STATUS_LABELS[status]}</p>
							<p class="text-muted-foreground">{FACT_STATUS_DESCRIPTIONS[status]}</p>
						</div>
					</div>
				{/each}
			</div>
		</Card.Content>
	</Card.Root>

	<div class="flex flex-col items-center gap-1 py-4 text-center">
		<p class="text-sm font-medium">{config.name} — conocimiento con procedencia.</p>
		<p class="text-xs text-muted-foreground">
			Construido con LangChain y LangGraph · Prototipo para AgentSprint
		</p>
	</div>
</div>
