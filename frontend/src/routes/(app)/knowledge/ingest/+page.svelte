<script lang="ts">
	import { IngestionView } from '$lib/features/knowledge-ingestion';
	import { config } from '$lib/config';
</script>

<svelte:head>
	<title>Crear base de conocimiento — {config.name}</title>
</svelte:head>

<IngestionView />
