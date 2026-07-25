<script lang="ts">
	import { FileInput } from '$lib/components/base';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import { SOURCE_INTAKE_ACCEPT, SOURCE_TYPE_LABELS } from '$lib/config';
	import type { IngestionStore } from '../stores/ingestion.svelte';
	import PaperclipIcon from '@lucide/svelte/icons/paperclip';
	import Link2Icon from '@lucide/svelte/icons/link-2';
	import XIcon from '@lucide/svelte/icons/x';

	let { store }: { store: IngestionStore } = $props();

	let apiUrl = $state('');
	// Arranca abierto: es la primera interacción del usuario con la vista.
	let showDropzone = $state(true);

	function handleAddApi() {
		store.addApiSource(apiUrl);
		apiUrl = '';
	}
</script>

<div class="flex flex-col gap-3">
	{#if store.sources.length > 0}
		<div class="flex flex-wrap gap-1.5">
			{#each store.fileSources as source (source.id)}
				<span class="inline-flex items-center gap-1 rounded-full bg-muted px-2 py-0.5 text-xs">
					{SOURCE_TYPE_LABELS[source.type]} · {source.name}
				</span>
			{/each}
			{#each store.apiSources as source (source.id)}
				<span class="inline-flex items-center gap-1 rounded-full bg-muted px-2 py-0.5 text-xs">
					{SOURCE_TYPE_LABELS[source.type]} · {source.name}
					<button
						type="button"
						class="rounded-full hover:text-destructive"
						disabled={store.isRunning}
						onclick={() => store.removeApiSource(source.id)}
					>
						<XIcon class="size-3" />
						<span class="sr-only">Quitar {source.name}</span>
					</button>
				</span>
			{/each}
		</div>
	{/if}

	<div class:hidden={!showDropzone}>
		{#key store.resetToken}
			<FileInput
				variant="multiple"
				accept={SOURCE_INTAKE_ACCEPT}
				maxFiles={20}
				disabled={store.isRunning}
				onFilesChange={(files) => store.setFiles(files)}
			/>
		{/key}
	</div>

	<div class="flex items-center gap-2">
		<Button
			type="button"
			variant="outline"
			size="icon"
			disabled={store.isRunning}
			onclick={() => (showDropzone = !showDropzone)}
			aria-label={showDropzone ? 'Ocultar archivos' : 'Adjuntar archivos'}
		>
			<PaperclipIcon class="size-4" />
		</Button>
		<Input
			type="url"
			placeholder="Pegá la URL de una API…"
			bind:value={apiUrl}
			disabled={store.isRunning}
			onkeydown={(e) => e.key === 'Enter' && handleAddApi()}
			class="flex-1"
		/>
		<Button
			type="button"
			variant="outline"
			size="icon"
			onclick={handleAddApi}
			disabled={store.isRunning || !apiUrl.trim()}
			aria-label="Agregar API"
		>
			<Link2Icon class="size-4" />
		</Button>
	</div>
</div>
