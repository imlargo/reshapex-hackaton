import type { Handle, HandleServerError } from '@sveltejs/kit';
import { config } from '$lib/config';
import { AuthService, createAuthHandler } from '$lib/features/auth';
import { serverAuthCookies } from '$lib/features/auth/server';
import { normalizeError } from '$lib/core/errors';

export const handleError: HandleServerError = ({ error, status }) => {
	const err = normalizeError(error);
	if (status !== 404) console.error('[server error]', err);
	return { message: err.getMessage() };
};
