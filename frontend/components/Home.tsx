/**
 * Home Landing Page Component
 * 
 * ChatGPT-style landing page - using inline styles for width constraints
 */
'use client';
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter();

  const handleGetStarted = () => {
    router.push('/chat');
  };

  return (
    <div className="min-h-screen bg-white" style={{ paddingTop: 'calc(3.5rem + 5rem)' }}>
      
      {/* Date label */}
      <div className="text-center text-sm text-gray-500 mb-6">
        {new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}
      </div>
      
      {/* Title - using inline max-width */}
      <div style={{ maxWidth: '768px', margin: '0 auto', padding: '0 24px', marginBottom: '24px' }}>
        <h1 className="text-5xl font-semibold text-gray-900 text-center leading-tight">
          Introducing FCS - Alex
        </h1>
      </div>
      
      {/* Button - centered */}
      <div className="text-center mb-12">
        <button 
          onClick={handleGetStarted}
          className="px-5 py-2 text-sm font-medium text-gray-900 border border-gray-300 hover:bg-gray-50 rounded-md transition"
        >
          Get Started - Start Chatting
        </button>
      </div>
      
      {/* Text content - INLINE STYLES for width */}
      <div style={{ maxWidth: '672px', margin: '0 auto', padding: '0 24px' }}>
        <p className="text-base text-gray-900 leading-relaxed text-center mb-6">
          We've built a RAG (Retrieval Augmented Generation) bot called FCS - Alex which provides intelligent technical support for the Vena financial consolidation platform. The system combines a comprehensive knowledge base with advanced language models to deliver accurate, context-aware answers to your questions.
        </p>
        
        <p className="text-base text-gray-900 leading-relaxed text-center mb-6">
          FCS - Alex is powered by OpenAI's GPT-4o and uses semantic search to retrieve relevant documentation from our knowledge base, ensuring responses are grounded in verified information. The system can answer follow-up questions, provide step-by-step instructions for Workbook tasks, assist with configuration tasks, and help users across different roles—from Contributors to Modelers to Administrators.
        </p>
        
        <p className="text-base text-gray-900 leading-relaxed text-center">
          We're excited to introduce FCS - Alex to help streamline technical support and improve productivity. The system includes source citations, anti-hallucination safeguards, and the ability to create Jira tickets when needed. Start chatting now to experience AI-powered support for your Vena platform questions.
        </p>
      </div>
      
    </div>
  );
}
