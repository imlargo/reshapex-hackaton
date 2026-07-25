<script lang="ts">
	import * as Item from '$lib/components/ui/item/index.js';
	import { relativeTime } from '$lib/utils/date';
	import { ActivitySeverity } from '$lib/types/knowledge';
	import type { ActivityEvent } from '$lib/types/knowledge';
	import CircleAlertIcon from '@lucide/svelte/icons/circle-alert';
	import TriangleAlertIcon from '@lucide/svelte/icons/triangle-alert';
	import InfoIcon from '@lucide/svelte/icons/info';

	let { events }: { events: ActivityEvent[] } = $props();

	const SEVERITY_STYLE: Record<ActivitySeverity, { icon: typeof InfoIcon; color: string }> = {
		[ActivitySeverity.CRITICAL]: { icon: CircleAlertIcon, color: 'var(--destructive)' },
		[ActivitySeverity.WARNING]: { icon: TriangleAlertIcon, color: 'var(--warning)' },
		[ActivitySeverity.INFO]: { icon: InfoIcon, color: 'var(--muted-foreground)' }
	};
</script>

<Item.Group class="gap-2">
	{#each events as event (event.id)}
		{@const meta = SEVERITY_STYLE[event.severity]}
		<Item.Root
			variant="outline"
			size="sm"
			style="border-left: 2px solid {meta.color};"
		>
			<Item.Media variant="icon">
				<meta.icon class="size-4" style="color: {meta.color};" />
			</Item.Media>
			<Item.Content>
				<Item.Description class="line-clamp-2 text-foreground">{event.message}</Item.Description>
				<span class="text-xs text-muted-foreground">{relativeTime(event.timestamp)}</span>
			</Item.Content>
		</Item.Root>
	{/each}
</Item.Group>
