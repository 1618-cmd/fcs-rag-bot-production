'use client';

import { useEffect } from 'react';
import Container from '@/components/Container';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error('Application error:', error);
  }, [error]);

  return (
    <div className="min-h-screen bg-white flex items-center justify-center" style={{ paddingTop: '3.5rem' }}>
      <Container size="md">
        <div className="text-center">
          <h1 className="text-2xl font-semibold text-gray-900 mb-4">
            Something went wrong
          </h1>
          <p className="text-gray-600 mb-6">
            {error.message || 'An unexpected error occurred'}
          </p>
          <button
            onClick={reset}
            className="px-6 py-2 bg-gray-900 text-white rounded-full hover:bg-gray-700 transition"
          >
            Try again
          </button>
        </div>
      </Container>
    </div>
  );
}
