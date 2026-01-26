"""
Test Error Code 1008 retrieval with different queries.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.core.rag import get_rag_pipeline

def test_retrieval(query, top_k=15):
    """Test retrieval for a query."""
    print(f"\n{'='*60}")
    print(f"Query: {query}")
    print(f"{'='*60}")
    
    pipeline = get_rag_pipeline()
    documents = pipeline.retrieve(query, top_k=top_k)
    
    print(f"Found {len(documents)} documents\n")
    
    error_1008_found = False
    for i, doc in enumerate(documents, 1):
        source = doc.metadata.get('source', 'unknown')
        source_name = source.split('\\')[-1] if '\\' in source else source.split('/')[-1]
        
        # Check if Error Code 1008 document
        if '1008' in source_name or 'Error Code 1008' in source_name:
            error_1008_found = True
            print(f"[FOUND] {i}. {source_name}")
            print(f"   Content preview: {doc.page_content[:200]}...")
        else:
            print(f"   {i}. {source_name}")
    
    print(f"\nError Code 1008 document found: {error_1008_found}")
    return error_1008_found

if __name__ == "__main__":
    queries = [
        "What causes Error Code 1008 in Vena Copilot?",
        "Error Code 1008 CSV blank",
        "1008",
        "Error Code 1008 or CSV Report Downloaded Is Blank",
    ]
    
    for query in queries:
        test_retrieval(query, top_k=15)
        print()
