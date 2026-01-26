/**
 * Chat Component - Production-ready with markdown rendering
 */
'use client';
import { useState } from 'react';
import Container from './Container';
import ChatMessage from './ChatMessage';
import { queryRAG, QueryResponse, Source } from '@/lib/api';

interface Message {
  role: string;
  content: string;
  sources?: Source[];
}

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedProvider, setSelectedProvider] = useState<'openai' | 'anthropic' | undefined>(undefined);

  const handleSend = async () => {
    if (!input.trim() || isLoading) return;
    
    const userMessage = input.trim();
    setMessages([...messages, { role: 'user', content: userMessage }]);
    setInput('');
    setIsLoading(true);
    
    try {
      // Call the backend RAG API with selected provider
      const response: QueryResponse = await queryRAG(userMessage, false, selectedProvider);
      
      // Add assistant response to messages with sources
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: response.answer,
        sources: response.sources
      }]);
      
    } catch (error) {
      console.error('Error:', error);
      // Show error message to user
      const errorMessage = error instanceof Error 
        ? error.message 
        : 'Sorry, I encountered an error processing your request.';
      
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: errorMessage 
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-white flex flex-col" style={{ paddingTop: '3.5rem' }}>
      
      {/* EMPTY STATE - Input centered in middle */}
      {messages.length === 0 && (
        <div 
          className="flex-1 flex flex-col items-center justify-center px-6"
          style={{ minHeight: 'calc(100vh - 3.5rem)' }}
        >
          {/* Welcome Message */}
          <div className="text-center mb-12">
            <h1 className="text-4xl font-semibold text-gray-900 mb-4">
              What's on the agenda today?
            </h1>
            <p className="text-base text-gray-600">
              Ask me anything about the Vena platform
            </p>
          </div>
          
          {/* Model Selector */}
          <div className="mb-6">
            <Container size="md">
              <div className="flex items-center gap-4 justify-center">
                <span className="text-sm text-gray-600">Model:</span>
                <div className="flex gap-2">
                  <button
                    onClick={() => setSelectedProvider('openai')}
                    className={`px-4 py-2 rounded-full text-sm font-medium transition ${
                      selectedProvider === 'openai'
                        ? 'bg-gray-900 text-white'
                        : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                    }`}
                  >
                    GPT-4o
                  </button>
                  <button
                    onClick={() => setSelectedProvider('anthropic')}
                    className={`px-4 py-2 rounded-full text-sm font-medium transition ${
                      selectedProvider === 'anthropic'
                        ? 'bg-gray-900 text-white'
                        : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                    }`}
                  >
                    Claude 3.5
                  </button>
                  <button
                    onClick={() => setSelectedProvider(undefined)}
                    className={`px-4 py-2 rounded-full text-sm font-medium transition ${
                      selectedProvider === undefined
                        ? 'bg-gray-900 text-white'
                        : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                    }`}
                  >
                    Default
                  </button>
                </div>
              </div>
            </Container>
          </div>
          
          {/* Input Box - Centered, Clean ChatGPT style */}
          <Container size="md">
            <div className="relative flex items-center bg-gray-100 rounded-full px-4 hover:bg-gray-200 transition">
              
              {/* Text Input */}
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    handleSend();
                  }
                }}
                placeholder="Ask anything"
                className="flex-1 py-4 bg-transparent text-base text-gray-900 placeholder-gray-500 focus:outline-none"
                style={{ paddingTop: '1rem', paddingBottom: '1rem' }}
              />
              
              {/* Send Button - Circular */}
              <button
                onClick={handleSend}
                disabled={!input.trim() || isLoading}
                className="p-2 rounded-full bg-gray-900 hover:bg-gray-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition flex items-center justify-center"
              >
                <svg 
                  width="20" 
                  height="20" 
                  viewBox="0 0 24 24" 
                  fill="none" 
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  className="text-white"
                >
                  <path d="M12 19V5M5 12l7-7 7 7"/>
                </svg>
              </button>
              
            </div>
          </Container>
        </div>
      )}
      
      {/* CHAT STATE - Input fixed at bottom */}
      {messages.length > 0 && (
        <>
          {/* Messages Area - Scrollable */}
          <div className="flex-1 overflow-y-auto" style={{ paddingBottom: '180px' }}>
            <Container size="md">
              <div className="py-8 overflow-x-hidden">
                {messages.map((message, index) => (
                  <ChatMessage
                    key={index}
                    message={message}
                    onFeedback={(feedback) => {
                      console.log(`Feedback for message ${index}: ${feedback}`);
                      // TODO: Send feedback to API
                    }}
                    onCreateTicket={() => {
                      console.log(`Create ticket for message ${index}`);
                      // TODO: Implement Jira ticket creation
                    }}
                  />
                ))}
                
                {/* Thinking Indicator */}
                {isLoading && (
                  <div className="flex items-center gap-2 text-gray-600 mb-8">
                    <div className="flex gap-1">
                      <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></span>
                      <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></span>
                      <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></span>
                    </div>
                    <span className="text-sm">FCS - Alex is thinking...</span>
                  </div>
                )}
              </div>
            </Container>
          </div>
          
          {/* Model Selector - Fixed at bottom above input */}
          <div 
            className="fixed left-0 right-0 bg-white border-t border-gray-200 py-3"
            style={{ 
              bottom: '72px', 
              left: 0, 
              right: 0, 
              zIndex: 40,
              backgroundColor: '#ffffff',
              boxShadow: '0 -1px 0 0 rgba(0,0,0,0.05)'
            }}
          >
            <Container size="md">
              <div className="flex items-center gap-4 justify-center">
                <span className="text-sm text-gray-600">Model:</span>
                <div className="flex gap-2">
                  <button
                    onClick={() => setSelectedProvider('openai')}
                    disabled={isLoading}
                    className={`px-4 py-1.5 rounded-full text-sm font-medium transition ${
                      selectedProvider === 'openai'
                        ? 'bg-gray-900 text-white'
                        : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                    } disabled:opacity-50 disabled:cursor-not-allowed`}
                  >
                    GPT-4o
                  </button>
                  <button
                    onClick={() => setSelectedProvider('anthropic')}
                    disabled={isLoading}
                    className={`px-4 py-1.5 rounded-full text-sm font-medium transition ${
                      selectedProvider === 'anthropic'
                        ? 'bg-gray-900 text-white'
                        : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                    } disabled:opacity-50 disabled:cursor-not-allowed`}
                  >
                    Claude 3.5
                  </button>
                  <button
                    onClick={() => setSelectedProvider(undefined)}
                    disabled={isLoading}
                    className={`px-4 py-1.5 rounded-full text-sm font-medium transition ${
                      selectedProvider === undefined
                        ? 'bg-gray-900 text-white'
                        : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                    } disabled:opacity-50 disabled:cursor-not-allowed`}
                  >
                    Default
                  </button>
                </div>
              </div>
            </Container>
          </div>
          
          {/* Input Box - Fixed at Bottom, Clean ChatGPT style */}
          <div 
            className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 py-6"
            style={{ 
              bottom: 0, 
              left: 0, 
              right: 0, 
              zIndex: 50,
              backgroundColor: '#ffffff',
              paddingTop: '1.5rem',
              paddingBottom: '1.5rem'
            }}
          >
            <Container size="md">
              <div className="relative flex items-center bg-gray-100 rounded-full px-4 hover:bg-gray-200 transition">
                
                {/* Text Input */}
                <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' && !e.shiftKey) {
                      e.preventDefault();
                      handleSend();
                    }
                  }}
                  placeholder="Ask anything"
                  disabled={isLoading}
                  className="flex-1 py-4 bg-transparent text-base text-gray-900 placeholder-gray-500 focus:outline-none disabled:cursor-not-allowed"
                  style={{ paddingTop: '1rem', paddingBottom: '1rem' }}
                />
                
                {/* Send Button - Circular */}
                <button
                  onClick={handleSend}
                  disabled={!input.trim() || isLoading}
                  className="p-2 rounded-full bg-gray-900 hover:bg-gray-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition flex items-center justify-center"
                >
                  <svg 
                    width="20" 
                    height="20" 
                    viewBox="0 0 24 24" 
                    fill="none" 
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    className="text-white"
                  >
                    <path d="M12 19V5M5 12l7-7 7 7"/>
                  </svg>
                </button>
                
              </div>
            </Container>
          </div>
        </>
      )}
      
    </div>
  );
}
