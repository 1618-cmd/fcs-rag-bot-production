/**
 * Tabs Navigation Component
 * 
 * Shared navigation tabs for Chat and Admin pages.
 */

'use client';

import { useState, useEffect } from 'react';
import { useRouter, usePathname } from 'next/navigation';
import { checkAuthStatus, logout, getAuthToken } from '@/lib/auth-api';

export default function TabsNavigation() {
  const router = useRouter();
  const pathname = usePathname();
  const [isAdmin, setIsAdmin] = useState(false);
  const [hasToken, setHasToken] = useState(false);
  const [mounted, setMounted] = useState(false);

  // Set mounted flag after component mounts (client-side only)
  useEffect(() => {
    setMounted(true);
  }, []);

  // Check if user is authenticated (and whether they are admin)
  useEffect(() => {
    const checkAdmin = async () => {
      const status = await checkAuthStatus();
      setIsAdmin(status.authenticated && status.role === 'admin');
      // Also check for token (client-side only)
      setHasToken(!!getAuthToken());
    };
    if (mounted) {
      checkAdmin();
    }
  }, [mounted, pathname]);

  const handleLogout = () => {
    logout();
    setIsAdmin(false);
    setHasToken(false);
    // Redirect to home after logout
    if (pathname?.startsWith('/admin') || pathname === '/chat') {
      router.push('/');
    }
  };

  const isHomePage = pathname === '/';
  const isAdminPage = pathname?.startsWith('/admin');

  const handleLoginClick = (e?: React.MouseEvent<HTMLButtonElement>) => {
    e?.preventDefault();
    e?.stopPropagation();
    console.log('Login button clicked, navigating to /login');
    try {
      router.push('/login?next=/chat');
    } catch (error) {
      console.error('Navigation error:', error);
      // Fallback to window.location if router fails
      if (typeof window !== 'undefined') {
        window.location.href = '/login?next=/chat';
      }
    }
  };

  const isAppArea = pathname === '/chat' || pathname?.startsWith('/admin');

  return (
    <div className="fixed top-0 left-0 right-0 w-full bg-white z-50">
      <div className="w-full px-4 flex items-center justify-between h-14">
        {!isAppArea ? (
          // Public header (Home + Login)
          <div className="flex gap-1 items-center flex-shrink-0">
            <button
              onClick={() => router.push('/')}
              className={`px-4 py-3 font-medium text-sm bg-white hover:bg-white border-0 outline-none transition-colors ${
                isHomePage
                  ? 'text-black'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Home
            </button>
          </div>
        ) : (
          // App header (Chat/Admin/Logout) - feels like a separate app surface
          <div className="flex gap-1 items-center flex-shrink-0">
            <button
              onClick={() => router.push('/chat')}
              className={`px-4 py-3 font-medium text-sm bg-white hover:bg-white border-0 outline-none transition-colors ${
                pathname === '/chat'
                  ? 'text-black'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              Chat
            </button>
            <button
              onClick={() => router.push('/admin/documents')}
              className={`px-4 py-3 font-medium text-sm bg-white hover:bg-white border-0 outline-none transition-colors ${
                isAdminPage
                  ? 'text-black'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
              style={{ display: isAdmin ? 'inline-flex' : 'none' }}
            >
              Admin
            </button>
          </div>
        )}
        {/* Login/Logout Button - Top Right */}
        <div className="flex items-center flex-shrink-0" style={{ marginRight: '2.5%', position: 'relative', zIndex: 100 }}>
          {!mounted ? (
            // Show login button immediately while checking auth status
            <button
              type="button"
              onClick={handleLoginClick}
              className="px-4 py-3 font-medium text-sm bg-white hover:bg-white border-0 outline-none transition-colors text-gray-600 hover:text-gray-900 cursor-pointer"
              style={{ position: 'relative', zIndex: 101 }}
            >
              Login
            </button>
          ) : hasToken ? (
            <button
              type="button"
              onClick={handleLogout}
              className="px-4 py-3 font-medium text-sm bg-white hover:bg-white border-0 outline-none transition-colors text-gray-600 hover:text-gray-900 cursor-pointer"
              style={{ position: 'relative', zIndex: 101 }}
            >
              Logout
            </button>
          ) : (
            <button
              type="button"
              onClick={handleLoginClick}
              className="px-4 py-3 font-medium text-sm bg-white hover:bg-white border-0 outline-none transition-colors text-gray-600 hover:text-gray-900 cursor-pointer"
              style={{ position: 'relative', zIndex: 101 }}
            >
              Login
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
