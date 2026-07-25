<script lang="ts">
	import { page } from '$app/state';
	import * as Sidebar from '$lib/components/ui/sidebar/index.js';
	import AppSidebar from '$lib/components/layout/sidebar/app-sidebar.svelte';
	import SiteHeader from '$lib/components/layout/sidebar/site-header.svelte';
	import { Iridescence } from '$lib/components/common';
	import type { LayoutProps } from './$types';

	let { data, children }: LayoutProps = $props();

	const showIngestionBackground = $derived(page.url.pathname === '/knowledge/ingest');
</script>

<Sidebar.Provider
	class="h-screen"
	style="--sidebar-width: calc(var(--spacing) * 64); --header-height: calc(var(--spacing) * 12);"
>
	<AppSidebar user={data.user} variant="inset" />
	<Sidebar.Inset class="flex h-[calc(100%-1rem)] min-h-0 flex-col overflow-hidden">
		{#if showIngestionBackground}
			<div class="pointer-events-none absolute inset-0 opacity-10 grayscale">
				<Iridescence color={[1, 1, 1]} amplitude={0.15} speed={0.7} />
			</div>
		{/if}

		<div class="relative z-10 flex h-full min-h-0 flex-1 flex-col">
			<SiteHeader />
			<div class="@container/main flex min-h-0 flex-1 flex-col overflow-auto">
				<div
					id="main-content"
					class="flex min-h-full flex-1 flex-col px-4 pt-4 pb-8 md:px-8 md:pt-6"
				>
					{@render children()}
				</div>
			</div>
		</div>
	</Sidebar.Inset>
</Sidebar.Provider>
