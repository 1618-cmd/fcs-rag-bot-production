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
    
    # Paths (relative to project root)
    project_root: Path = Path(__file__).parent.parent.parent.parent
    knowledge_base_dir: Path = project_root / "knowledge_base"
    
    # RAG Configuration
    chunk_size: int = 500  # tokens per chunk
    chunk_overlap: int = 50  # overlap between chunks
    top_k_results: int = 5  # number of documents to retrieve
    
    # Model Configuration
    max_tokens: int = 2000  # max response tokens
    temperature: float = 0.1  # low temperature for factual responses
    
    # Environment
    environment: str = "production"  # production, development, testing
    debug: bool = False
    
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

