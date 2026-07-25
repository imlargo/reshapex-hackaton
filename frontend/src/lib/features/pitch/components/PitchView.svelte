<script lang="ts">
	import { fly } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';
	import { MediaQuery } from 'svelte/reactivity';
	import { Button } from '$lib/components/ui/button/index.js';
	import ChevronLeftIcon from '@lucide/svelte/icons/chevron-left';
	import ChevronRightIcon from '@lucide/svelte/icons/chevron-right';
	import MaximizeIcon from '@lucide/svelte/icons/maximize';
	import MinimizeIcon from '@lucide/svelte/icons/minimize';

	import TitleSlide from './slides/TitleSlide.svelte';
	import ProblemSlide from './slides/ProblemSlide.svelte';
	import SolutionSlide from './slides/SolutionSlide.svelte';
	import RuleSlide from './slides/RuleSlide.svelte';
	import ArchitectureSlide from './slides/ArchitectureSlide.svelte';
	import DemoSlide from './slides/DemoSlide.svelte';
	import StackSlide from './slides/StackSlide.svelte';
	import DifferentiatorSlide from './slides/DifferentiatorSlide.svelte';
	import ClosingSlide from './slides/ClosingSlide.svelte';

	const SLIDES = [
		{ label: 'Portada', component: TitleSlide },
		{ label: 'El problema', component: ProblemSlide },
		{ label: 'La solución', component: SolutionSlide },
		{ label: 'La regla', component: RuleSlide },
		{ label: 'Arquitectura', component: ArchitectureSlide },
		{ label: 'En vivo', component: DemoSlide },
		{ label: 'Stack', component: StackSlide },
		{ label: 'Diferenciador', component: DifferentiatorSlide },
		{ label: 'Cierre', component: ClosingSlide }
	];

	const total = SLIDES.length;
	const FLY_DISTANCE = 24;

	let current = $state(0);
	let direction = $state(1);
	let deckEl = $state<HTMLDivElement | null>(null);
	let isFullscreen = $state(false);

	const reducedMotion = new MediaQuery('(prefers-reduced-motion: reduce)');

	function goTo(index: number) {
		const clamped = Math.max(0, Math.min(total - 1, index));
		direction = clamped >= current ? 1 : -1;
		current = clamped;
	}

	function next() {
		goTo(current + 1);
	}

	function prev() {
		goTo(current - 1);
	}

	function handleKeydown(event: KeyboardEvent) {
		switch (event.key) {
			case 'ArrowRight':
			case 'ArrowDown':
			case 'PageDown':
			case ' ':
				event.preventDefault();
				next();
				break;
			case 'ArrowLeft':
			case 'ArrowUp':
			case 'PageUp':
				event.preventDefault();
				prev();
				break;
			case 'Home':
				event.preventDefault();
				goTo(0);
				break;
			case 'End':
				event.preventDefault();
				goTo(total - 1);
				break;
		}
	}

	async function toggleFullscreen() {
		if (!deckEl) return;
		if (!document.fullscreenElement) {
			await deckEl.requestFullscreen();
		} else {
			await document.exitFullscreen();
		}
	}

	$effect(() => {
		function onFullscreenChange() {
			isFullscreen = document.fullscreenElement === deckEl;
		}
		document.addEventListener('fullscreenchange', onFullscreenChange);
		return () => document.removeEventListener('fullscreenchange', onFullscreenChange);
	});
</script>

<svelte:window onkeydown={handleKeydown} />

<div
	bind:this={deckEl}
	class="flex h-[calc(100vh-11rem)] min-h-[28rem] flex-col gap-4"
	class:bg-background={isFullscreen}
	class:p-8={isFullscreen}
>
	<div class="relative flex-1 overflow-hidden rounded-3xl border bg-card shadow-sm">
		{#key current}
			{@const CurrentSlide = SLIDES[current].component}
			<div
				class="absolute inset-0"
				in:fly={{
					x: direction * FLY_DISTANCE,
					duration: reducedMotion.current ? 0 : 260,
					easing: quintOut
				}}
			>
				<CurrentSlide />
			</div>
		{/key}
	</div>

	<div class="flex items-center gap-3">
		<Button
			variant="outline"
			size="icon"
			onclick={prev}
			disabled={current === 0}
			aria-label="Diapositiva anterior"
		>
			<ChevronLeftIcon class="size-4" />
		</Button>

		<div class="flex flex-1 flex-col gap-1.5">
			<div class="h-1 overflow-hidden rounded-full bg-muted">
				<div
					class="h-full rounded-full bg-primary transition-[width] duration-300 ease-out"
					style="width: {((current + 1) / total) * 100}%"
				></div>
			</div>
			<div class="flex items-center justify-center gap-1.5">
				{#each SLIDES as slide, i (slide.label)}
					<button
						type="button"
						onclick={() => goTo(i)}
						class="h-1.5 rounded-full transition-all {i === current
							? 'w-4 bg-primary'
							: 'w-1.5 bg-muted-foreground/30 hover:bg-muted-foreground/60'}"
						aria-label={`Ir a la diapositiva ${i + 1}: ${slide.label}`}
					></button>
				{/each}
			</div>
		</div>

		<Button
			variant="outline"
			size="icon"
			onclick={next}
			disabled={current === total - 1}
			aria-label="Siguiente diapositiva"
		>
			<ChevronRightIcon class="size-4" />
		</Button>

		<Button
			variant="ghost"
			size="icon"
			onclick={toggleFullscreen}
			aria-label={isFullscreen ? 'Salir de pantalla completa' : 'Pantalla completa'}
		>
			{#if isFullscreen}
				<MinimizeIcon class="size-4" />
			{:else}
				<MaximizeIcon class="size-4" />
			{/if}
		</Button>

		<span class="w-14 shrink-0 text-right text-xs font-medium text-muted-foreground tabular-nums">
			{current + 1} / {total}
		</span>
	</div>
</div>
