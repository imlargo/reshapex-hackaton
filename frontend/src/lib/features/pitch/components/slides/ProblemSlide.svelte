<script lang="ts">
	import PitchSlideShell from '../PitchSlideShell.svelte';
	import ClockIcon from '@lucide/svelte/icons/clock';
	import FileWarningIcon from '@lucide/svelte/icons/file-warning';
	import SirenIcon from '@lucide/svelte/icons/siren';

	const PAIN_POINTS = [
		{
			icon: ClockIcon,
			title: 'Cada consulta cuesta minutos que no sobran',
			description:
				'Specs y precio de un type code obligan a cruzar el datasheet del fabricante contra el listado del distribuidor, a mano, cada vez.',
			accent: 'var(--chart-source-api)'
		},
		{
			icon: FileWarningIcon,
			title: 'Un chatbot genérico responde de memoria',
			description:
				'Suena seguro, pero no cita fuente. Cuando dos documentos discrepan, promedia o adivina en vez de avisar.',
			accent: 'var(--destructive)'
		},
		{
			icon: SirenIcon,
			title: 'La auditoría de seguridad es manual',
			description:
				'Nivel de PL/SIL insuficiente, distancia de montaje que no cumple ISO 13855, dispositivos que ya superaron su vida útil — nadie los busca si nadie pregunta.',
			accent: 'var(--warning)'
		}
	];
</script>

<PitchSlideShell
	kicker="El problema"
	title="Cada consulta de specs es una apuesta"
	subtitle="Los ingenieros de aplicaciones pierden tiempo verificando datos que deberían ser instantáneos — y los riesgos de seguridad se quedan sin auditar hasta que ya es tarde."
>
	<div class="grid gap-4 sm:grid-cols-3">
		{#each PAIN_POINTS as point (point.title)}
			<div class="flex flex-col gap-3 rounded-2xl border bg-card p-5">
				<div
					class="flex size-9 items-center justify-center rounded-full"
					style="background-color: color-mix(in oklab, {point.accent} 16%, transparent);"
				>
					<point.icon class="size-5" style="color: {point.accent};" />
				</div>
				<p class="font-semibold">{point.title}</p>
				<p class="text-sm text-muted-foreground">{point.description}</p>
			</div>
		{/each}
	</div>
</PitchSlideShell>
