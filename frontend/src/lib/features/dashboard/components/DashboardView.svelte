<script lang="ts">
	import { PageHeader, AsyncView, StatTile, RadialProgress } from '$lib/components/common';
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
	import ShieldCheckIcon from '@lucide/svelte/icons/shield-check';
	import CircleAlertIcon from '@lucide/svelte/icons/circle-alert';
	import ClockIcon from '@lucide/svelte/icons/clock';
	import UploadIcon from '@lucide/svelte/icons/upload';

	const store = new DashboardStore();

	$effect(() => {
		store.load();
	});
</script>

<div class="flex flex-col gap-6">
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
				<div class="flex flex-col gap-6">
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
								<p class="text-xs text-muted-foreground">Sobre hechos verificados</p>
							</Card.Content>
						</Card.Root>

						<StatTile
							title="Conflictos activos"
							value={(
								snapshot.statusBreakdown.find((s) => s.status === FactStatus.CONFLICT)?.count ?? 0
							).toLocaleString()}
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

					<section class="grid gap-4 lg:grid-cols-3">
						<Card.Root class="lg:col-span-2">
							<Card.Header>
								<Card.Title>Crecimiento de la base de conocimiento</Card.Title>
								<Card.Description>Hechos publicados por corrida del pipeline</Card.Description>
							</Card.Header>
							<Card.Content>
								<FactsTrendChart data={snapshot.factsTrend} />
							</Card.Content>
						</Card.Root>

						<Card.Root>
							<Card.Header>
								<Card.Title>Composición por estado</Card.Title>
								<Card.Description>Verificado, en conflicto y sin revisar</Card.Description>
							</Card.Header>
							<Card.Content>
								<FactsStatusBar breakdown={snapshot.statusBreakdown} />
							</Card.Content>
						</Card.Root>
					</section>

					<section class="grid gap-4 lg:grid-cols-3">
						<Card.Root>
							<Card.Header>
								<Card.Title>Fuentes ingeridas</Card.Title>
								<Card.Description>{snapshot.sourcesIngested} fuentes por tipo</Card.Description>
							</Card.Header>
							<Card.Content>
								<SourcesBarChart breakdown={snapshot.sourceBreakdown} />
							</Card.Content>
						</Card.Root>

						<Card.Root class="lg:col-span-2">
							<Card.Header>
								<Card.Title>Actividad reciente</Card.Title>
								<Card.Description>Conflictos, escalaciones y publicaciones</Card.Description>
							</Card.Header>
							<Card.Content>
								<ActivityFeed events={snapshot.recentActivity} />
							</Card.Content>
						</Card.Root>
					</section>
				</div>
			{/if}
		{/snippet}
	</AsyncView>
</div>
