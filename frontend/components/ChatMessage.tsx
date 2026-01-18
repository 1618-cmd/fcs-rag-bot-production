'use client';
import { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import CodeBlock from './CodeBlock';
import { Source } from '@/lib/api';

interface ChatMessageProps {
  message: {
    role: string;
    content: string;
    sources?: Source[];
  };
  onFeedback?: (feedback: 'positive' | 'negative') => void;
  onCreateTicket?: () => void;
}

export default function ChatMessage({ message, onFeedback, onCreateTicket }: ChatMessageProps) {
  const [copied, setCopied] = useState(false);
  const [feedbackGiven, setFeedbackGiven] = useState<'positive' | 'negative' | null>(null);

  const handleCopyMessage = async () => {
    await navigator.clipboard.writeText(message.content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleFeedback = (type: 'positive' | 'negative') => {
    setFeedbackGiven(type);
    onFeedback?.(type);
  };

  if (message.role === 'user') {
    return (
      <div className="flex justify-end mb-6">
        <div className="bg-gray-100 rounded-2xl px-5 py-3 max-w-[80%]">
          <p className="text-base text-gray-900 whitespace-pre-wrap">{message.content}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="mb-8">
      {/* Assistant Message Content */}
      <div className="prose prose-gray max-w-none">
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          components={{
            // Handle pre tags (block-level code) - this prevents nesting issues
            pre: ({ children, ...props }: any) => {
              // ReactMarkdown passes a code element as children
              // Extract from React.ReactElement
              if (children && typeof children === 'object' && 'props' in children) {
                const codeProps = children.props;
                if (codeProps && codeProps.className) {
                  const match = /language-(\w+)/.exec(codeProps.className || '');
                  const language = match ? match[1] : undefined;
                  const value = String(codeProps.children || codeProps.children[0] || '').replace(/\n$/, '');
                  
                  // Render our custom CodeBlock component (returns div)
                  return <CodeBlock language={language} value={value} />;
                }
              }
              // Fallback to default pre rendering
              return <pre {...props}>{children}</pre>;
            },
            // Custom inline code rendering
            code({ node, inline, className, children, ...props }: any) {
              // This should only handle inline code now
              if (inline) {
                return (
                  <code className="bg-gray-100 text-red-600 px-1.5 py-0.5 rounded text-sm font-mono" {...props}>
                    {children}
                  </code>
                );
              }
              // Block-level code is handled by 'pre' component above
              return null;
            },
            // Style paragraphs - check if it contains a code block to avoid nesting
            p: ({ children, ...props }: any) => {
              // Check if children contains a pre/code block (which will render as div)
              if (children && Array.isArray(children)) {
                const hasCodeBlock = children.some((child: any) => 
                  child && typeof child === 'object' && 
                  (child.type?.name === 'CodeBlock' || child.type === 'pre' || (child.props && child.props.className && child.props.className.includes('language-')))
                );
                
                if (hasCodeBlock) {
                  // Don't wrap code blocks in <p> tags
                  return <>{children}</>;
                }
              }
              
              // Normal paragraph
              return (
                <p className="text-base text-gray-900 leading-relaxed my-3" {...props}>
                  {children}
                </p>
              );
            },
            // Style headers
            h2: ({ children }) => (
              <h2 className="text-xl font-semibold text-gray-900 mt-6 mb-3">{children}</h2>
            ),
            h3: ({ children }) => (
              <h3 className="text-lg font-semibold text-gray-900 mt-4 mb-2">{children}</h3>
            ),
            // Style lists
            ul: ({ children }) => (
              <ul className="list-disc list-inside space-y-1 my-3">{children}</ul>
            ),
            ol: ({ children }) => (
              <ol className="list-decimal list-inside space-y-1 my-3">{children}</ol>
            ),
            // Style blockquotes
            blockquote: ({ children }: any) => (
              <blockquote className="border-l-4 border-blue-500 bg-blue-50 pl-4 py-2 my-3 italic">
                {children}
              </blockquote>
            ),
            // Style tables
            table: ({ children }) => (
              <div className="overflow-x-auto my-4">
                <table className="min-w-full border-collapse border border-gray-300">
                  {children}
                </table>
              </div>
            ),
            th: ({ children }) => (
              <th className="border border-gray-300 bg-gray-100 px-4 py-2 text-left font-semibold">
                {children}
              </th>
            ),
            td: ({ children }) => (
              <td className="border border-gray-300 px-4 py-2">{children}</td>
            ),
          }}
        >
          {message.content}
        </ReactMarkdown>
      </div>

      {/* Source Citations */}
      {message.sources && message.sources.length > 0 && (
        <div className="mt-4 pt-4 border-t border-gray-200">
          <p className="text-xs font-medium text-gray-600 mb-2">Sources:</p>
          <div className="flex flex-wrap gap-2">
            {message.sources.map((source, idx) => {
              // Clean up source name - remove Windows paths and extract just the document name
              const cleanSourceName = source.name
                .replace(/^.*[\\/]knowledge_base[\\/]?/i, '')
                .replace(/^C:[\\/].*?[\\/]knowledge_base[\\/]?/i, '')
                .replace(/\\/g, '/')
                .replace(/\.(md|txt|pdf)$/i, '')
                .replace(/^[\\/]+/, '')
                || source.name;
              
              return (
                <span
                  key={idx}
                  className="text-xs px-2 py-1 bg-gray-100 text-gray-700 rounded"
                  title={source.name}
                >
                  {cleanSourceName}
                </span>
              );
            })}
          </div>
        </div>
      )}

      {/* Message Actions */}
      <div className="flex items-center gap-3 mt-4">
        {/* Copy Button */}
        <button
          onClick={handleCopyMessage}
          className="text-sm text-gray-600 hover:text-gray-900 transition flex items-center gap-1"
          title="Copy message"
        >
          {copied ? (
            <>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <polyline points="20 6 9 17 4 12" />
              </svg>
              Copied!
            </>
          ) : (
            <>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
              </svg>
              Copy
            </>
          )}
        </button>

        {/* Feedback Buttons */}
        <div className="flex items-center gap-1 border-l border-gray-300 pl-3">
          <button
            onClick={() => handleFeedback('positive')}
            className={`p-1 rounded transition ${
              feedbackGiven === 'positive'
                ? 'text-green-600 bg-green-50'
                : 'text-gray-600 hover:text-green-600 hover:bg-green-50'
            }`}
            title="Good response"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3" />
            </svg>
          </button>
          <button
            onClick={() => handleFeedback('negative')}
            className={`p-1 rounded transition ${
              feedbackGiven === 'negative'
                ? 'text-red-600 bg-red-50'
                : 'text-gray-600 hover:text-red-600 hover:bg-red-50'
            }`}
            title="Bad response"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17" />
            </svg>
          </button>
        </div>

        {/* Create Jira Ticket */}
        {onCreateTicket && (
          <button
            onClick={onCreateTicket}
            className="text-sm text-gray-600 hover:text-gray-900 transition flex items-center gap-1 border-l border-gray-300 pl-3"
            title="Create Jira ticket"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
              <polyline points="14 2 14 8 20 8" />
              <line x1="12" y1="18" x2="12" y2="12" />
              <line x1="9" y1="15" x2="15" y2="15" />
            </svg>
            Create Ticket
          </button>
        )}
      </div>
    </div>
  );
}
