<script lang="ts">
	import * as InputGroup from '$lib/components/ui/input-group/index.js';
	import { SOURCE_INTAKE_ACCEPT, SOURCE_TYPE_LABELS } from '$lib/config';
	import type { IngestionStore } from '../stores/ingestion.svelte';
	import PaperclipIcon from '@lucide/svelte/icons/paperclip';
	import Link2Icon from '@lucide/svelte/icons/link-2';
	import XIcon from '@lucide/svelte/icons/x';

	let { store }: { store: IngestionStore } = $props();

	let apiUrl = $state('');
	let fileInputEl: HTMLInputElement | undefined = $state();

	function handleAddApi() {
		store.addApiSource(apiUrl);
		apiUrl = '';
	}

	function handleFilesPicked(e: Event) {
		const input = e.currentTarget as HTMLInputElement;
		if (input.files?.length) store.addFiles(Array.from(input.files));
		input.value = '';
	}
</script>

<div class="flex flex-col gap-3">
	{#if store.sources.length > 0}
		<div class="flex flex-wrap gap-1.5">
			{#each store.fileSources as source (source.id)}
				<span class="inline-flex items-center gap-1 rounded-full bg-muted px-2 py-0.5 text-xs">
					{SOURCE_TYPE_LABELS[source.type]} · {source.name}
					<button
						type="button"
						class="hover:text-destructive"
						disabled={store.isRunning}
						onclick={() => store.removeFileSource(source.id)}
					>
						<XIcon class="size-3" />
						<span class="sr-only">Quitar {source.name}</span>
					</button>
				</span>
			{/each}
			{#each store.apiSources as source (source.id)}
				<span class="inline-flex items-center gap-1 rounded-full bg-muted px-2 py-0.5 text-xs">
					{SOURCE_TYPE_LABELS[source.type]} · {source.name}
					<button
						type="button"
						class="hover:text-destructive"
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

	<input
		bind:this={fileInputEl}
		type="file"
		multiple
		accept={SOURCE_INTAKE_ACCEPT}
		class="hidden"
		onchange={handleFilesPicked}
	/>

	<InputGroup.Root>
		<InputGroup.Addon>
			<InputGroup.Button
				size="icon-xs"
				class="rounded-full"
				disabled={store.isRunning}
				onclick={() => fileInputEl?.click()}
				aria-label="Adjuntar archivos"
			>
				<PaperclipIcon />
			</InputGroup.Button>
		</InputGroup.Addon>
		<InputGroup.Input
			placeholder="Pegá la URL de una API…"
			bind:value={apiUrl}
			disabled={store.isRunning}
			onkeydown={(e) => e.key === 'Enter' && handleAddApi()}
		/>
		<InputGroup.Addon align="inline-end">
			<InputGroup.Button
				size="icon-xs"
				class="rounded-full"
				onclick={handleAddApi}
				disabled={store.isRunning || !apiUrl.trim()}
				aria-label="Agregar API"
			>
				<Link2Icon />
			</InputGroup.Button>
		</InputGroup.Addon>
	</InputGroup.Root>
</div>
