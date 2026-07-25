<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import { Badge } from '$lib/components/ui/badge/index.js';
	import { ValidationStatus, CheckStatus, ConfidenceLevel } from '$lib/types/knowledge';
	import type { PipelineRunResult, ValidationCheck } from '$lib/types/knowledge';
	import CircleCheckIcon from '@lucide/svelte/icons/circle-check';
	import TriangleAlertIcon from '@lucide/svelte/icons/triangle-alert';
	import CircleAlertIcon from '@lucide/svelte/icons/circle-alert';
	import QuoteIcon from '@lucide/svelte/icons/quote';
	import DatabaseIcon from '@lucide/svelte/icons/database';
	import WandSparklesIcon from '@lucide/svelte/icons/wand-sparkles';
	import NetworkIcon from '@lucide/svelte/icons/network';
	import LayersIcon from '@lucide/svelte/icons/layers';
	import { fade } from 'svelte/transition';

	let { result, onReset }: { result: PipelineRunResult; onReset: () => void } = $props();

	const VALIDATION_STATUS_LABEL: Record<ValidationStatus, string> = {
		[ValidationStatus.READY]: 'Lista',
		[ValidationStatus.CONDITIONAL]: 'Condicional',
		[ValidationStatus.NOT_READY]: 'No lista'
	};

	const VALIDATION_STATUS_COLOR: Record<ValidationStatus, string> = {
		[ValidationStatus.READY]: 'var(--success)',
		[ValidationStatus.CONDITIONAL]: 'var(--warning)',
		[ValidationStatus.NOT_READY]: 'var(--destructive)'
	};

	const CHECK_STYLE: Record<CheckStatus, { icon: typeof CircleCheckIcon; color: string }> = {
		[CheckStatus.PASS]: { icon: CircleCheckIcon, color: 'var(--success)' },
		[CheckStatus.WARNING]: { icon: TriangleAlertIcon, color: 'var(--warning)' },
		[CheckStatus.FAIL]: { icon: CircleAlertIcon, color: 'var(--destructive)' }
	};

	const CONFIDENCE_LABEL: Record<ConfidenceLevel, string> = {
		[ConfidenceLevel.LOW]: 'Confianza baja',
		[ConfidenceLevel.MEDIUM]: 'Confianza media',
		[ConfidenceLevel.HIGH]: 'Confianza alta'
	};

	function checkMeta(check: ValidationCheck) {
		return CHECK_STYLE[check.status];
	}
</script>

<div in:fade={{ duration: 250 }} class="overflow-hidden rounded-2xl border bg-card">
	<!-- Banner -->
	<div class="flex flex-wrap items-center justify-between gap-3 border-b bg-muted/40 px-5 py-4">
		<div class="flex items-center gap-3">
			<div
				class="flex size-9 items-center justify-center rounded-full"
				style="background-color: color-mix(in oklab, var(--success) 16%, transparent);"
			>
				<CircleCheckIcon class="size-5" style="color: var(--success);" />
			</div>
			<div>
				<p class="font-semibold">Base de conocimiento lista para consultas</p>
				<p class="text-xs text-muted-foreground">
					{result.sourcesCount} fuentes · {result.entitiesDetected} entidades · {result.relationshipsDetected}
					relaciones
				</p>
			</div>
		</div>
		<Badge
			variant="outline"
			style="color: {VALIDATION_STATUS_COLOR[result.validationStatus]}; border-color: {VALIDATION_STATUS_COLOR[
				result.validationStatus
			]};"
		>
			{VALIDATION_STATUS_LABEL[result.validationStatus]}
		</Badge>
	</div>

	<!-- Report sections -->
	<div class="grid divide-y sm:grid-cols-2 sm:divide-x sm:divide-y-0">
		<section class="flex flex-col gap-1.5 p-5">
			<div class="flex items-center gap-1.5 text-xs font-medium tracking-wide text-muted-foreground uppercase">
				<DatabaseIcon class="size-3.5" />
				Perfil del corpus
			</div>
			<p class="text-sm text-muted-foreground">{result.corpusProfile}</p>
		</section>

		<section class="flex flex-col gap-1.5 p-5">
			<div class="flex items-center gap-1.5 text-xs font-medium tracking-wide text-muted-foreground uppercase">
				<WandSparklesIcon class="size-3.5" />
				Plan de transformación
			</div>
			<p class="text-sm text-muted-foreground">{result.transformationPlan}</p>
		</section>

		<section class="flex flex-col gap-1.5 p-5">
			<div class="flex items-center gap-1.5 text-xs font-medium tracking-wide text-muted-foreground uppercase">
				<NetworkIcon class="size-3.5" />
				Taxonomía de relaciones
			</div>
			<div class="flex flex-wrap gap-1.5">
				{#each result.relationTypes as relation (relation)}
					<span class="rounded-full bg-background px-2 py-0.5 text-xs">{relation}</span>
				{/each}
			</div>
		</section>

		<section class="flex flex-col gap-1.5 p-5">
			<div class="flex items-center gap-1.5 text-xs font-medium tracking-wide text-muted-foreground uppercase">
				<LayersIcon class="size-3.5" />
				Almacenamiento recomendado
			</div>
			<p class="text-sm font-medium">{result.ragStrategy.name}</p>
			<p class="text-sm text-muted-foreground">{result.ragStrategy.storageTopology}</p>
		</section>
	</div>

	<!-- Quality report -->
	<div class="flex flex-col gap-2 border-t p-5">
		<p class="text-xs font-medium tracking-wide text-muted-foreground uppercase">Reporte de calidad</p>
		{#each result.validationChecks as check (check.name)}
			{@const meta = checkMeta(check)}
			<div class="flex items-start gap-2">
				<meta.icon class="mt-0.5 size-4 shrink-0" style="color: {meta.color};" />
				<div class="text-sm">
					<span class="font-medium">{check.name}:</span>
					<span class="text-muted-foreground">{check.detail}</span>
				</div>
			</div>
		{/each}
	</div>

	<!-- Sample answer -->
	<div class="flex flex-col gap-1.5 border-t bg-muted/20 p-5">
		<div class="flex items-center gap-1.5 text-xs font-medium tracking-wide text-muted-foreground uppercase">
			<QuoteIcon class="size-3.5" />
			Respuesta de ejemplo
		</div>
		<p class="text-sm font-medium">{result.sampleAnswer.question}</p>
		<p class="text-sm text-muted-foreground">{result.sampleAnswer.answer}</p>
		<div class="flex flex-wrap items-center gap-2 pt-1 text-xs text-muted-foreground">
			<span>Fuente: {result.sampleAnswer.citation}</span>
			<Badge variant="secondary">{CONFIDENCE_LABEL[result.sampleAnswer.confidence]}</Badge>
		</div>
	</div>

	<!-- Footer -->
	<div class="flex flex-wrap items-center justify-between gap-3 border-t p-5">
		<p class="text-sm text-muted-foreground">{result.nextAction}</p>
		<div class="flex flex-wrap gap-2">
			<Button href="/" size="sm">Ver en el dashboard</Button>
			<Button variant="outline" size="sm" onclick={onReset}>Ejecutar otra corrida</Button>
		</div>
	</div>
</div>
