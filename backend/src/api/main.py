"""
FastAPI application for Vena RAG Bot Production.

Main entry point for the API server.
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from ..utils.config import settings, validate_settings
from ..utils.logging_config import setup_logging
from ..services.rate_limiter import get_limiter, rate_limit_handler
from .routes import query, health, ingestion, jira, admin, auth, users

# Set up logging
setup_logging(log_level=settings.log_level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown."""
    # Initialize Sentry early (before other initialization)
    if settings.sentry_dsn:
        try:
            import sentry_sdk
            from sentry_sdk.integrations.fastapi import FastApiIntegration
            from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
            from sentry_sdk.integrations.logging import LoggingIntegration
            
            # Configure Sentry
            sentry_sdk.init(
                dsn=settings.sentry_dsn,
                environment=settings.sentry_environment,
                traces_sample_rate=settings.sentry_traces_sample_rate,  # 20% for performance
                profiles_sample_rate=0.1,  # 10% for profiling
                integrations=[
                    FastApiIntegration(transaction_style="endpoint"),
                    SqlalchemyIntegration(),
                    LoggingIntegration(level=logging.INFO, event_level=logging.ERROR),
                ],
                # Filter out noisy events
                before_send=lambda event, hint: _filter_sentry_event(event, hint),
                # Set release (optional, for tracking deployments)
                release=None,  # Can be set from git commit hash
            )
            logger.info("✅ Sentry error tracking initialized")
        except Exception as e:
            logger.warning(f"⚠️  Failed to initialize Sentry: {e}. Error tracking disabled.")
    else:
        logger.info("Sentry DSN not configured - error tracking disabled")
    
    # Startup
    logger.info("Starting FCS RAG Bot API...")
    
    # Validate configuration
    if not validate_settings():
        logger.error("Configuration validation failed! Check your .env file.")
        raise ValueError("Invalid configuration")
    
    logger.info("Configuration validated successfully")
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Qdrant URL: {settings.qdrant_url}")
    
    # Pre-initialize database connection (if configured)
    if settings.database_url:
        logger.info("Pre-initializing database connection...")
        try:
            from ..services.database import init_database
            init_database()
            logger.info("✅ Database connection pre-initialized successfully")
        except Exception as e:
            logger.warning(f"⚠️  Database pre-initialization failed: {e}. Database features may be disabled.")
    else:
        logger.info("DATABASE_URL not configured - database features disabled")
    
    # Pre-initialize Redis connection (if configured)
    if settings.redis_url:
        logger.info("Pre-initializing Redis connection...")
        try:
            from ..services.cache import get_redis_client
            redis_client = get_redis_client()
            if redis_client:
                logger.info("✅ Redis client pre-initialized successfully")
            else:
                logger.warning("⚠️  Redis client not available (caching disabled)")
        except Exception as e:
            logger.warning(f"⚠️  Redis pre-initialization failed: {e}. Caching may be disabled.")
    else:
        logger.info("Redis URL not configured - caching disabled")
    
    # Pre-initialize RAG pipeline to eliminate cold start delay
    # This ensures the first user doesn't wait 10-25 seconds for initialization
    # Wrapped in try/except to ensure API starts even if initialization fails
    # Qdrant client has a 30s timeout, so worst case is 30s delay on startup
    logger.info("Pre-initializing RAG pipeline (this may take a few seconds)...")
    try:
        from ..core.rag import get_rag_pipeline
        import time
        
        start_time = time.time()
        
        # Initialize pipeline synchronously (better than first user waiting)
        # Qdrant client already has 30s timeout configured, so this won't hang forever
        pipeline = get_rag_pipeline()
        
        init_time = time.time() - start_time
        logger.info(f"✅ RAG pipeline pre-initialized successfully in {init_time:.2f}s")
        
    except Exception as e:
        # If initialization fails, API still starts - pipeline will init on first query
        logger.warning(f"⚠️  RAG pipeline pre-initialization failed (will initialize on first query): {e}")
        logger.info("This is not critical - the API will still start and initialize on first query")
        # Don't re-raise - we want the API to start even if pipeline init fails
    
    yield
    
    # Shutdown
    logger.info("Shutting down FCS RAG Bot API...")


