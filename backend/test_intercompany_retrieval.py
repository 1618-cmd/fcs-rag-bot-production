"""
Test script to check what documents are retrieved for intercompany eliminations question.
"""
import sys
import asyncio
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent))

from src.core.rag import get_rag_pipeline
from src.utils.config import settings

# Fix Windows console encoding for emojis
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

async def test_retrieval(question: str):
    print("=" * 80)
    print("RETRIEVAL TEST")
    print("=" * 80)
    print(f"Question: {question}")
    print(f"Collection: {settings.qdrant_collection_name}")
    print(f"Top K: {settings.top_k_results}\n")

    try:
        pipeline = get_rag_pipeline()
        print("Pipeline initialized [OK]")
        print(f"Vector store: {pipeline.vector_store is not None}\n")

        print("Testing retrieval...")
        documents = pipeline.retrieve(question, top_k=settings.top_k_results)
        print(f"Documents retrieved: {len(documents)}\n")

        if documents:
            print("Retrieved Documents:")
            for i, doc in enumerate(documents, 1):
                source_path = doc.metadata.get('source', 'unknown')
                # Clean up source name for display
                source_name = Path(source_path).name
                if settings.knowledge_base_dir in Path(source_path).parents:
                    try:
                        relative_path = Path(source_path).relative_to(settings.knowledge_base_dir)
                        source_name = str(relative_path).replace("\\", "/")
                    except:
                        pass
                
                print(f"\n  {i}. {source_name}")
                print(f"     Preview: {doc.page_content[:200]}...")
        else:
            print("No documents retrieved.")

        print("\n" + "=" * 80)
        print("Testing full query...")
        print("=" * 80)
        response, docs = await pipeline.query_async(question)
        
        is_refusal = any(indicator.lower() in response.lower() for indicator in [
            "do not contain", "does not contain", "would need documentation", "insufficient information"
        ])

        print(f"Response length: {len(response)} characters")
        print(f"Is refusal: {is_refusal}\n")
        print("Response preview:")
        print("-" * 80)
        print(response[:1000])
        print("-" * 80)
        
        if docs:
            print(f"\nSources used: {pipeline.get_sources(docs)}")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_question = "How do I write a VenaQL script that handles intercompany eliminations with multiple entity relationships, includes error checking for missing data, and uses nested IF statements to apply different elimination rules based on entity type?"
    
    asyncio.run(test_retrieval(test_question))
