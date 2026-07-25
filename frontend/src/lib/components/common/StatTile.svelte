<script lang="ts">
	import * as Card from '$lib/components/ui/card/index.js';
	import type { Snippet } from 'svelte';
	import { cn } from '$lib/utils';

	let {
		title,
		value,
		description,
		icon,
		accent = 'var(--muted-foreground)',
		class: className
	}: {
		title: string;
		value: string;
		description?: string;
		icon?: Snippet<[{ props?: Record<string, unknown> }]>;
		/** CSS color used for the icon badge. Defaults to a neutral muted tone. */
		accent?: string;
		class?: string;
	} = $props();
</script>

<Card.Root class={cn(className)}>
	<Card.Header class="flex flex-row items-center justify-between pb-2">
		<Card.Title class="text-sm font-medium text-muted-foreground">{title}</Card.Title>
		{#if icon}
			<div
				class="flex size-8 shrink-0 items-center justify-center rounded-full"
				style="background-color: color-mix(in oklab, {accent} 14%, transparent); color: {accent};"
			>
				{@render icon({ props: { class: 'size-4' } })}
			</div>
		{/if}
	</Card.Header>
	<Card.Content>
		<div class="text-2xl font-bold tabular-nums">{value}</div>
		{#if description}
			<p class="text-xs text-muted-foreground">{description}</p>
		{/if}
	</Card.Content>
</Card.Root>
