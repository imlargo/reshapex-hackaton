<script lang="ts">
	// Svelte port of the React Bits "Iridescence" background (ogl-based shader).
	// Follows the same lifecycle pattern as ThinkingOrb: pause offscreen/hidden,
	// freeze on a static frame for prefers-reduced-motion.
	import { Renderer, Program, Mesh, Color, Triangle } from 'ogl';
	import type { HTMLAttributes } from 'svelte/elements';
	import { MediaQuery } from 'svelte/reactivity';
	import { cn } from '$lib/utils';

	const vertexShader = `
		attribute vec2 uv;
		attribute vec2 position;
		varying vec2 vUv;
		void main() {
			vUv = uv;
			gl_Position = vec4(position, 0, 1);
		}
	`;

	const fragmentShader = `
		precision highp float;
		uniform float uTime;
		uniform vec3 uColor;
		uniform vec3 uResolution;
		uniform vec2 uMouse;
		uniform float uAmplitude;
		uniform float uSpeed;
		varying vec2 vUv;
		void main() {
			float mr = min(uResolution.x, uResolution.y);
			vec2 uv = (vUv.xy * 2.0 - 1.0) * uResolution.xy / mr;
			uv += (uMouse - vec2(0.5)) * uAmplitude;
			float d = -uTime * 0.5 * uSpeed;
			float a = 0.0;
			for (float i = 0.0; i < 8.0; ++i) {
				a += cos(i - d - a * uv.x);
				d += sin(uv.y * i + a);
			}
			d += uTime * 0.5 * uSpeed;
			vec3 col = vec3(cos(uv * vec2(d, a)) * 0.6 + 0.4, cos(a + d) * 0.5 + 0.5);
			col = cos(col * cos(vec3(d, a, 2.5)) * 0.5 + 0.5) * uColor;
			gl_FragColor = vec4(col, 1.0);
		}
	`;

	type Props = Omit<Omit<HTMLAttributes<HTMLDivElement>, 'style'>, 'color'> & {
		/** Base color as [r, g, b], each 0..1. @default [0.3, 0.2, 0.5] */
		color?: [number, number, number];
		/** Animation speed multiplier. @default 1 */
		speed?: number;
		/** Amplitude of the mouse-driven pan. @default 0.1 */
		amplitude?: number;
		/** Enable mouse interaction with the shader. @default false */
		mouseReact?: boolean;
	};

	let {
		color = [0.3, 0.2, 0.5],
		speed = 1.0,
		amplitude = 0.1,
		mouseReact = false,
		class: className,
		...rest
	}: Props = $props();

	let container: HTMLDivElement | undefined = $state();

	const reducedMotionQuery = new MediaQuery('(prefers-reduced-motion: reduce)');

	$effect(() => {
		const el = container;
		if (!el) return;

		const renderer = new Renderer();
		const gl = renderer.gl;
		gl.clearColor(1, 1, 1, 1);

		const mousePos = { x: 0.5, y: 0.5 };

		const program = new Program(gl, {
			vertex: vertexShader,
			fragment: fragmentShader,
			uniforms: {
				uTime: { value: 0 },
				uColor: { value: new Color(...color) },
				uResolution: {
					value: new Color(gl.canvas.width, gl.canvas.height, gl.canvas.width / gl.canvas.height)
				},
				uMouse: { value: new Float32Array([mousePos.x, mousePos.y]) },
				uAmplitude: { value: amplitude },
				uSpeed: { value: speed }
			}
		});

		const geometry = new Triangle(gl);
		const mesh = new Mesh(gl, { geometry, program });

		const resize = () => {
			renderer.setSize(el.offsetWidth, el.offsetHeight);
			program.uniforms.uResolution.value = new Color(
				gl.canvas.width,
				gl.canvas.height,
				gl.canvas.width / gl.canvas.height
			);
		};

		const resizeObserver = new ResizeObserver(resize);
		resizeObserver.observe(el);
		resize();

		el.appendChild(gl.canvas);

		const handleMouseMove = (e: MouseEvent) => {
			const rect = el.getBoundingClientRect();
			const x = (e.clientX - rect.left) / rect.width;
			const y = 1.0 - (e.clientY - rect.top) / rect.height;
			program.uniforms.uMouse.value[0] = x;
			program.uniforms.uMouse.value[1] = y;
		};
		if (mouseReact) el.addEventListener('mousemove', handleMouseMove);

		const frame = (tSec: number) => {
			program.uniforms.uTime.value = tSec;
			renderer.render({ scene: mesh });
		};

		// reduced motion → one static, deterministic frame
		if (reducedMotionQuery.current) {
			frame(0.6);
			return () => {
				resizeObserver.disconnect();
				if (mouseReact) el.removeEventListener('mousemove', handleMouseMove);
				el.removeChild(gl.canvas);
				gl.getExtension('WEBGL_lose_context')?.loseContext();
			};
		}

		let raf = 0;
		let running = false;
		const loop = () => {
			frame(performance.now() * 0.001);
			if (running) raf = requestAnimationFrame(loop);
		};
		const start = () => {
			if (running) return;
			running = true;
			raf = requestAnimationFrame(loop);
		};
		const stop = () => {
			running = false;
			cancelAnimationFrame(raf);
		};

		// pause offscreen + on hidden tabs — free when not visible
		let visible = true;
		const io = new IntersectionObserver(([entry]) => {
			visible = entry.isIntersecting;
			if (visible && document.visibilityState !== 'hidden') start();
			else stop();
		});
		io.observe(el);
		const onVisibilityChange = () => {
			if (document.visibilityState === 'hidden') stop();
			else if (visible) start();
		};
		document.addEventListener('visibilitychange', onVisibilityChange);

		return () => {
			stop();
			io.disconnect();
			resizeObserver.disconnect();
			document.removeEventListener('visibilitychange', onVisibilityChange);
			if (mouseReact) el.removeEventListener('mousemove', handleMouseMove);
			el.removeChild(gl.canvas);
			gl.getExtension('WEBGL_lose_context')?.loseContext();
		};
	});
</script>

<div bind:this={container} class={cn('h-full w-full overflow-hidden', className)} {...rest}></div>
