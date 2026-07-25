/**
 * The six shipped states — each a hand-tuned animation:
 * - WORKING   — particles on tilted orbits
 * - SEARCHING — a scan meridian sweeps a dotted globe
 * - SOLVING   — bands scramble in quarter turns, then click back
 * - LISTENING — a waveform rolls through latitude rings
 * - COMPOSING — an undulating multi-band sash
 * - SHAPING   — a dotted outline morphs circle → triangle → square
 */
export enum OrbState {
	WORKING = 'working',
	SEARCHING = 'searching',
	SOLVING = 'solving',
	LISTENING = 'listening',
	COMPOSING = 'composing',
	SHAPING = 'shaping'
}

/**
 * Rendered size in CSS pixels. Exactly two tuned presets ship: 64
 * (chat-avatar scale) and 20 (inline-text scale). Each size carries its
 * own dot count, dot size and speed tuning — they are separate designs,
 * not a scale factor.
 */
export type OrbSize = 64 | 20;

/**
 * Theme mode.
 *
 * - AUTO (default) resolves in three layers, live-updating on change:
 *   1. a `data-theme="dark|light"` attribute or `dark`/`light` class on
 *      any ancestor (the Tailwind / shadcn convention);
 *   2. otherwise `prefers-color-scheme: dark`;
 *   3. defaults to dark before the client can resolve either.
 * - DARK / LIGHT pin the palette regardless of context.
 */
export enum OrbTheme {
	AUTO = 'auto',
	DARK = 'dark',
	LIGHT = 'light'
}
