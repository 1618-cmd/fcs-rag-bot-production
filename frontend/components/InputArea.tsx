'use client';

import { useRef, useEffect, useState } from 'react';

interface InputAreaProps {
  value: string;
  onChange: (value: string) => void;
  onSubmit: () => void;
  isLoading: boolean;
  onStop?: () => void;
}

export default function InputArea({ value, onChange, onSubmit, isLoading, onStop }: InputAreaProps) {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [isFocused, setIsFocused] = useState(false);

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      const height = Math.min(textareaRef.current.scrollHeight, 200);
      textareaRef.current.style.height = `${height}px`;
    }
  }, [value]);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      if (!isLoading && value.trim()) {
        onSubmit();
      }
    }
  };

  const canSend = value.trim().length > 0 && !isLoading;

  return (
    <div className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 z-40">
      <div className="max-w-[768px] mx-auto px-5 py-4">
        <div className="relative flex items-end gap-3">
          {/* Attachment Button */}
          <button
            className="p-2 rounded-lg hover:bg-gray-100 transition-colors flex-shrink-0"
            aria-label="Attach file"
          >
            <svg className="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
            </svg>
          </button>

          {/* Textarea */}
          <div className="flex-1 relative">
            <textarea
              ref={textareaRef}
              value={value}
              onChange={(e) => onChange(e.target.value)}
              onKeyDown={handleKeyDown}
              onFocus={() => setIsFocused(true)}
              onBlur={() => setIsFocused(false)}
                  placeholder="Ask a question about Vena..."
              rows={1}
              className={`
                w-full px-4 py-3.5 pr-12
                border rounded-xl
                resize-none
                text-base text-[#1F2937]
                placeholder:text-gray-400
                focus:outline-none focus:ring-2 focus:ring-[#3B82F6] focus:border-transparent
                transition-all
                ${isFocused ? 'border-gray-400 shadow-sm' : 'border-gray-300'}
              `}
              style={{ minHeight: '52px', maxHeight: '200px' }}
            />
          </div>

          {/* Send/Stop Button */}
          {isLoading && onStop ? (
            <button
              onClick={onStop}
              className="p-3 rounded-xl bg-gray-200 text-gray-700 hover:bg-gray-300 transition-colors flex-shrink-0"
              aria-label="Stop generating"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          ) : (
            <button
              onClick={onSubmit}
              disabled={!canSend}
              className={`
                p-3 rounded-xl transition-all flex-shrink-0
                ${canSend
                  ? 'bg-[#D97757] text-white hover:bg-[#C4694A] shadow-sm hover:shadow-md'
                  : 'bg-gray-200 text-gray-400 cursor-not-allowed'
                }
              `}
              aria-label="Send message"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
              </svg>
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
