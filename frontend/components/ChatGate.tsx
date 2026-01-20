/**
 * ChatGate
 *
 * Ensures Chat behaves like ChatGPT: Home is separate/public, and Chat is the entry
 * point for authentication. If no auth token is present, redirect to /login.
 */

'use client';

import { useEffect, useState } from 'react';
import { usePathname, useRouter } from 'next/navigation';
import { getAuthToken } from '@/lib/auth-api';

export default function ChatGate({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const [ready, setReady] = useState(false);
  const [checking, setChecking] = useState(true);

  useEffect(() => {
    const token = getAuthToken();
    if (!token) {
      const next = pathname || '/chat';
      router.replace(`/login?next=${encodeURIComponent(next)}`);
      return;
    }
    setReady(true);
    setChecking(false);
  }, [pathname, router]);

  if (!ready) {
    // Avoid a blank screen while checking auth / redirecting.
    return (
      <div className="min-h-screen bg-white flex items-center justify-center" style={{ paddingTop: '3.5rem' }}>
        <div className="text-sm text-gray-500">{checking ? 'Loading…' : 'Redirecting…'}</div>
      </div>
    );
  }
  return <>{children}</>;
}

