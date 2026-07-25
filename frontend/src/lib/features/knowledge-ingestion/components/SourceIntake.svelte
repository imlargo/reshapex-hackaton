<script lang="ts">
	import { FileInput } from '$lib/components/base';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Item from '$lib/components/ui/item/index.js';
	import { SOURCE_INTAKE_ACCEPT, SOURCE_TYPE_LABELS } from '$lib/config';
	import type { IngestionStore } from '../stores/ingestion.svelte';
	import Link2Icon from '@lucide/svelte/icons/link-2';
	import XIcon from '@lucide/svelte/icons/x';

	let { store }: { store: IngestionStore } = $props();

	let apiUrl = $state('');

	function handleAddApi() {
		store.addApiSource(apiUrl);
		apiUrl = '';
	}
</script>

<div class="flex flex-col gap-4">
	{#key store.resetToken}
		<FileInput
			variant="multiple"
			accept={SOURCE_INTAKE_ACCEPT}
			maxFiles={20}
			disabled={store.isRunning}
			onFilesChange={(files) => store.setFiles(files)}
		/>
	{/key}

	<div class="flex items-center gap-2">
		<Input
			type="url"
			placeholder="https://api.proveedor.com/catalogo"
			bind:value={apiUrl}
			disabled={store.isRunning}
			onkeydown={(e) => e.key === 'Enter' && handleAddApi()}
		/>
		<Button
			type="button"
			variant="outline"
			onclick={handleAddApi}
			disabled={store.isRunning || !apiUrl.trim()}
		>
			<Link2Icon class="size-4" />
			Agregar API
		</Button>
	</div>

	{#if store.apiSources.length > 0}
		<Item.Group class="gap-2">
			{#each store.apiSources as source (source.id)}
				<Item.Root variant="outline" size="sm">
					<Item.Media variant="icon">
						<Link2Icon class="size-4 text-muted-foreground" />
					</Item.Media>
					<Item.Content>
						<Item.Title>{source.name}</Item.Title>
						<Item.Description>{SOURCE_TYPE_LABELS[source.type]}</Item.Description>
					</Item.Content>
					<Item.Actions>
						<Button
							variant="ghost"
							size="icon"
							class="size-8"
							disabled={store.isRunning}
							onclick={() => store.removeApiSource(source.id)}
						>
							<XIcon class="size-4" />
							<span class="sr-only">Quitar fuente</span>
						</Button>
					</Item.Actions>
				</Item.Root>
			{/each}
		</Item.Group>
	{/if}
</div>
