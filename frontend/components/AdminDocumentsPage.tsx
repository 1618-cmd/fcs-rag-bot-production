/**
 * Admin Documents Page - Visual Mockup/Implementation
 * 
 * This is the main approval UI page for managers to review documents.
 * Shows pending documents with approve/reject functionality.
 */

'use client';

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { AdminDocumentCard } from './AdminDocumentCard';
import Container from './Container';
import {
  getPendingDocuments,
  getApprovedDocuments,
  getArchivedDocuments,
  approveDocument,
  rejectDocument,
  uploadDocument,
  Document,
} from '@/lib/admin-api';
import { checkAuthStatus, logout, getAuthToken } from '@/lib/auth-api';

type Tab = 'pending' | 'approved' | 'rejected' | 'all';

export const AdminDocumentsPage: React.FC = () => {
  const router = useRouter();
  const [activeTab, setActiveTab] = useState<Tab>('pending');
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [authenticated, setAuthenticated] = useState(false);
  const [checkingAuth, setCheckingAuth] = useState(true);
  const [uploading, setUploading] = useState(false);
  const [uploadSuccess, setUploadSuccess] = useState<string | null>(null);

  // Check authentication on mount (optional - don't redirect)
  useEffect(() => {
    const checkAuth = async () => {
      const status = await checkAuthStatus();
      setAuthenticated(status.authenticated);
      setCheckingAuth(false);
      // No redirect - page is accessible without login
    };
    checkAuth();
  }, []);

  // Load documents when tab changes
  useEffect(() => {
    loadDocuments();
  }, [activeTab]);

  const loadDocuments = async () => {
    setLoading(true);
    setError(null);
    try {
      let docs: Document[] = [];
      if (activeTab === 'pending') {
        docs = await getPendingDocuments();
      } else if (activeTab === 'approved') {
        docs = await getApprovedDocuments();
      } else if (activeTab === 'rejected') {
        docs = await getArchivedDocuments();
      } else {
        // All - combine all tabs
        const [pending, approved, archived] = await Promise.all([
          getPendingDocuments(),
          getApprovedDocuments(),
          getArchivedDocuments(),
        ]);
        docs = [...pending, ...approved, ...archived];
      }
      setDocuments(docs);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load documents');
    } finally {
      setLoading(false);
    }
  };

  const handleApprove = async (documentKey: string) => {
    try {
      await approveDocument(documentKey);
      // Reload documents after approval
      await loadDocuments();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to approve document');
    }
  };

  const handleReject = async (documentKey: string, reason?: string) => {
    try {
      await rejectDocument(documentKey, reason);
      // Reload documents after rejection
      await loadDocuments();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to reject document');
    }
  };

  const handlePreview = (documentKey: string) => {
    // TODO: Implement preview modal
    console.log('Preview document:', documentKey);
    alert(`Preview for: ${documentKey}\n\nThis feature will be implemented in a future update.`);
  };

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    setUploading(true);
    setError(null);
    setUploadSuccess(null);

    try {
      const result = await uploadDocument(file);
      setUploadSuccess(`Document "${result.filename}" uploaded successfully to staging.`);
      // Clear file input
      event.target.value = '';
      // Reload documents to show the new upload
      await loadDocuments();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to upload document');
    } finally {
      setUploading(false);
    }
  };

  const [tabCounts, setTabCounts] = useState({
    pending: 0,
    approved: 0,
    rejected: 0,
    all: 0,
  });

  // Calculate tab counts (fetch all to get accurate counts)
  useEffect(() => {
    const fetchCounts = async () => {
      try {
        const [pending, approved, archived] = await Promise.all([
          getPendingDocuments(),
          getApprovedDocuments(),
          getArchivedDocuments(),
        ]);
        setTabCounts({
          pending: pending.length,
          approved: approved.length,
          rejected: archived.length,
          all: pending.length + approved.length + archived.length,
        });
      } catch (err) {
        // Ignore errors for counts
      }
    };
    fetchCounts();
  }, [documents]);

  return (
    <div className="min-h-screen bg-white" style={{ paddingTop: 'calc(3.5rem + 2rem)' }}>
      <Container size="xl">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-semibold text-gray-900 mb-2">
            Document Management
          </h1>
          <p className="text-base text-gray-600">
            Review and approve documents for the knowledge base
          </p>
        </div>

        {/* Upload Form */}
        <div className="mb-6 p-6 bg-white border border-gray-200 rounded-lg">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Upload Document</h2>
          
          {/* File Requirements */}
          <div className="mb-4 p-4 bg-gray-50 border border-gray-200 rounded-md">
            <h3 className="text-sm font-semibold text-gray-900 mb-2">File Requirements</h3>
            <ul className="text-sm text-gray-600 space-y-1 mb-3">
              <li>✅ <strong>Formats:</strong> Markdown (.md), Text (.txt), or PDF (.pdf)</li>
              <li>✅ <strong>Encoding:</strong> UTF-8 (for text files)</li>
              <li>✅ <strong>Size:</strong> Under 10MB recommended</li>
              <li>✅ <strong>Naming:</strong> Use descriptive names with prefixes: <code className="text-xs bg-gray-200 px-1 rounded">(Reference) - Document Title.md</code></li>
            </ul>
            <details className="text-sm">
              <summary className="cursor-pointer text-gray-700 hover:text-gray-900 font-medium">📋 Best Practices (click to expand)</summary>
              <div className="mt-3 pl-4 space-y-2 text-gray-600">
                <p><strong>Formatting:</strong></p>
                <ul className="list-disc list-inside space-y-1 ml-2">
                  <li>Use clear heading hierarchy (# H1, ## H2, ### H3)</li>
                  <li>Separate paragraphs with blank lines</li>
                  <li>Use lists for step-by-step instructions</li>
                  <li>Include code examples in proper format</li>
                </ul>
                <p className="mt-2"><strong>Content:</strong></p>
                <ul className="list-disc list-inside space-y-1 ml-2">
                  <li>Be specific with technical details (dimension names, error codes)</li>
                  <li>Provide complete context (what, why, how)</li>
                  <li>Include concrete examples with actual values</li>
                  <li>Organize content with clear sections</li>
                </ul>
                <p className="mt-2 text-xs text-gray-500">💡 See <code>docs/KNOWLEDGE_BASE_BEST_PRACTICES.md</code> for detailed guidelines</p>
              </div>
            </details>
          </div>
          
          <div className="flex items-center gap-4">
            <label className="cursor-pointer">
              <input
                type="file"
                onChange={handleFileUpload}
                disabled={uploading}
                className="hidden"
                accept=".md,.txt,.pdf"
              />
              <span className={`px-5 py-2 text-sm font-medium rounded-md transition ${
                uploading
                  ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                  : 'bg-gray-900 text-white hover:bg-gray-800 cursor-pointer'
              }`}>
                {uploading ? 'Uploading...' : 'Choose File'}
              </span>
            </label>
            <span className="text-sm text-gray-500">
              Upload documents to staging folder (requires approval)
            </span>
          </div>
          {uploadSuccess && (
            <div className="mt-3 p-3 bg-green-50 border border-green-200 rounded text-green-700 text-sm">
              {uploadSuccess}
            </div>
          )}
        </div>

        {/* Tabs */}
        <div className="mb-6 border-b border-gray-200">
          <div className="flex gap-4">
            {(['pending', 'approved', 'rejected', 'all'] as Tab[]).map((tab) => (
              <button
                key={tab}
                onClick={() => setActiveTab(tab)}
                className={`px-4 py-2 font-medium text-sm border-b-2 transition ${
                  activeTab === tab
                    ? 'border-gray-900 text-gray-900'
                    : 'border-transparent text-gray-600 hover:text-gray-900'
                }`}
              >
                {tab.charAt(0).toUpperCase() + tab.slice(1)} ({tabCounts[tab]})
              </button>
            ))}
          </div>
        </div>

        {/* Error Message */}
        {error && (
          <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded text-sm text-red-700">
            {error}
          </div>
        )}

        {/* Document List */}
        {loading ? (
          <div className="text-center py-12 text-base text-gray-500">
            Loading documents...
          </div>
        ) : documents.length === 0 ? (
          <div className="text-center py-12 text-base text-gray-500">
            No documents in this category.
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            {documents.map((document) => (
              <AdminDocumentCard
                key={document.key}
                document={{
                  id: document.key,
                  name: document.name,
                  path: document.path,
                  uploadedAt: document.last_modified,
                  status: document.status || 'pending',
                }}
                onApprove={handleApprove}
                onReject={handleReject}
                onPreview={handlePreview}
              />
            ))}
          </div>
        )}

        {/* Footer Actions */}
        {activeTab === 'approved' && tabCounts.approved > 0 && (
          <div className="mt-6 pt-6 border-t border-gray-200">
            <button className="px-5 py-2 text-sm font-medium text-white bg-gray-900 rounded-md hover:bg-gray-800 transition">
              Run Ingestion on Approved Documents
            </button>
          </div>
        )}
      </Container>
    </div>
  );
};
