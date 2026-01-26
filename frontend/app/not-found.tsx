import Link from 'next/link';
import Container from '@/components/Container';

export default function NotFound() {
  return (
    <div className="min-h-screen bg-white flex items-center justify-center" style={{ paddingTop: '3.5rem' }}>
      <Container size="md">
        <div className="text-center">
          <h1 className="text-4xl font-semibold text-gray-900 mb-4">
            404
          </h1>
          <h2 className="text-2xl font-medium text-gray-700 mb-4">
            Page Not Found
          </h2>
          <p className="text-gray-600 mb-6">
            The page you're looking for doesn't exist.
          </p>
          <Link
            href="/"
            className="inline-block px-6 py-2 bg-gray-900 text-white rounded-full hover:bg-gray-700 transition"
          >
            Go back home
          </Link>
        </div>
      </Container>
    </div>
  );
}
