<script lang="ts">
	import type { Snippet } from 'svelte';
	import { cn } from '$lib/utils';
	import BrainIcon from '@lucide/svelte/icons/brain';
	import UserRoundIcon from '@lucide/svelte/icons/user-round';

	let {
		role,
		children,
		avatar,
		emphasis = false,
		class: className
	}: {
		role: 'agent' | 'user';
		children: Snippet;
		avatar?: Snippet;
		emphasis?: boolean;
		class?: string;
	} = $props();
</script>

<div class={cn('flex items-start gap-3', role === 'user' && 'flex-row-reverse', className)}>
	<div
		class="flex size-8 shrink-0 items-center justify-center overflow-hidden rounded-full"
		style={role === 'agent'
			? 'background-color: color-mix(in oklab, var(--chart-source-api) 16%, transparent); color: var(--chart-source-api);'
			: undefined}
		class:bg-muted={role === 'user'}
		class:text-muted-foreground={role === 'user'}
	>
		{#if avatar}
			{@render avatar()}
		{:else if role === 'agent'}
			<BrainIcon class="size-4" />
		{:else}
			<UserRoundIcon class="size-4" />
		{/if}
	</div>
	<div
		class={cn(
			'flex max-w-[85%] flex-col gap-3 rounded-2xl px-4 py-3 text-sm',
			role === 'agent' ? 'bg-muted/60' : 'bg-primary text-primary-foreground'
		)}
		style={role === 'agent' && emphasis
			? 'background-color: color-mix(in oklab, var(--success) 8%, var(--muted));'
			: undefined}
	>
		{@render children()}
	</div>
</div>
