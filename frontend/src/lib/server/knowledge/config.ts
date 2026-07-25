import { env } from '$env/dynamic/private';

const DEFAULT_KNOWLEDGE_API_URL = 'http://127.0.0.1:8001';
const DEFAULT_CORPUS_DIR = '../contents';

export function knowledgeApiBaseUrl(): string {
	return (env.KNOWLEDGE_API_URL ?? DEFAULT_KNOWLEDGE_API_URL).replace(/\/$/, '');
}

export function knowledgeCorpusDir(): string {
	return env.KNOWLEDGE_CORPUS_DIR ?? DEFAULT_CORPUS_DIR;
}
