<script lang="ts">
	import PitchSlideShell from '../PitchSlideShell.svelte';
	import { RadialProgress } from '$lib/components/common';
	import ScaleIcon from '@lucide/svelte/icons/scale';
</script>

<PitchSlideShell
	kicker="La regla que nunca se negocia"
	title="Un conflicto nunca se resuelve solo"
	subtitle="Cuando la ficha del fabricante y el listado del distribuidor discrepan, el sistema no elige un valor: lo marca, baja la confianza y escala a un humano."
>
	<div class="grid gap-4 sm:grid-cols-2">
		<div class="flex flex-col gap-3 rounded-2xl border bg-card p-6">
			<div class="flex items-center gap-3">
				<div
					class="flex size-9 items-center justify-center rounded-full"
					style="background-color: color-mix(in oklab, var(--destructive) 16%, transparent);"
				>
					<ScaleIcon class="size-5" style="color: var(--destructive);" />
				</div>
				<p class="font-semibold">Peso del sensor XG-400</p>
			</div>
			<div class="rounded-lg border-l-3 border-l-destructive bg-muted/30 p-4 text-sm">
				<p class="font-medium">1.2 kg (datasheet.pdf) vs. 1.5 kg (ficha_tecnica.pdf)</p>
				<p class="mt-1 text-muted-foreground">
					Ambas versiones se conservan con su procedencia. Estado: <span class="font-medium"
						>conflicto</span
					> — escalado para revisión humana.
				</p>
			</div>
			<p class="text-xs text-muted-foreground">
				Nunca se promedia, nunca se elige "el más probable".
			</p>
		</div>

		<div class="flex flex-col items-center justify-center gap-4 rounded-2xl border bg-card p-6">
			<RadialProgress value={0.75} label="75%" color="var(--warning)" size={96} />
			<div class="text-center">
				<p class="font-semibold">Umbral de confianza</p>
				<p class="text-sm text-muted-foreground">
					Toda respuesta por debajo del umbral se retiene para revisión — nunca se envía como si
					fuera segura.
				</p>
			</div>
		</div>
	</div>
</PitchSlideShell>
