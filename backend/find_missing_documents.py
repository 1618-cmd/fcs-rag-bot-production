"""
Find documents that might not be in Qdrant.
"""
import sys
import io
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.core.ingestion import load_documents
from src.utils.config import settings
from langchain_community.document_loaders import DirectoryLoader, TextLoader

def find_all_documents():
    """Find all documents in knowledge base."""
    print("="*60)
    print("FINDING ALL DOCUMENTS IN KNOWLEDGE BASE")
    print("="*60)
    
    # Load all documents
    documents = load_documents()
    
    print(f"\nTotal documents found: {len(documents)}\n")
    
    # List all document names
    doc_names = []
    for doc in documents:
        source = doc.metadata.get('source', 'unknown')
        if '\\' in source:
            name = source.split('\\')[-1]
        elif '/' in source:
            name = source.split('/')[-1]
        else:
            name = source
        doc_names.append(name)
    
    # Check for Error Code 1008
    error_1008_files = [name for name in doc_names if '1008' in name]
    
    print("Error Code 1008 related files:")
    if error_1008_files:
        for name in error_1008_files:
            print(f"  ✅ {name}")
    else:
        print("  ❌ No Error Code 1008 files found")
    
    print(f"\nTotal documents that should be ingested: {len(doc_names)}")
    print("\nIf you had 18 files not uploaded during ingestion,")
    print("these files exist locally but may not be in Qdrant.")
    print("\nSolution: Re-run ingestion to add missing files.")
    print("="*60)

if __name__ == "__main__":
    find_all_documents()
