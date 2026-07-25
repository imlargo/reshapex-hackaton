import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { queryKnowledgeBase, KnowledgeBackendError } from '$lib/server/knowledge/client';

export const POST: RequestHandler = async ({ request }) => {
	const body = (await request.json()) as { question?: string; deterministic?: boolean };
	if (!body.question?.trim()) {
		return json({ message: 'question is required' }, { status: 400 });
	}
	try {
		const payload = await queryKnowledgeBase(body.question.trim(), body.deterministic ?? false);
		return json(payload);
	} catch (error) {
		const status = error instanceof KnowledgeBackendError ? error.status : 502;
		return json(
			{ message: error instanceof Error ? error.message : 'Query failed' },
			{ status: status >= 400 ? status : 502 }
		);
	}
};
