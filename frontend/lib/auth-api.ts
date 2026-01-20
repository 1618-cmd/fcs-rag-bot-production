/**
 * Authentication API client.
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  success: boolean;
  token: string;
  message: string;
}

export interface AuthStatus {
  authenticated: boolean;
  email?: string;
  role?: string;
  user_id?: string;
}

/**
 * Login with email and password.
 */
export async function login(email: string, password: string): Promise<string> {
  const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'Login failed');
  }

  const data: LoginResponse = await response.json();
  
  // Store token in localStorage
  if (typeof window !== 'undefined') {
    localStorage.setItem('auth_token', data.token);
  }
  
  return data.token;
}

/**
 * Logout (remove token from localStorage).
 */
export function logout(): void {
  if (typeof window !== 'undefined') {
    localStorage.removeItem('auth_token');
  }
}

/**
 * Get authentication token from localStorage.
 */
export function getAuthToken(): string | null {
  if (typeof window !== 'undefined') {
    return localStorage.getItem('auth_token');
  }
  return null;
}

/**
 * Check authentication status.
 */
export async function checkAuthStatus(): Promise<AuthStatus> {
  const token = getAuthToken();
  if (!token) {
    return { authenticated: false };
  }

  try {
    const response = await fetch(`${API_BASE_URL}/api/auth/status`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      return { authenticated: false };
    }

    const data: AuthStatus = await response.json();
    return data;
  } catch (error) {
    return { authenticated: false };
  }
}
