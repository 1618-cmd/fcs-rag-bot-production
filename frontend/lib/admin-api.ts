/**
 * Admin API client for document approval workflow.
 */

import { getAuthToken } from './auth-api';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// Helper to get auth headers
function getAuthHeaders() {
  const token = getAuthToken();
  return {
    'Content-Type': 'application/json',
    ...(token && { 'Authorization': `Bearer ${token}` }),
  };
}

export interface Document {
  key: string;
  name: string;
  path: string;
  size: number;
  last_modified: string;
  status?: 'pending' | 'approved' | 'rejected';
}

export interface ApproveRequest {
  document_key: string;
}

export interface RejectRequest {
  document_key: string;
  reason?: string;
}

/**
 * Get list of pending documents awaiting approval.
 */
export async function getPendingDocuments(): Promise<Document[]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/documents/pending`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    throw new Error(`Failed to get pending documents: ${response.statusText}`);
  }

  return response.json();
}

/**
 * Get list of approved documents.
 */
export async function getApprovedDocuments(): Promise<Document[]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/documents/approved`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    throw new Error(`Failed to get approved documents: ${response.statusText}`);
  }

  return response.json();
}

/**
 * Get list of archived/rejected documents.
 */
export async function getArchivedDocuments(): Promise<Document[]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/documents/archived`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    throw new Error(`Failed to get archived documents: ${response.statusText}`);
  }

  return response.json();
}

/**
 * Approve a document (move from staging to approved).
 */
export async function approveDocument(documentKey: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/admin/documents/approve`, {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify({ document_key: documentKey }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || `Failed to approve document: ${response.statusText}`);
  }
}

/**
 * Reject a document (move from staging to archive).
 */
export async function rejectDocument(documentKey: string, reason?: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/admin/documents/reject`, {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify({ document_key: documentKey, reason }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || `Failed to reject document: ${response.statusText}`);
  }
}

export interface UploadResponse {
  success: boolean;
  message: string;
  document_key: string;
  filename: string;
}

/**
 * Upload a document to staging folder for approval.
 */
export async function uploadDocument(file: File): Promise<UploadResponse> {
  const token = getAuthToken();
  
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_BASE_URL}/api/admin/documents/upload`, {
    method: 'POST',
    headers: {
      ...(token && { 'Authorization': `Bearer ${token}` }),
      // Don't set Content-Type - let browser set it with boundary for FormData
    },
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || `Failed to upload document: ${response.statusText}`);
  }

  return response.json();
}
