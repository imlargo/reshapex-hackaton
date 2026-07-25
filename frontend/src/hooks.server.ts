import type { HandleServerError } from '@sveltejs/kit';
import { normalizeError } from '$lib/core/errors';

export const handleError: HandleServerError = ({ error, status }) => {
	const err = normalizeError(error);
	if (status !== 404) console.error('[server error]', err);
	return { message: err.getMessage() };
};
