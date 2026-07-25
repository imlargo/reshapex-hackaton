<script lang="ts">
	import type { ReadinessSummary } from '../types';

	let { summary }: { summary: ReadinessSummary } = $props();
</script>

<div class="flex flex-col gap-2 text-xs">
	<div class="flex flex-wrap gap-x-5 gap-y-1.5">
		<div class="flex flex-col">
			<span class="text-sm font-semibold">{summary.evidenceRetrieved.toLocaleString()}</span>
			<span class="text-muted-foreground">Evidencias recuperadas</span>
		</div>
		<div class="flex flex-col">
			<span class="text-sm font-semibold capitalize">{summary.evidenceGrade}</span>
			<span class="text-muted-foreground">Grado de evidencia</span>
		</div>
		<div class="flex flex-col">
			<span class="text-sm font-semibold capitalize">{summary.confidence}</span>
			<span class="text-muted-foreground">Confianza</span>
		</div>
		<div class="flex flex-col">
			<span class="text-sm font-semibold">{summary.status}</span>
			<span class="text-muted-foreground">Estado</span>
		</div>
	</div>
	<p class="text-muted-foreground"><span class="font-medium text-foreground">Riesgo no resuelto:</span> {summary.unresolvedRisk}</p>
	<p class="text-muted-foreground"><span class="font-medium text-foreground">Siguiente acción:</span> {summary.nextAction}</p>
</div>
