<script lang="ts">
	import PitchSlideShell from '../PitchSlideShell.svelte';
	import DatabaseIcon from '@lucide/svelte/icons/database';
	import NetworkIcon from '@lucide/svelte/icons/network';
	import UserIcon from '@lucide/svelte/icons/user';
	import ArrowRightIcon from '@lucide/svelte/icons/arrow-right';

	const LAYERS = [
		{
			label: 'Capa 2 — knowledge/',
			title: 'La base de conocimiento',
			description:
				'Pipeline batch: ingest → parse → extract → normalize → reconcile → validate → publish. Produce layer.json, con procedencia y confianza por hecho.',
			icon: DatabaseIcon,
			accent: 'var(--chart-source-api)'
		},
		{
			label: 'Capa 1 — expert/',
			title: 'El agente SICK',
			description:
				'get_specs, compare_products, find_products, escalate_to_human — todas llaman al agente de consulta de capa 2 como una tool más.',
			icon: NetworkIcon,
			accent: 'var(--success)'
		},
		{
			label: 'Interfaz',
			title: 'La persona',
			description: 'Recibe la respuesta con su cita, su confianza y, si aplica, su escalamiento.',
			icon: UserIcon,
			accent: 'var(--chart-source-excel)'
		}
	];
</script>

<PitchSlideShell
	kicker="Arquitectura"
	title="Dos capas, una sola regla de dependencia"
	subtitle="Capa 1 nunca importa nada de knowledge/pipeline/. Si no tiene el dato, la respuesta correcta es «no lo sé, escalo» — nunca inventar."
>
	<div class="flex flex-col items-stretch gap-3 sm:flex-row sm:items-center">
		{#each LAYERS as layer, i (layer.title)}
			<div class="flex flex-1 flex-col gap-2 rounded-2xl border bg-card p-5">
				<span class="text-xs font-medium text-muted-foreground">{layer.label}</span>
				<div class="flex items-center gap-2">
					<div
						class="flex size-8 shrink-0 items-center justify-center rounded-full"
						style="background-color: color-mix(in oklab, {layer.accent} 16%, transparent);"
					>
						<layer.icon class="size-4" style="color: {layer.accent};" />
					</div>
					<p class="font-semibold">{layer.title}</p>
				</div>
				<p class="text-sm text-muted-foreground">{layer.description}</p>
			</div>
			{#if i < LAYERS.length - 1}
				<ArrowRightIcon class="mx-auto size-5 shrink-0 rotate-90 text-muted-foreground sm:rotate-0" />
			{/if}
		{/each}
	</div>
</PitchSlideShell>
