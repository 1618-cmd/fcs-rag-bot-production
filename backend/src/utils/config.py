"""
Configuration settings for the Vena RAG Bot Production.

Loads settings from environment variables using Pydantic Settings.
"""

import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # OpenAI Configuration
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"
    embedding_model: str = "text-embedding-3-small"
    
    # Qdrant Configuration (Production Vector DB)
    qdrant_url: Optional[str] = None
    qdrant_api_key: Optional[str] = None
    qdrant_collection_name: str = "vena_rag_bot"
    
    # Database Configuration (Postgres)
    database_url: Optional[str] = None
    
    # Redis Configuration (Caching)
    redis_url: Optional[str] = None
    cache_ttl: int = 86400  # 24 hours in seconds
    
    # Rate Limiting Configuration
    rate_limit_enabled: bool = True
    rate_limit_query_per_minute: int = 20  # Queries per minute per user/IP
    rate_limit_user_management_per_minute: int = 10  # User management endpoints
    rate_limit_login_per_minute: int = 5  # Login attempts per minute per IP
    
    # Sentry Configuration (Error Tracking)
    sentry_dsn: Optional[str] = None
    sentry_environment: str = "production"  # Will be set from environment
    sentry_traces_sample_rate: float = 1.0  # 100% in production, lower in dev
    
    # Paths (relative to project root)
    project_root: Path = Path(__file__).parent.parent.parent.parent
    knowledge_base_dir: Path = project_root / "knowledge_base"
    
    # AWS S3 Configuration (optional - for knowledge base hosting)
    use_s3: bool = False  # Set to True to use S3 instead of local filesystem
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    aws_region: str = "us-east-1"  # Default AWS region
    s3_bucket_name: Optional[str] = None
    s3_prefix: str = ""  # Optional prefix/folder in S3 bucket
    s3_staging_prefix: str = ""  # Staging folder (default: knowledge_base/staging/)
    s3_approved_prefix: str = ""  # Approved folder (default: knowledge_base/approved/)
    s3_archive_prefix: str = ""  # Archive folder (default: knowledge_base/archive/)
    
    # Ingestion API Key (optional - for securing the /api/ingest endpoint)
    ingestion_api_key: Optional[str] = None
    
    # RAG Configuration
    chunk_size: int = 500  # tokens per chunk
    chunk_overlap: int = 50  # overlap between chunks
    top_k_results: int = 10  # number of documents to retrieve (increased for better multi-system question coverage)
    
    # Model Configuration
    max_tokens: int = 2000  # max response tokens
    temperature: float = 0.1  # low temperature for factual responses
    
    # Environment
    environment: str = "production"  # production, development, testing
    debug: bool = False
    
    # CORS Configuration
    frontend_url: str = "https://www.fcs-alex.com"  # Frontend URL for CORS
    
    # Jira Configuration (optional - for ticket creation)
    jira_server_url: Optional[str] = None  # e.g., "https://yourcompany.atlassian.net"
    jira_email: Optional[str] = None  # Jira account email
    jira_api_token: Optional[str] = None  # Jira API token (from https://id.atlassian.com/manage-profile/security/api-tokens)
    jira_project_key: Optional[str] = None  # e.g., "SUPPORT"
    jira_issue_type: str = "Task"  # Default issue type (Task, Bug, Story, etc.)
    jira_labels: Optional[str] = None  # Comma-separated labels (e.g., "rag-bot,support")
    
    # Authentication Configuration (simple auth, no database)
    jwt_secret_key: str = "your-secret-key-change-in-production"  # MUST be overridden in production
    admin_email: str = "admin@example.com"  # Used only for optional fallback login
    admin_password: str = "admin"  # Used only for optional fallback login
    allow_fallback_admin_login: bool = False  # Recommended: keep False in production
    
    # Logging
    log_level: str = "INFO"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False
    )


# Global settings instance
settings = Settings()


def validate_settings() -> bool:
    """
    Validate that required settings are configured.
    
    Returns:
        True if settings are valid, False otherwise
    """
    errors = []
    
    # Check OpenAI API key
    if not settings.openai_api_key or settings.openai_api_key == "sk-your-api-key-here":
        errors.append("OPENAI_API_KEY not configured")
    
    # For production, check Qdrant configuration
    if settings.environment == "production":
        if not settings.qdrant_url:
            errors.append("QDRANT_URL not configured (required for production)")
        if not settings.qdrant_api_key:
            errors.append("QDRANT_API_KEY not configured (required for production)")
    
    # Check database URL for production
    if settings.environment == "production" and not settings.database_url:
        errors.append("DATABASE_URL not configured (required for production)")
    
    # JWT secret MUST be set in production (avoid default)
    if settings.environment == "production":
        if (not settings.jwt_secret_key) or (settings.jwt_secret_key == "your-secret-key-change-in-production"):
            errors.append("JWT_SECRET_KEY not configured (required for production)")
        elif len(settings.jwt_secret_key) < 32:
            errors.append("JWT_SECRET_KEY is too short (recommended: 32+ characters)")
    
    if errors:
        print("Configuration validation failed:")
        for error in errors:
            print(f"   - {error}")
        print("\n   Please check your .env file and ensure all required variables are set.")
        return False
    
    return True


def get_settings() -> Settings:
    """Get the global settings instance."""
    return settings


if __name__ == "__main__":
    import sys
    # Fix Windows console encoding
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    if validate_settings():
        print("Configuration validated successfully!")
        print(f"   Environment: {settings.environment}")
        print(f"   Model: {settings.openai_model}")
        print(f"   Embeddings: {settings.embedding_model}")
        print(f"   Knowledge Base: {settings.knowledge_base_dir}")
        if settings.qdrant_url:
            print(f"   Qdrant: {settings.qdrant_url}")
        if settings.database_url:
            print(f"   Database: Configured")
        if settings.redis_url:
            print(f"   Redis: Configured")
    else:
        print("Configuration validation failed!")

