import { serverAuthCookies } from '$lib/features/auth/server';
import { config } from '$lib/config';
import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

function decodeRedirect(value: string | null): string | null {
	if (!value) return null;
	try {
		const decoded = atob(value);
		if (decoded.startsWith('/')) return decoded;
	} catch {
		// ignore malformed base64
	}
	return null;
}

export const load: PageServerLoad = async ({ cookies, url }) => {
	if (serverAuthCookies.isAuthenticated(cookies)) {
		const redirectTo = decodeRedirect(url.searchParams.get('redirect'));
		throw redirect(303, redirectTo ?? config.auth.defaultRedirectPath);
	}
};