# Create FastAPI app
app = FastAPI(
    title="FCS RAG Bot API",
    description="RAG-based technical support system for Vena platform",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS middleware (restrict to frontend domain for security)
# Build allowed origins list
allowed_origins = [settings.frontend_url]

# Add localhost for development
if settings.environment == "development" or settings.debug:
    allowed_origins.append("http://localhost:3000")
    allowed_origins.append("http://127.0.0.1:3000")
    # Next.js dev server may pick a different port if 3000 is occupied
    allowed_origins.append("http://localhost:3001")
    allowed_origins.append("http://127.0.0.1:3001")
    allowed_origins.append("http://localhost:3002")
    allowed_origins.append("http://127.0.0.1:3002")

logger.info(f"CORS allowed origins: {allowed_origins}")


def _filter_sentry_event(event, hint):
    """
    Filter out noisy events from Sentry.
    
    Filters:
    - Health check endpoints (not real errors)
    - 404 errors (expected, not errors)
    - Rate limit 429s (expected behavior)
    """
    # Get exception info if available
    exc_info = hint.get('exc_info')
    if exc_info:
        exc_type, exc_value, exc_traceback = exc_info
        
        # Filter out 404 Not Found errors
        from fastapi import HTTPException
        if isinstance(exc_value, HTTPException) and exc_value.status_code == 404:
            return None  # Don't send to Sentry
    
    # Filter by URL path
    if 'request' in event:
        url = event['request'].get('url', '')
        
        # Filter health check endpoints (but allow sentry-test)
        if any(path in url for path in ['/health/warmup', '/api/health/warmup', '/health/ready', '/api/health/ready']):
            return None  # Don't send health check errors
        # Allow /health/sentry-test to pass through for testing
        
        # Filter rate limit errors (429) - these are expected
        if 'status_code' in event.get('request', {}):
            if event['request'].get('status_code') == 429:
                return None  # Don't send rate limit errors
    
    # Sanitize sensitive data
    if 'request' in event:
        # Remove Authorization header
        if 'headers' in event['request']:
            event['request']['headers'].pop('Authorization', None)
            event['request']['headers'].pop('authorization', None)
        
        # Truncate query text if present (privacy)
        if 'data' in event['request']:
            data = event['request']['data']
            if isinstance(data, dict):
                # Truncate question/query text to 200 chars
                for key in ['question', 'query', 'calc_script']:
                    if key in data and isinstance(data[key], str) and len(data[key]) > 200:
                        data[key] = data[key][:200] + "... [truncated]"
    
    return event  # Send the event


# Import middleware after app creation to avoid circular import issues
from .middleware.sentry_middleware import SentryUserContextMiddleware
from .middleware.auth_middleware import AuthMiddleware

# Add Sentry user context middleware (before auth middleware)
app.add_middleware(SentryUserContextMiddleware)

# Add auth middleware to extract user_id from JWT (for rate limiting)
app.add_middleware(AuthMiddleware)

# Add rate limiting middleware (if enabled)
if settings.rate_limit_enabled:
    limiter = get_limiter()
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, rate_limit_handler)
    app.add_middleware(SlowAPIMiddleware)
    logger.info("Rate limiting middleware enabled")
else:
    logger.info("Rate limiting is disabled")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Only allow frontend domain
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Only needed HTTP methods
    allow_headers=["Content-Type", "Authorization"],  # Only needed headers
)

# Exception handler for validation errors (422)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Log validation errors for debugging."""
    body = await request.body()
    logger.error(f"Validation error on {request.url.path}: {exc.errors()}")
    logger.error(f"Request body (first 500 chars): {body[:500]}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body_preview": body[:500].decode('utf-8', errors='ignore')},
    )

# Include routers
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(query.router, prefix="/api", tags=["Query"])
app.include_router(ingestion.router, prefix="/api", tags=["Ingestion"])
app.include_router(jira.router, prefix="/api", tags=["Jira"])
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
app.include_router(users.router, prefix="/api", tags=["Users"])


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "FCS RAG Bot API",
        "version": "1.0.0",
        "docs": "/api/docs",
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "src.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )

