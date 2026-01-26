'use client';

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <html>
      <body>
        <div className="min-h-screen bg-white flex items-center justify-center">
          <div className="text-center p-8">
            <h1 className="text-2xl font-semibold text-gray-900 mb-4">
              Application Error
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
        </div>
      </body>
    </html>
  );
}
