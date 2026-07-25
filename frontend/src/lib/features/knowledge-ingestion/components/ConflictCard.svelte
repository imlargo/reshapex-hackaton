<script lang="ts">
	import type { SourceConflictSample } from '../types';
	import TriangleAlertIcon from '@lucide/svelte/icons/triangle-alert';

	let { sample }: { sample: SourceConflictSample } = $props();
</script>

<div class="flex flex-col gap-2.5 rounded-lg border p-3" style="border-color: var(--destructive);">
	<div class="flex items-center gap-2 text-sm font-medium" style="color: var(--destructive);">
		<TriangleAlertIcon class="size-4" />
		Conflicto: {sample.fact}
	</div>
	<div class="grid grid-cols-2 gap-3 text-sm">
		<div class="flex flex-col gap-0.5">
			<span class="text-xs text-muted-foreground">{sample.sourceA.name}</span>
			<span class="font-medium">{sample.sourceA.value}</span>
		</div>
		<div class="flex flex-col gap-0.5">
			<span class="text-xs text-muted-foreground">{sample.sourceB.name}</span>
			<span class="font-medium">{sample.sourceB.value}</span>
		</div>
	</div>
	<p class="text-xs text-muted-foreground">
		Se marca como conflicto — no se promedia ni se elige un valor automáticamente.
	</p>
</div>
