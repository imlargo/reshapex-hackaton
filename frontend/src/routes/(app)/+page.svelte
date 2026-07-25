<script lang="ts">
	import { DashboardView } from '$lib/features/dashboard';
	import { config } from '$lib/config';
</script>

<svelte:head>
	<title>Dashboard — {config.name}</title>
</svelte:head>

<DashboardView />
