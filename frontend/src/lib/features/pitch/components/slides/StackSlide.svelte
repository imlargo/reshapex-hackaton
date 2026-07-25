<script lang="ts">
	import PitchSlideShell from '../PitchSlideShell.svelte';
	import { Badge } from '$lib/components/ui/badge/index.js';

	const STACK_GROUPS = [
		{
			label: 'Capa 1 y 2 — agentes',
			items: ['Python 3.12', 'uv', 'FastAPI', 'pydantic-ai']
		},
		{
			label: 'Interfaz',
			items: ['SvelteKit 2', 'Svelte 5 (Runes)', 'TailwindCSS v4', 'shadcn-svelte']
		},
		{
			label: 'Modelo',
			items: ['Configurable vía MODEL=proveedor:modelo']
		}
	];
</script>

<PitchSlideShell
	kicker="Stack"
	title="Construido para iterar rápido, no para presumir"
	subtitle="Todo corre en local sobre Node y uv — sin desplegar nada durante el sprint."
>
	<div class="flex flex-col gap-5">
		{#each STACK_GROUPS as group (group.label)}
			<div class="flex flex-col gap-2 sm:flex-row sm:items-center sm:gap-4">
				<span class="w-48 shrink-0 text-sm font-medium text-muted-foreground">{group.label}</span>
				<div class="flex flex-wrap gap-2">
					{#each group.items as item (item)}
						<Badge variant="secondary">{item}</Badge>
					{/each}
				</div>
			</div>
		{/each}
	</div>
</PitchSlideShell>
