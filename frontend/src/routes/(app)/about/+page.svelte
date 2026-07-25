<script lang="ts">
	import { ProductView } from '$lib/features/product';
	import { config } from '$lib/config';
</script>

<svelte:head>
	<title>Producto — {config.name}</title>
</svelte:head>

<ProductView />
