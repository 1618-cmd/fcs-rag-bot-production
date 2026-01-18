/**
 * Tabs Navigation Component
 * 
 * Shared navigation tabs for Chat and Admin pages.
 */

'use client';

import { useState, useEffect } from 'react';
import { useRouter, usePathname } from 'next/navigation';
import { checkAuthStatus, logout, getAuthToken, login } from '@/lib/auth-api';

export default function TabsNavigation() {
  const router = useRouter();
  const pathname = usePathname();
  const [isAdmin, setIsAdmin] = useState(false);
  const [hasToken, setHasToken] = useState(false);
  const [mounted, setMounted] = useState(false);
  const [showLoginModal, setShowLoginModal] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loginLoading, setLoginLoading] = useState(false);
  const [loginError, setLoginError] = useState<string | null>(null);

  // Set mounted flag after component mounts (client-side only)
  useEffect(() => {
    setMounted(true);
  }, []);

  // Check if user is authenticated as admin
  useEffect(() => {
    const checkAdmin = async () => {
      const status = await checkAuthStatus();
      setIsAdmin(status.authenticated);
      // Also check for token (client-side only)
      setHasToken(!!getAuthToken());
    };
    if (mounted) {
      checkAdmin();
    }
  }, [mounted]);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoginLoading(true);
    setLoginError(null);

    try {
      const token = await login(email, password);
      // Refresh auth status after login
      const status = await checkAuthStatus();
      setIsAdmin(status.authenticated);
      setHasToken(!!token);
      setShowLoginModal(false);
      setEmail('');
      setPassword('');
    } catch (err) {
      setLoginError(err instanceof Error ? err.message : 'Login failed');
    } finally {
      setLoginLoading(false);
    }
  };

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
  const isChatPage = pathname === '/chat';
  const isAdminPage = pathname?.startsWith('/admin');

  return (
    <div className="fixed top-0 left-0 right-0 w-full bg-white z-50">
      <div className="w-full px-4 flex items-center justify-between h-14">
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
          <button
            onClick={() => router.push('/chat')}
            className={`px-4 py-3 font-medium text-sm bg-white hover:bg-white border-0 outline-none transition-colors ${
              isChatPage
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
          >
            Admin
          </button>
        </div>
        {/* Login/Logout Button - Top Right */}
        <div className="flex items-center flex-shrink-0" style={{ marginRight: '2.5%' }}>
          {mounted && (isAdmin || hasToken ? (
                <button
                  onClick={handleLogout}
                  className="px-4 py-3 font-medium text-sm bg-white hover:bg-white border-0 outline-none transition-colors text-gray-600 hover:text-gray-900"
                >
                  Logout
                </button>
              ) : (
                <>
                  <button
                    onClick={() => setShowLoginModal(true)}
                    className="px-4 py-3 font-medium text-sm bg-white hover:bg-white border-0 outline-none transition-colors text-gray-600 hover:text-gray-900"
                  >
                    Login
                  </button>
                  
                  {/* Login Modal */}
                  {showLoginModal && (
                    <>
                      {/* Backdrop */}
                      <div 
                        className="fixed inset-0 bg-black bg-opacity-50 z-40"
                        onClick={() => setShowLoginModal(false)}
                      />
                      {/* Modal */}
                      <div className="fixed inset-0 flex items-center justify-center z-50">
                        <div 
                          className="bg-white rounded-lg shadow-xl p-8 max-w-md w-full mx-4"
                          onClick={(e) => e.stopPropagation()}
                        >
                          <h2 className="text-2xl font-semibold text-gray-900 mb-6">
                            Login
                          </h2>
                          
                          <form onSubmit={handleLogin} className="space-y-4">
                            {loginError && (
                              <div className="p-3 bg-red-50 border border-red-200 rounded text-red-700 text-sm">
                                {loginError}
                              </div>
                            )}

                            <div>
                              <label htmlFor="modal-email" className="block text-sm font-medium text-gray-700 mb-1">
                                Email
                              </label>
                              <input
                                id="modal-email"
                                type="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                placeholder="admin@example.com"
                                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                required
                              />
                            </div>

                            <div>
                              <label htmlFor="modal-password" className="block text-sm font-medium text-gray-700 mb-1">
                                Password
                              </label>
                              <input
                                id="modal-password"
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                placeholder="Enter your password"
                                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                required
                              />
                            </div>

                            <div className="flex gap-3">
                              <button
                                type="button"
                                onClick={() => {
                                  setShowLoginModal(false);
                                  setLoginError(null);
                                  setEmail('');
                                  setPassword('');
                                }}
                                className="flex-1 px-4 py-2 border border-gray-300 text-gray-700 font-medium rounded-lg hover:bg-gray-50 transition-colors"
                              >
                                Cancel
                              </button>
                              <button
                                type="submit"
                                disabled={loginLoading}
                                className="flex-1 px-4 py-2 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
                              >
                                {loginLoading ? 'Logging in...' : 'Login'}
                              </button>
                            </div>
                          </form>
                        </div>
                      </div>
                    </>
                  )}
                </>
              ))}
        </div>
      </div>
    </div>
  );
}
