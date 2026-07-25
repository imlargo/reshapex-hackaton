<script lang="ts">
	import PitchSlideShell from '../PitchSlideShell.svelte';
	import DatabaseIcon from '@lucide/svelte/icons/database';
	import GitCompareIcon from '@lucide/svelte/icons/git-compare';
	import TargetIcon from '@lucide/svelte/icons/target';
	import ShieldCheckIcon from '@lucide/svelte/icons/shield-check';

	const CAPABILITIES = [
		{
			icon: DatabaseIcon,
			title: 'Specs y precio, con cita verificable',
			description: 'Cada dato factual sale de una tool, nunca de la memoria del modelo.'
		},
		{
			icon: GitCompareIcon,
			title: 'Compara productos similares',
			description: 'Explica en qué se diferencia un type code de otro, con evidencia de por medio.'
		},
		{
			icon: TargetIcon,
			title: 'Recomienda dado un contexto',
			description:
				'Sugiere qué producto usar según la aplicación y sus restricciones — y muestra lo descartado y por qué.'
		},
		{
			icon: ShieldCheckIcon,
			title: 'Audita seguridad sin que se lo pidan',
			description:
				'Dada una celda instalada, detecta PL/SIL insuficiente, montajes fuera de ISO 13855 y vida útil vencida.'
		}
	];
</script>

<PitchSlideShell
	kicker="La solución"
	title="Un ingeniero de aplicaciones que nunca improvisa"
	subtitle="Responde las preguntas del reto — y además revisa lo que nadie preguntó."
>
	<div class="grid gap-4 sm:grid-cols-2">
		{#each CAPABILITIES as capability (capability.title)}
			<div class="flex items-start gap-4 rounded-2xl border bg-card p-5">
				<div
					class="flex size-9 shrink-0 items-center justify-center rounded-full"
					style="background-color: color-mix(in oklab, var(--chart-source-api) 16%, transparent);"
				>
					<capability.icon class="size-5" style="color: var(--chart-source-api);" />
				</div>
				<div class="flex flex-col gap-1">
					<p class="font-semibold">{capability.title}</p>
					<p class="text-sm text-muted-foreground">{capability.description}</p>
				</div>
			</div>
		{/each}
	</div>
</PitchSlideShell>
