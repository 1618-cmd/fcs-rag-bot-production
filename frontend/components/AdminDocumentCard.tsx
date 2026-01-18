/**
 * Admin Document Card Component - Visual Mockup/Implementation
 * 
 * This component represents a single document card in the approval UI.
 * Shows document information and approve/reject actions.
 */

import React from 'react';

interface Document {
  id: string;
  name: string;
  path: string;
  uploadedAt: string;
  uploadedBy?: string;
  status: 'pending' | 'approved' | 'rejected';
}

interface AdminDocumentCardProps {
  document: Document;
  onApprove: (id: string) => void;
  onReject: (id: string, reason?: string) => void;
  onPreview: (id: string) => void;
}

export const AdminDocumentCard: React.FC<AdminDocumentCardProps> = ({
  document,
  onApprove,
  onReject,
  onPreview,
}) => {
  return (
    <div className="border border-gray-300 rounded-lg p-4 bg-white shadow-sm hover:shadow-md transition-shadow">
      {/* Document Icon and Title */}
      <div className="flex items-start gap-3 mb-3">
        <div className="text-2xl">📄</div>
        <div className="flex-1">
          <h3 className="font-semibold text-lg text-gray-900 mb-1">
            {document.name}
          </h3>
          <p className="text-sm text-gray-600 font-mono">
            {document.path}
          </p>
        </div>
      </div>

      {/* Metadata */}
      <div className="text-sm text-gray-500 mb-4 space-y-1">
        <div>
          <span className="font-medium">Uploaded:</span> {document.uploadedAt}
        </div>
        {document.uploadedBy && (
          <div>
            <span className="font-medium">Uploader:</span> {document.uploadedBy}
          </div>
        )}
      </div>

      {/* Action Buttons */}
      <div className="flex gap-2 pt-3 border-t border-gray-200 flex-wrap">
        <button
          onClick={() => onPreview(document.id)}
          className="px-3 py-1.5 text-sm font-medium text-gray-700 bg-gray-100 hover:bg-gray-200 rounded border border-gray-300 transition-colors"
        >
          Preview Content
        </button>
        
        {document.status === 'pending' && (
          <>
            <button
              onClick={() => onApprove(document.id)}
              className="px-4 py-1.5 text-sm font-medium text-white bg-green-600 hover:bg-green-700 rounded transition-colors flex items-center gap-1"
            >
              <span>✓</span> Approve
            </button>
            
            <button
              onClick={() => {
                const reason = prompt('Rejection reason (optional):');
                onReject(document.id, reason || undefined);
              }}
              className="px-4 py-1.5 text-sm font-medium text-white bg-red-600 hover:bg-red-700 rounded transition-colors flex items-center gap-1"
            >
              <span>✗</span> Reject
            </button>
          </>
        )}

        {document.status === 'approved' && (
          <span className="px-3 py-1.5 text-sm font-medium text-green-700 bg-green-50 rounded border border-green-200">
            ✓ Approved
          </span>
        )}

        {document.status === 'rejected' && (
          <span className="px-3 py-1.5 text-sm font-medium text-red-700 bg-red-50 rounded border border-red-200">
            ✗ Rejected
          </span>
        )}
      </div>
    </div>
  );
};
