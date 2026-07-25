<script lang="ts">
	import { ChatBubble } from '$lib/components/common';
	import { Button } from '$lib/components/ui/button/index.js';
	import { formatPercent } from '$lib/utils/number';
	import type { PipelineRunResult } from '$lib/types/knowledge';
	import CircleCheckIcon from '@lucide/svelte/icons/circle-check';

	let { result, onReset }: { result: PipelineRunResult; onReset: () => void } = $props();
</script>

<ChatBubble role="agent" emphasis>
	<div class="flex items-center gap-2 font-medium">
		<CircleCheckIcon class="size-4" style="color: var(--success);" />
		<span>Base de conocimiento actualizada</span>
	</div>
	<p class="text-muted-foreground">{result.sourcesCount} fuentes procesadas en esta corrida.</p>

	<div class="grid grid-cols-2 gap-4 py-1 sm:grid-cols-4">
		<div>
			<p class="text-2xl font-bold tabular-nums">{result.factsCreated}</p>
			<p class="text-xs text-muted-foreground">Hechos publicados</p>
		</div>
		<div>
			<p class="text-2xl font-bold tabular-nums" style="color: var(--destructive);">
				{result.conflictsFound}
			</p>
			<p class="text-xs text-muted-foreground">Conflictos marcados</p>
		</div>
		<div>
			<p class="text-2xl font-bold tabular-nums" style="color: var(--warning);">
				{result.escalated}
			</p>
			<p class="text-xs text-muted-foreground">Escalados a revisión</p>
		</div>
		<div>
			<p class="text-2xl font-bold tabular-nums">{formatPercent(result.avgConfidence)}</p>
			<p class="text-xs text-muted-foreground">Confianza promedio</p>
		</div>
	</div>

	<div class="flex flex-wrap gap-2">
		<Button href="/" size="sm">Ver en el dashboard</Button>
		<Button variant="outline" size="sm" onclick={onReset}>Ejecutar otra corrida</Button>
	</div>
</ChatBubble>
