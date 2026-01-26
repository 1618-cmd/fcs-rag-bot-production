"""
Find Error Code 1008 chunks in Qdrant by scanning chunks directly.
"""
import sys
import io
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.utils.config import settings
from qdrant_client import QdrantClient
from qdrant_client.models import ScrollRequest, Filter, FieldCondition, MatchValue

def find_error_1008_chunks():
    """Find Error Code 1008 chunks by scanning collection."""
    print("="*60)
    print("FINDING ERROR CODE 1008 CHUNKS IN QDRANT")
    print("="*60)
    
    # Connect to Qdrant
    try:
        client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
        )
        print("[OK] Connected to Qdrant")
    except Exception as e:
        print(f"[ERROR] Failed to connect: {e}")
        return
    
    # Scan for chunks with "1008" in source path
    print("\nScanning chunks for Error Code 1008 document...")
    print("(This may take a minute for large collections)\n")
    
    found_chunks = []
    offset = None
    
    try:
        # Scroll through chunks in batches
        for i in range(100):  # Check first 10,000 chunks
            batch_size = 100
            scroll_result = client.scroll(
                collection_name=settings.qdrant_collection_name,
                limit=batch_size,
                offset=offset,
                with_payload=True,
            )
            
            points = scroll_result[0]
            offset = scroll_result[1]
            
            if not points:
                break
            
            # Check each point
            for point in points:
                source = point.payload.get('source', '')
                if '1008' in source or 'Error Code 1008' in source:
                    source_name = source.split('\\')[-1] if '\\' in source else source.split('/')[-1]
                    content_preview = point.payload.get('page_content', '')[:200]
                    
                    found_chunks.append({
                        'id': point.id,
                        'source': source_name,
                        'content_preview': content_preview
                    })
                    print(f"[FOUND] Chunk ID: {point.id}")
                    print(f"         Source: {source_name}")
                    print(f"         Content: {content_preview}...")
                    print()
            
            if offset is None:
                break
            
            # Print progress every 10 batches
            if i % 10 == 0:
                print(f"Scanned {(i+1) * batch_size} chunks...")
        
        print("="*60)
        if found_chunks:
            print(f"[RESULT] Found {len(found_chunks)} chunks from Error Code 1008 document!")
            print("The document IS in Qdrant.")
            print("\nThis confirms the issue: chunks exist but aren't retrieved by semantic search.")
            print("Possible causes:")
            print("  1. Chunks contain HTML/navigation noise instead of actual content")
            print("  2. Semantic similarity is too low for the query")
            print("  3. Chunks are at the end of the document (with actual content) but not retrieved")
        else:
            print("[RESULT] No chunks from Error Code 1008 document found in scanned chunks.")
            print("The document may NOT be in Qdrant (not ingested).")
            print("Solution: Re-ingest the knowledge base.")
        print("="*60)
        
    except Exception as e:
        print(f"[ERROR] Failed to scan chunks: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    find_error_1008_chunks()
