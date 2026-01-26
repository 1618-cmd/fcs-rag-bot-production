"""
Check if Error Code 1008 document is in Qdrant collection.
"""
import sys
import io
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.core.rag import get_rag_pipeline
from src.utils.config import settings
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue

def check_error_1008_in_collection():
    """Check if Error Code 1008 document exists in Qdrant collection."""
    print("="*60)
    print("CHECKING ERROR CODE 1008 DOCUMENT IN QDRANT")
    print("="*60)
    print(f"Collection: {settings.qdrant_collection_name}")
    print()
    
    # Connect to Qdrant
    try:
        client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
        )
        print("[OK] Connected to Qdrant")
    except Exception as e:
        print(f"[ERROR] Failed to connect to Qdrant: {e}")
        return
    
    # Get collection info
    try:
        collection_info = client.get_collection(settings.qdrant_collection_name)
        print(f"[OK] Collection has {collection_info.points_count} points (chunks)")
        print()
    except Exception as e:
        print(f"[ERROR] Failed to get collection info: {e}")
        return
    
    # Search for chunks from Error Code 1008 document
    # Try different search strategies
    search_terms = [
        "Error Code 1008",
        "1008",
        "CSV Report Downloaded Is Blank",
        "Troubleshooting Vena Copilot Error Code 1008",
    ]
    
    print("Searching for Error Code 1008 chunks...")
    print()
    
    found_chunks = []
    for term in search_terms:
        try:
            # Search using the same embedding model
            from langchain_openai import OpenAIEmbeddings
            embeddings = OpenAIEmbeddings(
                model=settings.embedding_model,
                openai_api_key=settings.openai_api_key
            )
            
            # Generate embedding for search term
            query_embedding = embeddings.embed_query(term)
            
            # Search in Qdrant
            results = client.search(
                collection_name=settings.qdrant_collection_name,
                query_vector=query_embedding,
                limit=20,
                with_payload=True,
            )
            
            # Check if any results are from Error Code 1008 document
            for result in results:
                source = result.payload.get('source', '')
                if '1008' in source or 'Error Code 1008' in source:
                    if source not in [chunk['source'] for chunk in found_chunks]:
                        found_chunks.append({
                            'source': source,
                            'score': result.score,
                            'content_preview': result.payload.get('page_content', '')[:200]
                        })
                        print(f"[FOUND] Chunk from: {source.split(chr(92))[-1] if chr(92) in source else source.split('/')[-1]}")
                        print(f"         Similarity score: {result.score:.4f}")
                        print(f"         Content preview: {result.payload.get('page_content', '')[:150]}...")
                        print()
        except Exception as e:
            print(f"[WARNING] Search for '{term}' failed: {e}")
            continue
    
    print("="*60)
    if found_chunks:
        print(f"[RESULT] Found {len(found_chunks)} chunks from Error Code 1008 document!")
        print("The document IS in Qdrant, but may not be retrieved due to semantic mismatch.")
    else:
        print("[RESULT] No chunks from Error Code 1008 document found in top results.")
        print("The document may NOT be properly indexed, or chunks don't match well semantically.")
    print("="*60)

if __name__ == "__main__":
    check_error_1008_in_collection()
