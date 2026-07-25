import { redirect } from '@sveltejs/kit';
import { config } from '$lib/config';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {
	if (config.auth.enabled && !locals.user) throw redirect(303, '/login');

	return {
		user: locals.user ?? null
	};
};
