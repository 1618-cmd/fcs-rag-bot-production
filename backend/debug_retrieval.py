"""
Debug script to test retrieval directly.
Run: python debug_retrieval.py
"""

import sys
import io
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.core.rag import get_rag_pipeline
from src.utils.config import settings

def debug_retrieval(question: str = "How do I access Vena's training platform?"):
    """Debug retrieval for a question."""
    print("=" * 60)
    print("RETRIEVAL DEBUG")
    print("=" * 60)
    print(f"Question: {question}")
    print(f"Collection: {settings.qdrant_collection_name}")
    print(f"Top K: {settings.top_k_results}")
    print()
    
    try:
        pipeline = get_rag_pipeline()
        
        print("Pipeline initialized [OK]")
        print(f"Vector store: {pipeline.vector_store is not None}")
        print()
        
        # Test retrieval
        print("Testing retrieval...")
        documents = pipeline.retrieve(question, top_k=settings.top_k_results)
        
        print(f"Documents retrieved: {len(documents)}")
        print()
        
        if documents:
            print("Retrieved Documents:")
            for i, doc in enumerate(documents[:5], 1):
                source = doc.metadata.get('source', 'unknown')
                print(f"  {i}. {source}")
                print(f"     Preview: {doc.page_content[:150]}...")
                print()
        else:
            print("[WARNING] NO DOCUMENTS RETRIEVED!")
            print("This might explain why the bot is refusing to answer.")
            print()
        
        # Test full query
        print("Testing full query...")
        try:
            response, docs = pipeline.query(question)
            
            is_refusal = any(indicator in response.lower() for indicator in [
                "do not contain", "does not contain", "would need documentation",
                "context documents do not contain"
            ])
            
            print(f"Response length: {len(response)} characters")
            print(f"Is refusal: {is_refusal}")
            print()
            print("Response preview:")
            print("-" * 60)
            print(response[:500])
            print("-" * 60)
            
        except Exception as e:
            print(f"Query failed: {e}")
            import traceback
            traceback.print_exc()
        
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    question = sys.argv[1] if len(sys.argv) > 1 else "How do I access Vena's training platform?"
    debug_retrieval(question)
