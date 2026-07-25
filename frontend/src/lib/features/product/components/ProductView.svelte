<script lang="ts">
	import { fade } from 'svelte/transition';
	import { MediaQuery } from 'svelte/reactivity';
	import { StatTile, RadialProgress } from '$lib/components/common';
	import { ThinkingOrb, OrbState } from '$lib/components/common/thinking-orb';
	import * as Card from '$lib/components/ui/card/index.js';
	import * as Accordion from '$lib/components/ui/accordion/index.js';
	import * as Tabs from '$lib/components/ui/tabs/index.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Switch } from '$lib/components/ui/switch/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
	import {
		config,
		PIPELINE_PHASE_ORDER,
		PIPELINE_PHASE_LABELS,
		PIPELINE_PHASE_DESCRIPTIONS,
		FACT_STATUS_LABELS,
		FACT_STATUS_COLORS,
		SOURCE_TYPE_LABELS,
		SOURCE_TYPE_COLORS
	} from '$lib/config';
	import { FactStatus, SourceType } from '$lib/types/knowledge';
	import WorkflowIcon from '@lucide/svelte/icons/workflow';
	import ShieldCheckIcon from '@lucide/svelte/icons/shield-check';
	import DatabaseIcon from '@lucide/svelte/icons/database';
	import CircleAlertIcon from '@lucide/svelte/icons/circle-alert';
	import ArrowRightIcon from '@lucide/svelte/icons/arrow-right';

	const FACT_STATUS_EXAMPLES: Record<FactStatus, { fact: string; note: string }> = {
		[FactStatus.VERIFIED]: {
			fact: 'Voltaje nominal: 24V DC',
			note: 'Confirmado por dos fuentes coincidentes: datasheet.pdf y catalogo.xlsx.'
		},
		[FactStatus.CONFLICT]: {
			fact: 'Peso: 1.2 kg (datasheet.pdf) vs. 1.5 kg (ficha_tecnica.pdf)',
			note: 'Ambas versiones se conservan con su procedencia. Escalado para revisión humana.'
		},
		[FactStatus.UNREVIEWED]: {
			fact: 'Rango de temperatura: -10°C a 60°C',
			note: 'Extraído de manual_v2.md. Aún sin una segunda fuente que lo confirme.'
		}
	};

	const sourceTypeCount = Object.keys(SOURCE_TYPE_LABELS).length;

	let openPhase = $state<string>(PIPELINE_PHASE_ORDER[0]);
	let activeStatus = $state<string>(FactStatus.VERIFIED);
	let grounded = $state(false);

	const reducedMotion = new MediaQuery('(prefers-reduced-motion: reduce)');

	function reveal(node: HTMLElement) {
		if (typeof IntersectionObserver === 'undefined' || reducedMotion.current) return {};
		node.classList.add('opacity-0', 'translate-y-3');
		const io = new IntersectionObserver(
			([entry]) => {
				if (entry.isIntersecting) {
					node.classList.remove('opacity-0', 'translate-y-3');
					io.unobserve(node);
				}
			},
			{ threshold: 0.15 }
		);
		io.observe(node);
		return { destroy: () => io.disconnect() };
	}
</script>

