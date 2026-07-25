import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { buildKnowledgeBase, KnowledgeBackendError } from '$lib/server/knowledge/client';

export const POST: RequestHandler = async ({ request }) => {
	const body = (await request.json().catch(() => ({}))) as { representative_only?: boolean };
	try {
		const payload = await buildKnowledgeBase(body.representative_only ?? true);
		return json(payload);
	} catch (error) {
		const status = error instanceof KnowledgeBackendError ? error.status : 502;
		return json(
			{ message: error instanceof Error ? error.message : 'Build failed' },
			{ status: status >= 400 ? status : 502 }
		);
	}
};
