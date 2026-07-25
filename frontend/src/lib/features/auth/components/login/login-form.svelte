<script lang="ts">
	import { Label } from '$lib/components/ui/label/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import { cn, type WithElementRef } from '$lib/utils.js';
	import type { HTMLFormAttributes } from 'svelte/elements';
	import { goto } from '$app/navigation';
	import { config } from '$lib/config';

	// Demo-only credentials: no auth backend is wired up yet (see .env: PUBLIC_AUTH_ENABLED=false).
	const DEMO_EMAIL = 'reshape@gmail.com';
	const DEMO_PASSWORD = '123';
	const FAKE_LOGIN_DELAY_MS = 900;

	let {
		ref = $bindable(null),
		class: className,
		...restProps
	}: WithElementRef<HTMLFormAttributes> = $props();

	let email = $state('');
	let password = $state('');
	let loading = $state(false);
	let error = $state<string | null>(null);

	async function handleSubmit(event: SubmitEvent) {
		event.preventDefault();
		error = null;
		loading = true;

		await new Promise((resolve) => setTimeout(resolve, FAKE_LOGIN_DELAY_MS));

		if (email !== DEMO_EMAIL || password !== DEMO_PASSWORD) {
			error = 'Invalid email or password.';
			loading = false;
			return;
		}

		try {
			await goto(config.auth.defaultRedirectPath);
		} catch {
			error = 'Something went wrong. Please try again.';
			loading = false;
		}
	}
</script>

<form
	class={cn('flex flex-col gap-6', className)}
	bind:this={ref}
	onsubmit={handleSubmit}
	{...restProps}
>
	<div class="flex flex-col items-center gap-2 text-center">
		<h1 class="text-2xl font-bold">Sign in to your account</h1>
		<p class="text-sm text-balance text-muted-foreground">
			Enter your email and password to sign in.
		</p>
	</div>

	{#if error}
		<p class="rounded-md bg-destructive/10 px-3 py-2 text-center text-sm text-destructive">
			{error}
		</p>
	{/if}

	<div class="grid gap-6">
		<div class="grid gap-2">
			<Label for="email">Email</Label>
			<Input
				id="email"
				type="email"
				placeholder="reshape@gmail.com"
				autocomplete="email"
				disabled={loading}
				bind:value={email}
			/>
		</div>

		<div class="grid gap-2">
			<Label for="password">Password</Label>
			<Input
				id="password"
				type="password"
				autocomplete="current-password"
				disabled={loading}
				bind:value={password}
			/>
		</div>

		<Button type="submit" class="w-full" disabled={loading}>
			{loading ? 'Signing in...' : 'Sign in'}
		</Button>
	</div>
</form>
