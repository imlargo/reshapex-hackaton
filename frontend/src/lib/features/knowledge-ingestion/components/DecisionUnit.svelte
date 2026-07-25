<script lang="ts">
	import type { PipelineDecisionEvent } from '../types';
	import ClassificationTable from './ClassificationTable.svelte';
	import ExtractionMethodMap from './ExtractionMethodMap.svelte';
	import NormalizationDiff from './NormalizationDiff.svelte';
	import RelationsGraph from './RelationsGraph.svelte';
	import ArchitectureComparison from './ArchitectureComparison.svelte';
	import IndexStatsView from './IndexStatsView.svelte';
	import ConflictCard from './ConflictCard.svelte';
	import ReadinessSummaryView from './ReadinessSummaryView.svelte';

	let { event }: { event: PipelineDecisionEvent } = $props();
</script>

<div class="flex flex-col gap-3 rounded-lg border bg-card/60 p-3.5">
	<div class="flex flex-col gap-1">
		<p class="text-[10px] font-medium tracking-wide text-muted-foreground uppercase">Entrada</p>
		<ul class="list-inside list-disc text-xs text-muted-foreground">
			{#each event.inputs as input (input)}
				<li>{input}</li>
			{/each}
		</ul>
	</div>

	<div class="flex flex-col gap-0.5">
		<p class="text-[10px] font-medium tracking-wide text-muted-foreground uppercase">Pregunta</p>
		<p class="text-sm">{event.question}</p>
	</div>

	<div class="flex flex-col gap-0.5">
		<p class="text-[10px] font-medium tracking-wide text-muted-foreground uppercase">Decisión</p>
		<p class="text-sm font-medium">{event.decision}</p>
	</div>

	<div class="flex flex-col gap-0.5">
		<p class="text-[10px] font-medium tracking-wide text-muted-foreground uppercase">Criterio</p>
		<p class="text-xs text-muted-foreground">{event.criteria}</p>
	</div>

	<div class="flex flex-col gap-1.5 border-t pt-2.5">
		<p class="text-[10px] font-medium tracking-wide text-muted-foreground uppercase">Artefacto</p>
		{#if event.artifact.kind === 'text'}
			<p class="text-sm text-muted-foreground">{event.artifact.content}</p>
		{:else if event.artifact.kind === 'classification'}
			<ClassificationTable rows={event.artifact.rows} />
		{:else if event.artifact.kind === 'extraction-methods'}
			<ExtractionMethodMap rows={event.artifact.rows} />
		{:else if event.artifact.kind === 'normalization'}
			<NormalizationDiff examples={event.artifact.examples} />
		{:else if event.artifact.kind === 'relations'}
			<RelationsGraph samples={event.artifact.samples} />
		{:else if event.artifact.kind === 'architecture'}
			<ArchitectureComparison options={event.artifact.options} />
		{:else if event.artifact.kind === 'index-stats'}
			<IndexStatsView stats={event.artifact.stats} />
		{:else if event.artifact.kind === 'conflict'}
			<ConflictCard sample={event.artifact.sample} />
		{:else if event.artifact.kind === 'readiness'}
			<ReadinessSummaryView summary={event.artifact.summary} />
		{/if}
	</div>
</div>
