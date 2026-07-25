<script lang="ts">
	import type { EntityRelationSample } from '../types';

	let { samples }: { samples: EntityRelationSample[] } = $props();

	function edgeKey(sample: EntityRelationSample): string {
		return `${sample.subject}::${sample.predicate}::${sample.object}`;
	}

	function truncate(name: string): string {
		return name.length > 9 ? `${name.slice(0, 8)}…` : name;
	}

	const entities = $derived.by(() => {
		const set = new Set<string>();
		for (const sample of samples) {
			set.add(sample.subject);
			set.add(sample.object);
		}
		return [...set];
	});

	const positions = $derived.by(() => {
		const map = new Map<string, { x: number; y: number }>();
		const total = entities.length;
		entities.forEach((name, i) => {
			const angle = (i * (2 * Math.PI)) / total - Math.PI / 2;
			map.set(name, { x: 130 + 85 * Math.cos(angle), y: 85 + 60 * Math.sin(angle) });
		});
		return map;
	});
</script>

<div class="flex flex-col gap-3 rounded-lg border bg-card/60 p-3 sm:flex-row sm:items-center">
	<svg viewBox="0 0 260 170" class="h-36 w-full shrink-0 sm:w-52">
		{#each samples as sample (edgeKey(sample))}
			{@const from = positions.get(sample.subject)}
			{@const to = positions.get(sample.object)}
			{#if from && to}
				<line x1={from.x} y1={from.y} x2={to.x} y2={to.y} stroke="var(--border)" stroke-width="1.5" />
			{/if}
		{/each}
		{#each entities as name (name)}
			{@const pos = positions.get(name)}
			{#if pos}
				<circle
					cx={pos.x}
					cy={pos.y}
					r="20"
					fill="var(--card)"
					stroke="var(--chart-source-api)"
					stroke-width="1.5"
				/>
				<text x={pos.x} y={pos.y + 3} text-anchor="middle" font-size="7" fill="var(--foreground)"
					>{truncate(name)}</text
				>
			{/if}
		{/each}
	</svg>
	<div class="flex flex-1 flex-col gap-1.5 text-xs">
		{#each samples as sample (edgeKey(sample))}
			<div class="text-muted-foreground">
				<span class="font-medium text-foreground">{sample.subject}</span>
				<span class="mx-1 rounded-full bg-muted px-1.5 py-0.5">{sample.predicate}</span>
				<span class="font-medium text-foreground">{sample.object}</span>
			</div>
		{/each}
	</div>
</div>
