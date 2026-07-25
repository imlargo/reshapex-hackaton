<script lang="ts">
	import type { Snippet } from 'svelte';

	let {
		kicker,
		title,
		subtitle,
		children
	}: {
		kicker: string;
		title: string;
		subtitle?: string;
		children: Snippet;
	} = $props();
</script>

<div class="flex h-full flex-col gap-8 overflow-y-auto p-8 sm:p-14">
	<div class="flex flex-col gap-3">
		<span class="text-xs font-semibold tracking-[0.2em] text-muted-foreground uppercase">
			{kicker}
		</span>
		<h2 class="text-3xl font-semibold tracking-tight sm:text-5xl">{title}</h2>
		{#if subtitle}
			<p class="max-w-2xl text-base text-muted-foreground sm:text-lg">{subtitle}</p>
		{/if}
	</div>
	<div class="flex flex-1 flex-col justify-center">
		{@render children()}
	</div>
</div>
