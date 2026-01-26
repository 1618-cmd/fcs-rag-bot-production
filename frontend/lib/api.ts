/**
 * API client for FCS RAG Bot backend.
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface QueryRequest {
  question: string;
  top_k?: number;
  skip_cache?: boolean;
  llm_provider?: 'openai' | 'anthropic';
}

export interface Source {
  name: string;
  content?: string;
}

export interface QueryResponse {
  answer: string;
  sources: Source[];
  latency_ms: number;
  model: string;
}

export async function queryRAG(
  question: string, 
  skipCache: boolean = false,
  llmProvider?: 'openai' | 'anthropic'
): Promise<QueryResponse> {
  try {
    const body: QueryRequest = { question, skip_cache: skipCache };
    if (llmProvider) {
      body.llm_provider = llmProvider;
    }
    
    const response = await fetch(`${API_BASE_URL}/api/query`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
      throw new Error(error.detail || `HTTP error! status: ${response.status}`);
    }

    return response.json();
  } catch (err) {
    if (err instanceof TypeError && err.message.includes('fetch')) {
      throw new Error(`Unable to connect to backend API. Please check that the backend is running at ${API_BASE_URL}`);
    }
    throw err;
  }
}

export async function checkHealth(): Promise<{ status: string; environment: string; version: string }> {
  const response = await fetch(`${API_BASE_URL}/api/health`);
  if (!response.ok) {
    throw new Error('Health check failed');
  }
  return response.json();
}

export interface CreateTicketRequest {
  question: string;
  bot_response?: string;
  sources?: Source[];
  user_context?: string;
}

export interface CreateTicketResponse {
  success: boolean;
  ticket_key?: string;
  ticket_url?: string;
  error?: string;
}

export async function createJiraTicket(request: CreateTicketRequest): Promise<CreateTicketResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/api/jira/create-ticket`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
      throw new Error(error.detail || `HTTP error! status: ${response.status}`);
    }

    return response.json();
  } catch (err) {
    if (err instanceof TypeError && err.message.includes('fetch')) {
      throw new Error(`Unable to connect to backend API. Please check that the backend is running at ${API_BASE_URL}`);
    }
    throw err;
  }
}

export async function checkJiraStatus(): Promise<{ configured: boolean; server_url?: string; project_key?: string; issue_type?: string }> {
  const response = await fetch(`${API_BASE_URL}/api/jira/status`);
  if (!response.ok) {
    return { configured: false };
  }
  return response.json();
}


