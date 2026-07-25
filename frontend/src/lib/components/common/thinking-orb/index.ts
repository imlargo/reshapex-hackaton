export { default as ThinkingOrb } from './ThinkingOrb.svelte';

export { OrbState, OrbTheme } from './types';
export type { OrbSize } from './types';

// Power-user surface: the resolved presets + raw frame painters, for
// consumers driving their own canvas outside this component.
export { resolvePreset, STATE_TO_MODE, type ModeKey, type Resolved } from './presets';
export { MODE_DRAWS } from './engine/registry';
