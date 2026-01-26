"""
Quick debugging utility for RAG bot.

Usage:
    python scripts/debug_rag_bot.py --question "Your question"
    python scripts/debug_rag_bot.py --check-connections
    python scripts/debug_rag_bot.py --view-logs --limit 10
    python scripts/debug_rag_bot.py --test-retrieval "Your question"
"""

import sys
import os
import argparse
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend" / "src"))

def check_connections():
    """Check all external service connections."""
    print("=" * 80)
    print("CHECKING CONNECTIONS")
    print("=" * 80)
    print()
    
    from src.utils.config import settings
    
    # Check Qdrant
    print("1. Qdrant Connection:")
    try:
        from qdrant_client import QdrantClient
        client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key
        )
        collections = client.get_collections()
        print(f"   ✓ Connected")
        print(f"   Collection '{settings.qdrant_collection_name}': ", end="")
        collection_names = [c.name for c in collections.collections]
        if settings.qdrant_collection_name in collection_names:
            info = client.get_collection(settings.qdrant_collection_name)
            print(f"✓ Found ({info.points_count} points)")
        else:
            print("✗ Not found")
            print(f"   Available collections: {collection_names}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    print()
    
    # Check Redis
    print("2. Redis Connection:")
    try:
        import redis
        r = redis.from_url(settings.redis_url)
        r.ping()
        print(f"   ✓ Connected to {settings.redis_url}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    print()
    
    # Check PostgreSQL
    print("3. PostgreSQL Connection:")
    try:
        from sqlalchemy import create_engine, text
        engine = create_engine(settings.database_url)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print(f"   ✓ Connected")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    print()
    
    # Check OpenAI
    print("4. OpenAI API:")
    try:
        import openai
        client = openai.OpenAI(api_key=settings.openai_api_key)
        # Just check if key is set (don't make actual API call)
        if settings.openai_api_key:
            print(f"   ✓ API key configured")
        else:
            print(f"   ✗ API key not set")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    print()
    
    # Check Anthropic
    print("5. Anthropic API:")
    if settings.anthropic_api_key:
        print(f"   ✓ API key configured")
    else:
        print(f"   ⚠ API key not set (optional if using OpenAI)")
    print()
    
    # Check LLM Provider
    print("6. LLM Provider Configuration:")
    print(f"   Provider: {settings.llm_provider}")
    if settings.llm_provider == "openai":
        print(f"   Model: {settings.openai_model}")
    elif settings.llm_provider == "anthropic":
        print(f"   Model: {settings.anthropic_model}")
    print()


def test_retrieval(question: str):
    """Test retrieval for a question."""
    print("=" * 80)
    print("TESTING RETRIEVAL")
    print("=" * 80)
    print(f"Question: {question}")
    print()
    
    try:
        from src.core.rag import get_rag_pipeline
        from src.utils.config import settings
        
        pipeline = get_rag_pipeline()
        print("✓ Pipeline initialized")
        print()
        
        # Test retrieval
        print("Testing retrieval...")
        documents = pipeline.retrieve(question, top_k=settings.top_k_results)
        print(f"✓ Retrieved {len(documents)} documents")
        print()
        
        if documents:
            print("Retrieved Documents:")
            for i, doc in enumerate(documents, 1):
                source = doc.metadata.get('source', 'unknown')
                preview = doc.page_content[:100].replace('\n', ' ')
                print(f"  {i}. {source}")
                print(f"     {preview}...")
                print()
        else:
            print("⚠ NO DOCUMENTS RETRIEVED!")
            print("   This might explain why the bot refuses to answer.")
            print()
        
        # Test full query
        print("Testing full query...")
        response, docs = pipeline.query(question)
        print(f"✓ Response generated ({len(response)} chars)")
        print()
        
        # Check for refusal
        refusal_indicators = [
            "do not contain", "does not contain", "would need documentation",
            "context documents do not contain"
        ]
        is_refusal = any(indicator in response.lower() for indicator in refusal_indicators)
        
        print(f"Refusal detected: {is_refusal}")
        print()
        print("Response preview:")
        print("-" * 80)
        print(response[:500])
        print("-" * 80)
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()


def view_logs(limit: int = 20):
    """View recent query logs."""
    print("=" * 80)
    print(f"RECENT QUERY LOGS (last {limit})")
    print("=" * 80)
    print()
    
    try:
        from src.utils.config import settings
        from sqlalchemy import create_engine, text
        
        engine = create_engine(settings.database_url)
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT 
                    question,
                    answer,
                    latency_ms,
                    was_cached,
                    was_refusal,
                    created_at
                FROM query_logs
                ORDER BY created_at DESC
                LIMIT :limit
            """), {"limit": limit})
            
            for i, row in enumerate(result, 1):
                print(f"{i}. [{row.created_at}]")
                print(f"   Q: {row.question[:60]}...")
                print(f"   A: {row.answer[:60]}...")
                print(f"   Latency: {row.latency_ms}ms | Cached: {row.was_cached} | Refusal: {row.was_refusal}")
                print()
                
    except Exception as e:
        print(f"✗ Error: {e}")
        print("   Make sure DATABASE_URL is set and query_logs table exists")


def main():
    parser = argparse.ArgumentParser(description="Debug RAG bot")
    parser.add_argument("--question", "-q", help="Test question for retrieval")
    parser.add_argument("--check-connections", "-c", action="store_true", help="Check all connections")
    parser.add_argument("--view-logs", "-l", action="store_true", help="View recent query logs")
    parser.add_argument("--limit", type=int, default=20, help="Number of logs to show (default: 20)")
    parser.add_argument("--test-retrieval", "-t", help="Test retrieval for a question")
    
    args = parser.parse_args()
    
    if args.check_connections:
        check_connections()
    
    if args.view_logs:
        view_logs(args.limit)
    
    if args.test_retrieval:
        test_retrieval(args.test_retrieval)
    
    if args.question:
        test_retrieval(args.question)
    
    if not any([args.check_connections, args.view_logs, args.test_retrieval, args.question]):
        parser.print_help()


if __name__ == "__main__":
    main()
