<script lang="ts">
	import { PitchView } from '$lib/features/pitch';
	import { config } from '$lib/config';
</script>

<svelte:head>
	<title>Pitch — {config.name}</title>
</svelte:head>

<PitchView />
