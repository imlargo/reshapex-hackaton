<script lang="ts">
	import { ThinkingOrb, OrbState } from '$lib/components/common/thinking-orb';
	import { Button } from '$lib/components/ui/button/index.js';
	import ArrowRightIcon from '@lucide/svelte/icons/arrow-right';
</script>

<div class="flex h-full flex-col items-center justify-center gap-8 p-8 text-center sm:p-14">
	<ThinkingOrb state={OrbState.LISTENING} size={64} />

	<div class="flex flex-col gap-3">
		<h2 class="text-4xl font-semibold tracking-tight sm:text-6xl">Gracias</h2>
		<p class="max-w-xl text-base text-muted-foreground sm:text-lg">
			SICK — conocimiento con procedencia. Construido en un sprint de ~3.5 horas para AgentSprint
			by ReshapeX.
		</p>
	</div>

	<div class="flex flex-wrap items-center justify-center gap-3">
		<Button href="/">
			Ver el dashboard
			<ArrowRightIcon class="size-4" />
		</Button>
		<Button href="/about" variant="outline">Ver el producto</Button>
	</div>
</div>
