"""
API middleware modules.
"""

# Export middleware classes for easier imports
try:
    from .sentry_middleware import SentryUserContextMiddleware
    from .auth_middleware import AuthMiddleware
    __all__ = ['SentryUserContextMiddleware', 'AuthMiddleware']
except ImportError:
    # If imports fail, define empty __all__ to prevent errors
    __all__ = []
