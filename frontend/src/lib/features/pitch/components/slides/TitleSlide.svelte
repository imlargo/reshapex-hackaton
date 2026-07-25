<script lang="ts">
	import { ThinkingOrb, OrbState } from '$lib/components/common/thinking-orb';
	import { Badge } from '$lib/components/ui/badge/index.js';
</script>

<div class="flex h-full flex-col items-center justify-center gap-8 p-8 text-center sm:p-14">
	<ThinkingOrb state={OrbState.SHAPING} size={64} />

	<div class="flex flex-col gap-4">
		<h1 class="text-5xl font-semibold tracking-tight sm:text-7xl">SICK</h1>
		<p class="max-w-xl text-lg text-muted-foreground sm:text-xl">
			El ingeniero de aplicaciones que no se va a dormir.
		</p>
	</div>

	<div class="flex flex-wrap items-center justify-center gap-2">
		<Badge variant="outline">AgentSprint by ReshapeX</Badge>
		<Badge variant="outline">Universidad EAFIT</Badge>
		<Badge variant="outline">25 jul 2026</Badge>
	</div>
</div>
