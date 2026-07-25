<script lang="ts">
	import { PageHeader, AsyncView, StatTile, RadialProgress, Iridescence } from '$lib/components/common';
	import { ThinkingOrb, OrbState } from '$lib/components/common/thinking-orb';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import { DashboardStore } from '../stores/dashboard.svelte';
	import FactsTrendChart from './FactsTrendChart.svelte';
	import FactsStatusBar from './FactsStatusBar.svelte';
	import SourcesBarChart from './SourcesBarChart.svelte';
	import ActivityFeed from './ActivityFeed.svelte';
	import { relativeTime } from '$lib/utils/date';
	import { formatPercent } from '$lib/utils/number';
	import { FactStatus } from '$lib/types/knowledge';
	import DatabaseIcon from '@lucide/svelte/icons/database';
	import CircleAlertIcon from '@lucide/svelte/icons/circle-alert';
	import ClockIcon from '@lucide/svelte/icons/clock';
	import UploadIcon from '@lucide/svelte/icons/upload';
	import { fade } from 'svelte/transition';

	const store = new DashboardStore();

	$effect(() => {
		store.load();
	});

	function conflictInsight(count: number): string {
		return count > 0
			? `${count} hecho${count === 1 ? '' : 's'} en conflicto — nunca se promedian, quedan escalados a revisión.`
			: 'Sin conflictos activos entre fuentes.';
	}

	function confidenceInsight(avgConfidence: number, conflicts: number): string {
		if (conflicts > 0) return 'Baja por los hechos en conflicto que todavía no se resolvieron.';
		return avgConfidence >= 0.85 ? 'Sobre hechos verificados, sin discrepancias pendientes.' : 'Sube a medida que se resuelven las revisiones pendientes.';
	}
</script>

<div class="relative flex flex-col gap-6">
	<div class="pointer-events-none absolute inset-0 -z-10 opacity-20 grayscale">
		<Iridescence color={[1, 1, 1]} amplitude={0.15} speed={0.7} />
	</div>

	<div class="flex items-start gap-4">
		<ThinkingOrb state={OrbState.WORKING} size={64} class="mt-1 hidden sm:block" />
		<PageHeader
			class="flex-1"
			title="Estado de la base de conocimiento"
			description="El estado actual del cerebro: qué sabe, qué tan seguro está y qué necesita revisión humana."
		>
			{#snippet actions()}
				<Button href="/knowledge/ingest" size="sm">
					<UploadIcon class="size-4" />
					Alimentar conocimiento
				</Button>
			{/snippet}
		</PageHeader>
	</div>

	<AsyncView viewState={store.view}>
		{#snippet children()}
			{#if store.snapshot}
				{@const snapshot = store.snapshot}
				{@const conflictCount =
					snapshot.statusBreakdown.find((s) => s.status === FactStatus.CONFLICT)?.count ?? 0}
				<div in:fade={{ duration: 220 }} class="flex flex-col gap-6">
					<section class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
						<StatTile
							title="Hechos totales"
							value={snapshot.totalFacts.toLocaleString()}
							accent="var(--chart-source-pdf)"
						>
							{#snippet icon({ props })}
								<DatabaseIcon {...props} />
							{/snippet}
						</StatTile>

						<Card.Root>
							<Card.Header class="flex flex-row items-center justify-between pb-2">
								<Card.Title class="text-sm font-medium text-muted-foreground"
									>Confianza promedio</Card.Title
								>
							</Card.Header>
							<Card.Content class="flex items-center gap-4">
								<RadialProgress
									value={snapshot.avgConfidence}
									label={formatPercent(snapshot.avgConfidence)}
									color="var(--success)"
								/>
								<p class="text-xs text-muted-foreground">
									{confidenceInsight(snapshot.avgConfidence, conflictCount)}
								</p>
							</Card.Content>
						</Card.Root>

						<StatTile
							title="Conflictos activos"
							value={conflictCount.toLocaleString()}
							description="Nunca se resuelven solos"
							accent="var(--destructive)"
						>
							{#snippet icon({ props })}
								<CircleAlertIcon {...props} />
							{/snippet}
						</StatTile>
						<StatTile
							title="Escalaciones pendientes"
							value={snapshot.escalationsPending.toLocaleString()}
							description={snapshot.lastRunAt
								? `Última corrida ${relativeTime(snapshot.lastRunAt)}`
								: undefined}
							accent="var(--warning)"
						>
							{#snippet icon({ props })}
								<ClockIcon {...props} />
							{/snippet}
						</StatTile>
					</section>

					<div class="overflow-hidden rounded-2xl border bg-card">
						<div class="grid divide-y lg:grid-cols-3 lg:divide-x lg:divide-y-0">
							<div class="flex flex-col gap-3 p-5 lg:col-span-2">
								<div>
									<p class="font-medium">Crecimiento de la base de conocimiento</p>
									<p class="text-xs text-muted-foreground">Hechos publicados por corrida del pipeline</p>
								</div>
								<FactsTrendChart data={snapshot.factsTrend} />
							</div>
							<div class="flex flex-col gap-3 p-5">
								<div>
									<p class="font-medium">Composición por estado</p>
									<p class="text-xs text-muted-foreground">Verificado, en conflicto y sin revisar</p>
								</div>
								<FactsStatusBar breakdown={snapshot.statusBreakdown} />
								<p class="mt-auto border-t pt-2 text-xs text-muted-foreground">
									{conflictInsight(conflictCount)}
								</p>
							</div>
						</div>
					</div>

					<div class="overflow-hidden rounded-2xl border bg-card">
						<div class="grid divide-y lg:grid-cols-3 lg:divide-x lg:divide-y-0">
							<div class="flex flex-col gap-3 p-5">
								<div>
									<p class="font-medium">Fuentes ingeridas</p>
									<p class="text-xs text-muted-foreground">{snapshot.sourcesIngested} fuentes por tipo</p>
								</div>
								<SourcesBarChart breakdown={snapshot.sourceBreakdown} />
							</div>
							<div class="flex flex-col gap-3 p-5 lg:col-span-2">
								<div>
									<p class="font-medium">Actividad reciente</p>
									<p class="text-xs text-muted-foreground">Conflictos, escalaciones y publicaciones</p>
								</div>
								<ActivityFeed events={snapshot.recentActivity} />
							</div>
						</div>
					</div>
				</div>
			{/if}
		{/snippet}
	</AsyncView>
</div>
