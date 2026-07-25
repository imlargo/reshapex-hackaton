<script lang="ts">
	import PitchSlideShell from '../PitchSlideShell.svelte';
	import { StatTile } from '$lib/components/common';
	import { Button } from '$lib/components/ui/button/index.js';
	import WorkflowIcon from '@lucide/svelte/icons/workflow';
	import ShieldCheckIcon from '@lucide/svelte/icons/shield-check';
	import DatabaseIcon from '@lucide/svelte/icons/database';
	import MonitorPlayIcon from '@lucide/svelte/icons/monitor-play';
	import ArrowRightIcon from '@lucide/svelte/icons/arrow-right';
</script>

<PitchSlideShell
	kicker="En vivo"
	title="No es un mockup — corre en esta plataforma"
	subtitle="Sube una fuente real y mira cada fase del pipeline avanzar, desde el documento crudo hasta el hecho verificado."
>
	<div class="flex flex-col gap-6">
		<div class="grid gap-4 sm:grid-cols-3">
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
				value="5"
				description="PDF, Excel, Markdown, archivo o API"
				accent="var(--chart-source-pdf)"
			>
				{#snippet icon({ props })}
					<DatabaseIcon {...props} />
				{/snippet}
			</StatTile>
		</div>

		<div class="flex flex-wrap items-center gap-3 rounded-2xl border bg-muted/30 p-5">
			<MonitorPlayIcon class="size-5 text-muted-foreground" />
			<p class="flex-1 text-sm text-muted-foreground">
				Demo en vivo: ingesta de una fuente real y consulta al agente sobre un producto SICK.
			</p>
			<Button href="/knowledge/ingest" size="sm">
				Probar el pipeline
				<ArrowRightIcon class="size-4" />
			</Button>
		</div>
	</div>
</PitchSlideShell>
