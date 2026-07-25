<script lang="ts">
	// One shared clock (performance.now) keeps every mounted orb in phase;
	// each instance runs its own rAF loop but pauses automatically while
	// offscreen (IntersectionObserver) or when the tab is hidden
	// (visibilitychange). Reduced-motion users get a static representative
	// frame that still follows the live theme.
	import { MediaQuery } from 'svelte/reactivity';
	import type { HTMLAttributes } from 'svelte/elements';
	import { MODE_DRAWS } from './engine/registry';
	import { resolvePreset } from './presets';
	import { OrbState, OrbTheme, type OrbSize } from './types';

	const LABELS: Record<OrbState, string> = {
		[OrbState.WORKING]: 'Working…',
		[OrbState.SEARCHING]: 'Searching…',
		[OrbState.SOLVING]: 'Solving…',
		[OrbState.LISTENING]: 'Listening…',
		[OrbState.COMPOSING]: 'Composing…',
		[OrbState.SHAPING]: 'Shaping…'
	};

	type Props = Omit<HTMLAttributes<HTMLCanvasElement>, 'style'> & {
		/** Which animation to show. @default OrbState.WORKING */
		state?: OrbState;
		/** Tuned size preset — 64 or 20 CSS px. @default 64 */
		size?: OrbSize;
		/** Theme mode; AUTO detects from the host project. @default OrbTheme.AUTO */
		theme?: OrbTheme;
		/** Animation speed multiplier on top of the preset's baked speed. @default 1 */
		speed?: number;
		/** Freeze the animation on the current frame. @default false */
		paused?: boolean;
		style?: string;
	};

	let {
		state: orbState = OrbState.WORKING,
		size = 64,
		theme = OrbTheme.AUTO,
		speed = 1,
		paused = false,
		style,
		'aria-label': ariaLabel,
		...rest
	}: Props = $props();

	let canvas: HTMLCanvasElement | undefined = $state();

	const reducedMotionQuery = new MediaQuery('(prefers-reduced-motion: reduce)');
	const systemDarkQuery = new MediaQuery('(prefers-color-scheme: dark)');

	function ancestorDark(el: Element | null): boolean | null {
		let node: Element | null = el;
		while (node) {
			const attr = node.getAttribute('data-theme');
			if (attr === 'dark') return true;
			if (attr === 'light') return false;
			if (node.classList.contains('dark')) return true;
			if (node.classList.contains('light')) return false;
			node = node.parentElement;
		}
		return null;
	}

	let treeDark: boolean | null = $state(null);

	const dark = $derived(
		theme === OrbTheme.DARK ? true : theme === OrbTheme.LIGHT ? false : (treeDark ?? systemDarkQuery.current)
	);

	// live app-level toggles: watch class/data-theme flips on ancestors
	$effect(() => {
		if (theme !== OrbTheme.AUTO || !canvas) return;
		treeDark = ancestorDark(canvas);
		const mo = new MutationObserver(() => {
			treeDark = ancestorDark(canvas ?? null);
		});
		mo.observe(document.documentElement, {
			attributes: true,
			attributeFilter: ['class', 'data-theme'],
			subtree: true
		});
		return () => mo.disconnect();
	});

	$effect(() => {
		const el = canvas;
		if (!el) return;
		const dpr = Math.min(2, (typeof devicePixelRatio !== 'undefined' && devicePixelRatio) || 1);
		el.width = Math.round(size * dpr);
		el.height = Math.round(size * dpr);
		const ctx = el.getContext('2d');
		if (!ctx) return;

		const { mode, speed: baseSpeed, opts } = resolvePreset(orbState, size);
		const draw = MODE_DRAWS[mode];
		const effSpeed = baseSpeed * speed;
		const isDark = dark;

		const frame = (tSec: number) => {
			ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
			ctx.clearRect(0, 0, size, size);
			draw(ctx, size, tSec, isDark, opts);
		};

		// reduced motion → one static, deterministic frame
		if (reducedMotionQuery.current) {
			frame(0.6);
			return;
		}

		let raf = 0;
		let running = false;
		const loop = () => {
			frame((performance.now() / 1000) * effSpeed);
			if (running) raf = requestAnimationFrame(loop);
		};
		const start = () => {
			if (running || paused) return;
			running = true;
			raf = requestAnimationFrame(loop);
		};
		const stop = () => {
			running = false;
			cancelAnimationFrame(raf);
		};

		// draw at least one frame even when paused/offscreen
		frame((performance.now() / 1000) * effSpeed);

		// pause offscreen + on hidden tabs — free when not visible
		let visible = true;
		const io =
			typeof IntersectionObserver !== 'undefined'
				? new IntersectionObserver(([entry]) => {
						visible = entry.isIntersecting;
						if (visible && document.visibilityState !== 'hidden') start();
						else stop();
					})
				: null;
		io?.observe(el);
		const onVis = () => {
			if (document.visibilityState === 'hidden') stop();
			else if (visible) start();
		};
		document.addEventListener('visibilitychange', onVis);
		if (!io) start();

		return () => {
			stop();
			io?.disconnect();
			document.removeEventListener('visibilitychange', onVis);
		};
	});
</script>

<canvas
	bind:this={canvas}
	role="img"
	aria-label={ariaLabel ?? LABELS[orbState]}
	style={`width:${size}px;height:${size}px;display:block;${style ?? ''}`}
	{...rest}
></canvas>