<div class="flex flex-col gap-8">
	<div class="flex flex-col gap-5">
		<div class="flex items-start gap-4">
			<ThinkingOrb state={OrbState.SHAPING} size={64} class="mt-1 hidden sm:block" />
			<div class="flex flex-1 flex-col gap-2">
				<h1 class="text-3xl font-semibold tracking-tight sm:text-4xl">{config.name}</h1>
				<p class="text-lg text-muted-foreground">
					La base de conocimiento que no inventa lo que no sabe.
				</p>
				<p class="max-w-2xl text-sm text-muted-foreground">
					{config.name} convierte PDFs, hojas de cálculo, markdown y APIs dispersas en hechos verificables
					— cada uno con su fuente, su nivel de confianza y, si hace falta, una alerta para que una persona
					lo revise.
				</p>
			</div>
		</div>

		<div class="flex flex-wrap items-center gap-2 ps-0 sm:ps-20">
			{#each Object.values(SourceType) as type (type)}
				<span
					class="inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1 text-xs text-muted-foreground"
				>
					<span class="size-1.5 rounded-full" style="background-color: {SOURCE_TYPE_COLORS[type]};"
					></span>
					{SOURCE_TYPE_LABELS[type]}
				</span>
			{/each}
		</div>

		<div class="flex flex-wrap gap-3 ps-0 sm:ps-20">
			<Button href="/knowledge/ingest">
				Probar el pipeline
				<ArrowRightIcon class="size-4" />
			</Button>
			<Button href="/" variant="outline">Ver el dashboard</Button>
		</div>
	</div>

	<section
		use:reveal
		class="grid gap-4 transition-all duration-700 ease-out sm:grid-cols-2 lg:grid-cols-4"
	>
		<StatTile
			title="Fases del pipeline"
			value="7"
			accent="var(--chart-source-api)"
			class="transition-transform duration-200 hover:-translate-y-1 hover:shadow-md"
		>
			{#snippet icon({ props })}
				<WorkflowIcon {...props} />
			{/snippet}
		</StatTile>

		<StatTile
			title="Estados por hecho"
			value="3"
			description="Verificado, en conflicto o sin revisar"
			accent="var(--success)"
			class="transition-transform duration-200 hover:-translate-y-1 hover:shadow-md"
		>
			{#snippet icon({ props })}
				<ShieldCheckIcon {...props} />
			{/snippet}
		</StatTile>

		<StatTile
			title="Fuentes soportadas"
			value={String(sourceTypeCount)}
			description="PDF, Excel, Markdown, archivo o API"
			accent="var(--chart-source-pdf)"
			class="transition-transform duration-200 hover:-translate-y-1 hover:shadow-md"
		>
			{#snippet icon({ props })}
				<DatabaseIcon {...props} />
			{/snippet}
		</StatTile>

		<StatTile
			title="Conflictos resueltos en silencio"
			value="0"
			description="Se escalan a revisión humana, nunca se inventan"
			accent="var(--destructive)"
			class="transition-transform duration-200 hover:-translate-y-1 hover:shadow-md"
		>
			{#snippet icon({ props })}
				<CircleAlertIcon {...props} />
			{/snippet}
		</StatTile>
	</section>

	<div use:reveal class="transition-all duration-700 ease-out">
		<Card.Root>
			<Card.Header>
				<Card.Title>Compara la diferencia</Card.Title>
				<Card.Description>La misma pregunta, con y sin evidencia trazable.</Card.Description>
			</Card.Header>
			<Card.Content class="flex flex-col gap-5">
				<div class="flex items-center gap-3">
					<Switch bind:checked={grounded} id="grounded-toggle" />
					<Label for="grounded-toggle">
						{grounded ? `Respondiendo con ${config.name}` : 'Respondiendo con un chatbot genérico'}
					</Label>
				</div>

				<div class="rounded-lg border bg-muted/30 p-4">
					<p class="text-xs text-muted-foreground">Pregunta de un usuario</p>
					<p class="mt-1 text-sm font-medium">
						¿Cuál es la presión máxima de operación del sensor XG-400?
					</p>
				</div>

				{#if grounded}
					<div
						class="flex items-start gap-4"
						transition:fade={{ duration: reducedMotion.current ? 0 : 180 }}
					>
						<RadialProgress value={0.94} label="94%" color="var(--success)" size={52} />
						<div class="flex flex-col gap-1 text-sm">
							<p class="text-base font-semibold">6 bar</p>
							<p class="text-muted-foreground">manual_XG400.pdf · sección 4.2</p>
							<span
								class="mt-1 inline-flex w-fit items-center gap-1.5 text-xs"
								style="color: var(--success);"
							>
								<span class="size-1.5 rounded-full" style="background-color: var(--success);"
								></span>
								Verificado · trazable a la fuente
							</span>
						</div>
					</div>
				{:else}
					<div
						class="flex flex-col gap-1.5 text-sm"
						transition:fade={{ duration: reducedMotion.current ? 0 : 180 }}
					>
						<p class="text-base font-medium text-muted-foreground">
							"La presión máxima suele estar entre 6 y 10 bar, dependiendo del modelo."
						</p>
						<span class="text-xs text-muted-foreground"
							>Sin fuente citada · confianza desconocida</span
						>
					</div>
				{/if}

				<p class="text-xs text-muted-foreground">
					Ejemplo ilustrativo del mismo flujo en ambos casos.
				</p>
			</Card.Content>
		</Card.Root>
	</div>

	<div use:reveal class="transition-all duration-700 ease-out">
		<Card.Root>
			<Card.Header>
				<Card.Title>Cómo funciona</Card.Title>
				<Card.Description>Siete fases, del documento crudo al hecho verificado.</Card.Description>
			</Card.Header>
			<Card.Content>
				<Accordion.Root type="single" bind:value={openPhase}>
					{#each PIPELINE_PHASE_ORDER as phase, i (phase)}
						<Accordion.Item value={phase}>
							<Accordion.Trigger>
								<span class="flex items-center gap-3">
									<span class="font-mono text-xs text-muted-foreground">0{i + 1}</span>
									{PIPELINE_PHASE_LABELS[phase]}
								</span>
							</Accordion.Trigger>
							<Accordion.Content>
								<p class="text-muted-foreground">{PIPELINE_PHASE_DESCRIPTIONS[phase]}</p>
							</Accordion.Content>
						</Accordion.Item>
					{/each}
				</Accordion.Root>
			</Card.Content>
		</Card.Root>
	</div>

	<div use:reveal class="transition-all duration-700 ease-out">
		<Card.Root>
			<Card.Header>
				<Card.Title>Por qué es distinto</Card.Title>
				<Card.Description>Los conflictos no se resuelven solos.</Card.Description>
			</Card.Header>
			<Card.Content class="flex flex-col gap-5">
				<p class="max-w-2xl text-sm text-muted-foreground">
					Cuando dos fuentes se contradicen, la mayoría de los sistemas promedia la diferencia o
					elige la respuesta que suena mejor. {config.name} no: marca el hecho, conserva ambas versiones
					con su procedencia, y lo escala a revisión humana en vez de fabricar un consenso donde no lo
					hay.
				</p>

				<Tabs.Root bind:value={activeStatus}>
					<Tabs.List>
						{#each Object.values(FactStatus) as status (status)}
							<Tabs.Trigger value={status}>{FACT_STATUS_LABELS[status]}</Tabs.Trigger>
						{/each}
					</Tabs.List>
					{#each Object.values(FactStatus) as status (status)}
						<Tabs.Content value={status}>
							<div
								class="rounded-lg border p-4"
								style="border-left: 3px solid {FACT_STATUS_COLORS[status]};"
							>
								<p class="text-sm font-medium">{FACT_STATUS_EXAMPLES[status].fact}</p>
								<p class="mt-1 text-sm text-muted-foreground">
									{FACT_STATUS_EXAMPLES[status].note}
								</p>
							</div>
						</Tabs.Content>
					{/each}
				</Tabs.Root>
			</Card.Content>
		</Card.Root>
	</div>

	<div
		use:reveal
		class="flex flex-col items-center gap-4 rounded-xl border bg-muted/30 p-8 text-center transition-all duration-700 ease-out"
	>
		<p class="text-lg font-medium">¿Listo para ver a {config.name} en acción?</p>
		<p class="max-w-md text-sm text-muted-foreground">
			Sube una fuente real y mira cada fase del pipeline avanzar en vivo.
		</p>
		<div class="flex flex-wrap justify-center gap-3">
			<Button href="/knowledge/ingest">
				Probar el pipeline
				<ArrowRightIcon class="size-4" />
			</Button>
			<Button href="/" variant="outline">Ver el dashboard</Button>
		</div>
	</div>

	<div class="flex flex-col items-center gap-1 py-4 text-center">
		<p class="text-sm font-medium">{config.name} — conocimiento con procedencia.</p>
		<p class="text-xs text-muted-foreground">
			Construido con LangChain y LangGraph · Prototipo para AgentSprint
		</p>
	</div>
</div>
