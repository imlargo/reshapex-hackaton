import { serverAuthCookies } from '$lib/features/auth/server';
import { config } from '$lib/config';
import type { PageServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';

export const load = (async ({ cookies }) => {
	serverAuthCookies.clearTokens(cookies);
	redirect(303, config.auth.defaultRedirectPath);
}) satisfies PageServerLoad;
