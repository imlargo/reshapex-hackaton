<script lang="ts">
	import * as Chart from '$lib/components/ui/chart/index.js';
	import { AreaChart } from 'layerchart';
	import type { FactsTrendPoint } from '$lib/types/knowledge';

	let { data }: { data: FactsTrendPoint[] } = $props();

	const chartConfig = {
		facts: {
			label: 'Hechos publicados',
			theme: { light: '#eb6834', dark: '#d95926' }
		}
	} satisfies Chart.ChartConfig;
</script>

<Chart.Container config={chartConfig} class="aspect-auto h-64 w-full">
	<AreaChart {data} x="label" series={[{ key: 'facts', color: 'var(--color-facts)' }]}>
		{#snippet tooltip()}
			<Chart.Tooltip labelKey="label" />
		{/snippet}
	</AreaChart>
</Chart.Container>
