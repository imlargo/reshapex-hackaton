<script lang="ts">
	import { Badge } from '$lib/components/ui/badge/index.js';
	import { ArchitectureStatus } from '../types';
	import type { ArchitectureOption } from '../types';
	import CircleCheckIcon from '@lucide/svelte/icons/circle-check';
	import LockIcon from '@lucide/svelte/icons/lock';

	let { options }: { options: ArchitectureOption[] } = $props();

	const STATUS_LABEL: Record<ArchitectureStatus, string> = {
		[ArchitectureStatus.SELECTED]: 'Seleccionado',
		[ArchitectureStatus.AVAILABLE]: 'Disponible',
		[ArchitectureStatus.BLOCKED]: 'Bloqueado'
	};

	const winner = $derived(options.find((o) => o.status === ArchitectureStatus.SELECTED));
	const rest = $derived(options.filter((o) => o.status !== ArchitectureStatus.SELECTED));
</script>

<div class="flex flex-col gap-3">
	{#if winner}
		<div
			class="flex flex-col gap-1.5 rounded-lg border p-3"
			style="border-color: var(--success); background-color: color-mix(in oklab, var(--success) 6%, var(--card));"
		>
			<div class="flex items-center justify-between gap-2">
				<div class="flex items-center gap-2">
					<CircleCheckIcon class="size-4" style="color: var(--success);" />
					<span class="font-medium">{winner.name}</span>
				</div>
				<Badge variant="outline" style="color: var(--success); border-color: var(--success);">
					{STATUS_LABEL[winner.status]}
				</Badge>
			</div>
			<p class="text-xs text-muted-foreground">{winner.algorithm}</p>
			<p class="text-xs">{winner.reason}</p>
			<p class="text-xs text-muted-foreground">Límites: {winner.limitations}</p>
		</div>
	{/if}

	<div class="flex flex-col gap-2">
		{#each rest as option (option.name)}
			<div class="flex flex-col gap-1 rounded-lg border border-dashed p-2.5 opacity-80">
				<div class="flex items-center justify-between gap-2">
					<span class="text-sm font-medium text-muted-foreground">{option.name}</span>
					<Badge variant="secondary" class="gap-1">
						{#if option.status === ArchitectureStatus.BLOCKED}
							<LockIcon class="size-3" />
						{/if}
						{STATUS_LABEL[option.status]}
					</Badge>
				</div>
				<p class="text-xs text-muted-foreground">{option.algorithm}</p>
				<p class="text-xs text-muted-foreground">{option.reason}</p>
				{#if option.gate}
					<p class="text-xs" style="color: var(--warning);">Gate: {option.gate}</p>
				{/if}
			</div>
		{/each}
	</div>
</div>
