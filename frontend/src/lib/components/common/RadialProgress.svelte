<script lang="ts">
	let {
		value,
		size = 56,
		strokeWidth = 6,
		color = 'var(--success)',
		label
	}: {
		/** 0–1 */
		value: number;
		size?: number;
		strokeWidth?: number;
		color?: string;
		label?: string;
	} = $props();

	const radius = $derived((size - strokeWidth) / 2);
	const circumference = $derived(2 * Math.PI * radius);
	const clamped = $derived(Math.min(1, Math.max(0, value)));
	const offset = $derived(circumference * (1 - clamped));
</script>

<div
	class="relative inline-flex shrink-0 items-center justify-center"
	style="width: {size}px; height: {size}px;"
>
	<svg width={size} height={size} class="-rotate-90">
		<circle
			cx={size / 2}
			cy={size / 2}
			r={radius}
			fill="none"
			stroke="var(--border)"
			stroke-width={strokeWidth}
		/>
		<circle
			cx={size / 2}
			cy={size / 2}
			r={radius}
			fill="none"
			stroke={color}
			stroke-width={strokeWidth}
			stroke-linecap="round"
			stroke-dasharray={circumference}
			stroke-dashoffset={offset}
			style="transition: stroke-dashoffset 0.6s ease;"
		/>
	</svg>
	{#if label}
		<span class="absolute text-sm font-semibold tabular-nums">{label}</span>
	{/if}
</div>
