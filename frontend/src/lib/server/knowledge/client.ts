import { knowledgeApiBaseUrl, knowledgeCorpusDir } from './config';

export class KnowledgeBackendError extends Error {
	readonly status: number;
	readonly payload: unknown;

	constructor(message: string, status: number, payload: unknown) {
		super(message);
		this.name = 'KnowledgeBackendError';
		this.status = status;
		this.payload = payload;
	}
}

async function parseJson(response: Response): Promise<unknown> {
	try {
		return await response.json();
	} catch {
		return null;
	}
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
	const response = await fetch(`${knowledgeApiBaseUrl()}${path}`, {
		...init,
		headers: {
			'Content-Type': 'application/json',
			...(init?.headers ?? {})
		}
	});
	const payload = await parseJson(response);
	if (!response.ok) {
		const detail =
			typeof payload === 'object' && payload !== null && 'detail' in payload
				? String((payload as { detail: unknown }).detail)
				: `Knowledge API ${response.status}`;
		throw new KnowledgeBackendError(detail, response.status, payload);
	}
	return payload as T;
}

export interface BackendHealthResponse {
	status: string;
	provider_configured: boolean;
	knowledge_base_ready: boolean;
	index_id: string | null;
	readiness: string | null;
}

export interface BackendBuildResponse {
	build: {
		inventory: Record<string, unknown>;
		package: Record<string, unknown>;
		plan: Record<string, unknown>;
		validation: Record<string, unknown>;
		readiness: string;
	};
	query_contract: {
		index_id: string;
		validation_status: string;
		supported_question_min_length: number;
		supported_question_max_length: number;
	};
}

export interface BackendQueryResponse {
	index_id: string;
	question: string;
	answer: {
		answer: string;
		citations: Array<{ evidence_id: string; claim: string; source_id?: string; location?: string }>;
		confidence: string;
		evidence_grade: string;
		unresolved_risk: string;
		next_action: string;
		sufficient_evidence: boolean;
		trace: { steps: number; tool_events: unknown[]; latency_ms: number };
	};
	validation_status: string;
}

export function fetchKnowledgeHealth(): Promise<BackendHealthResponse> {
	return request<BackendHealthResponse>('/api/health');
}

export function buildKnowledgeBase(representativeOnly = true): Promise<BackendBuildResponse> {
	return request<BackendBuildResponse>('/api/knowledge/build', {
		method: 'POST',
		body: JSON.stringify({
			corpus_dir: knowledgeCorpusDir(),
			representative_only: representativeOnly
		})
	});
}

export function queryKnowledgeBase(question: string, deterministic = false): Promise<BackendQueryResponse> {
	return request<BackendQueryResponse>('/api/knowledge/query', {
		method: 'POST',
		body: JSON.stringify({ question, deterministic })
	});
}
