<script lang="ts">
	import PitchSlideShell from '../PitchSlideShell.svelte';
	import CircleAlertIcon from '@lucide/svelte/icons/circle-alert';
	import CircleCheckBigIcon from '@lucide/svelte/icons/circle-check-big';

	const GENERIC_POINTS = [
		'Responde de memoria, sin citar fuente',
		'Ante dos fuentes que discrepan, promedia o elige la que suena mejor',
		'No audita seguridad — solo contesta lo que se le pregunta'
	];

	const SICK_POINTS = [
		'Cada dato factual sale de una tool, con cita verificable',
		'Un conflicto se marca, baja la confianza y se escala a un humano',
		'Detecta problemas de seguridad que nadie preguntó'
	];
</script>

<PitchSlideShell
	kicker="Por qué es distinto"
	title="Grounded, no memorizado"
	subtitle="La diferencia no es el tono de la respuesta — es de dónde sale cada dato."
>
	<div class="grid gap-4 sm:grid-cols-2">
		<div class="flex flex-col gap-3 rounded-2xl border bg-card p-5">
			<p class="text-sm font-medium text-muted-foreground">Chatbot genérico</p>
			<ul class="flex flex-col gap-2.5">
				{#each GENERIC_POINTS as point (point)}
					<li class="flex items-start gap-2 text-sm">
						<CircleAlertIcon class="mt-0.5 size-4 shrink-0" style="color: var(--destructive);" />
						<span class="text-muted-foreground">{point}</span>
					</li>
				{/each}
			</ul>
		</div>

		<div
			class="flex flex-col gap-3 rounded-2xl border-2 bg-card p-5"
			style="border-color: color-mix(in oklab, var(--success) 40%, transparent);"
		>
			<p class="text-sm font-medium">SICK</p>
			<ul class="flex flex-col gap-2.5">
				{#each SICK_POINTS as point (point)}
					<li class="flex items-start gap-2 text-sm">
						<CircleCheckBigIcon class="mt-0.5 size-4 shrink-0" style="color: var(--success);" />
						<span>{point}</span>
					</li>
				{/each}
			</ul>
		</div>
	</div>
</PitchSlideShell>
