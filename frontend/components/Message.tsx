'use client';

import { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { Source } from '@/lib/api';

interface MessageProps {
  role: 'user' | 'assistant';
  content: string;
  sources?: Source[];
  timestamp: Date;
  onCopy?: () => void;
  onFeedback?: (type: 'up' | 'down') => void;
  onRegenerate?: () => void;
  isLast?: boolean;
}

export default function Message({
  role,
  content,
  sources,
  timestamp,
  onCopy,
  onFeedback,
  onRegenerate,
  isLast = false,
}: MessageProps) {
  const [showCopyButton, setShowCopyButton] = useState(false);
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    if (onCopy) {
      await onCopy();
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const formatTimestamp = (date: Date) => {
    const now = new Date();
    const diff = now.getTime() - new Date(date).getTime();
    const minutes = Math.floor(diff / 60000);
    const hours = Math.floor(diff / 3600000);
    const days = Math.floor(diff / 86400000);

    if (minutes < 1) return 'Just now';
    if (minutes < 60) return `${minutes}m ago`;
    if (hours < 24) return `${hours}h ago`;
    if (days < 7) return `${days}d ago`;
    return new Date(date).toLocaleDateString();
  };

  if (role === 'user') {
    return (
      <div className="group w-full py-5 px-6 bg-[#F9FAFB]">
        <div className="max-w-[680px] mx-auto flex gap-3">
          <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gray-400 flex items-center justify-center">
            <span className="text-sm font-medium text-white">U</span>
          </div>
          <div className="flex-1 min-w-0">
            <div className="text-base leading-relaxed text-[#1F2937] whitespace-pre-wrap">
              {content}
            </div>
            <div className="mt-2 text-xs text-[#6B7280]">
              {formatTimestamp(timestamp)}
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div
      className="group w-full py-5 px-6 bg-white relative"
      onMouseEnter={() => setShowCopyButton(true)}
      onMouseLeave={() => setShowCopyButton(false)}
    >
      <div className="max-w-[680px] mx-auto flex gap-3">
        {/* Claude Avatar */}
        <div className="flex-shrink-0 w-8 h-8 rounded-full bg-[#D97757] flex items-center justify-center">
          <span className="text-sm font-medium text-white">C</span>
        </div>

        {/* Message Content */}
        <div className="flex-1 min-w-0">
          {/* Copy Button - Top Right */}
          {showCopyButton && onCopy && (
            <button
              onClick={handleCopy}
              className="absolute top-8 right-8 p-1.5 rounded-lg bg-white border border-gray-200 hover:bg-gray-50 transition-colors shadow-sm"
              aria-label={copied ? 'Copied!' : 'Copy message'}
            >
              {copied ? (
                <svg className="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
              ) : (
                <svg className="w-4 h-4 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
              )}
            </button>
          )}

          {/* Markdown Content */}
          <div className="prose prose-sm max-w-none">
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                code({ node, inline, className, children, ...props }) {
                  const match = /language-(\w+)/.exec(className || '');
                  return !inline && match ? (
                    <SyntaxHighlighter
                      style={vscDarkPlus}
                      language={match[1]}
                      PreTag="div"
                      className="rounded-lg my-4"
                      {...props}
                    >
                      {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                  ) : (
                    <code className="px-1.5 py-0.5 bg-gray-100 rounded text-sm font-mono text-[#1F2937]" {...props}>
                      {children}
                    </code>
                  );
                },
                a({ node, ...props }) {
                  return (
                    <a
                      className="text-[#3B82F6] underline hover:text-[#2563EB]"
                      {...props}
                    />
                  );
                },
                blockquote({ node, ...props }) {
                  return (
                    <blockquote
                      className="border-l-4 border-gray-300 pl-4 my-4 italic text-[#6B7280]"
                      {...props}
                    />
                  );
                },
                h1({ node, ...props }) {
                  return <h1 className="text-xl font-semibold text-[#1F2937] mt-6 mb-3" {...props} />;
                },
                h2({ node, ...props }) {
                  return <h2 className="text-lg font-semibold text-[#1F2937] mt-5 mb-2" {...props} />;
                },
                h3({ node, ...props }) {
                  return <h3 className="text-base font-semibold text-[#1F2937] mt-4 mb-2" {...props} />;
                },
                ul({ node, ...props }) {
                  return <ul className="list-disc list-inside my-3 space-y-1 text-[#1F2937]" {...props} />;
                },
                ol({ node, ...props }) {
                  return <ol className="list-decimal list-inside my-3 space-y-1 text-[#1F2937]" {...props} />;
                },
                p({ node, ...props }) {
                  return <p className="mb-3 text-[#1F2937] leading-relaxed" {...props} />;
                },
                strong({ node, ...props }) {
                  return <strong className="font-semibold text-[#1F2937]" {...props} />;
                },
                em({ node, ...props }) {
                  return <em className="italic" {...props} />;
                },
              }}
            >
              {content}
            </ReactMarkdown>
          </div>

          {/* Sources */}
          {sources && sources.length > 0 && (
            <div className="mt-4 pt-4 border-t border-gray-200">
              <p className="text-xs font-medium text-[#6B7280] mb-2">Sources:</p>
              <div className="flex flex-wrap gap-2">
                {sources.map((source, idx) => {
                  // Clean up source name - remove Windows paths and extract just the document name
                  const cleanSourceName = source.name
                    .replace(/^.*[\\/]knowledge_base[\\/]?/i, '') // Remove path up to knowledge_base
                    .replace(/^C:[\\/].*?[\\/]knowledge_base[\\/]?/i, '') // Remove full Windows path
                    .replace(/\\/g, '/') // Convert backslashes to forward slashes
                    .replace(/\.(md|txt|pdf)$/i, '') // Remove file extensions
                    .replace(/^[\\/]+/, '') // Remove leading slashes
                    || source.name; // Fallback to original if cleaning fails
                  
                  return (
                    <span
                      key={idx}
                      className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium bg-gray-100 text-[#6B7280]"
                      title={source.name} // Show full path on hover
                    >
                      {cleanSourceName}
                    </span>
                  );
                })}
              </div>
            </div>
          )}

          {/* Feedback & Regenerate Buttons */}
          <div className="mt-4 flex items-center gap-3 opacity-0 group-hover:opacity-100 transition-opacity">
            {onFeedback && (
              <>
                <button
                  onClick={() => onFeedback('up')}
                  className="p-1.5 rounded-lg hover:bg-gray-100 transition-colors"
                  aria-label="Thumbs up"
                >
                  <svg className="w-4 h-4 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                  </svg>
                </button>
                <button
                  onClick={() => onFeedback('down')}
                  className="p-1.5 rounded-lg hover:bg-gray-100 transition-colors"
                  aria-label="Thumbs down"
                >
                  <svg className="w-4 h-4 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 14H5.236a2 2 0 01-1.789-2.894l3.5-7A2 2 0 018.736 3h4.018a2 2 0 01.485.06l3.76.94m-7 10v5a2 2 0 002 2h.096c.5 0 .905-.405.905-.904 0-.715.211-1.413.608-2.008L17 13V4m-7 10h2m5-10h2a2 2 0 012 2v6a2 2 0 01-2 2h-2.5" />
                  </svg>
                </button>
              </>
            )}
            {isLast && onRegenerate && (
              <button
                onClick={onRegenerate}
                className="px-3 py-1.5 text-sm text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
              >
                Regenerate
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
