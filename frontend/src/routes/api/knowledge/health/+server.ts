import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { fetchKnowledgeHealth, KnowledgeBackendError } from '$lib/server/knowledge/client';

export const GET: RequestHandler = async () => {
	try {
		const health = await fetchKnowledgeHealth();
		return json(health);
	} catch (error) {
		const status = error instanceof KnowledgeBackendError ? error.status : 502;
		return json(
			{
				status: 'unavailable',
				message: error instanceof Error ? error.message : 'Knowledge backend unavailable'
			},
			{ status: status >= 400 ? status : 502 }
		);
	}
};
