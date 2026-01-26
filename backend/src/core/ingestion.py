"""
Document ingestion pipeline for the Vena RAG Bot Production.

Loads documents from knowledge_base/, chunks them, generates embeddings,
and stores them in Qdrant Cloud for semantic search.
"""

import logging
import io
import hashlib
from pathlib import Path
from typing import List, Optional, Dict, Set
from datetime import datetime

from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from ..utils.config import settings, validate_settings

# AWS S3 support (optional)
try:
    import boto3
    from botocore.exceptions import ClientError
    S3_AVAILABLE = True
except ImportError:
    S3_AVAILABLE = False
    boto3 = None

# Set up logging
logger = logging.getLogger(__name__)


def load_documents_from_s3(bucket_name: str, prefix: str = "") -> List:
    """
    Load all markdown and text documents from AWS S3 bucket.
    
    Args:
        bucket_name: Name of S3 bucket
        prefix: Optional prefix/folder path in S3 bucket
        
    Returns:
        List of loaded documents
    """
    if not S3_AVAILABLE:
        raise ImportError("boto3 is not installed. Install it with: pip install boto3")
    
    logger.info(f"Loading documents from S3: s3://{bucket_name}/{prefix}")
    
    documents = []
    
    try:
        # Initialize S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region
        )
        
        # List all objects in the bucket with the prefix
        paginator = s3_client.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
        
        # Supported file extensions
        supported_extensions = {'.md', '.txt', '.pdf'}
        
        for page in pages:
            if 'Contents' not in page:
                continue
                
            for obj in page['Contents']:
                key = obj['Key']
                
                # Skip if it's a directory (ends with /)
                if key.endswith('/'):
                    continue
                
                # Check if file extension is supported
                file_ext = Path(key).suffix.lower()
                if file_ext not in supported_extensions:
                    continue
                
                try:
                    # Download file content
                    response = s3_client.get_object(Bucket=bucket_name, Key=key)
                    content = response['Body'].read()
                    
                    # Create a document based on file type
                    if file_ext == '.pdf':
                        # For PDFs, we need to use PyPDFLoader with BytesIO
                        from langchain_community.document_loaders import PyPDFLoader
                        import tempfile
                        import os
                        
                        # Create temporary file for PDF
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                            tmp_file.write(content)
                            tmp_path = tmp_file.name
                        
                        try:
                            pdf_loader = PyPDFLoader(tmp_path)
                            docs = pdf_loader.load()
                            # Update source to show S3 path
                            for doc in docs:
                                doc.metadata['source'] = f"s3://{bucket_name}/{key}"
                            documents.extend(docs)
                        finally:
                            os.unlink(tmp_path)
                    else:
                        # For text files (md, txt), decode and create document
                        text_content = content.decode('utf-8')
                        from langchain_core.documents import Document
                        doc = Document(
                            page_content=text_content,
                            metadata={'source': f"s3://{bucket_name}/{key}"}
                        )
                        documents.append(doc)
                        
                except Exception as e:
                    logger.warning(f"Error loading {key} from S3: {e}")
                    continue
        
        logger.info(f"Found {len(documents)} documents in S3")
        
    except ClientError as e:
        logger.error(f"AWS S3 error: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading documents from S3: {e}")
        raise
    
    return documents


def load_documents(knowledge_base_path: Optional[Path] = None) -> List:
    """
    Load all markdown and text documents from knowledge base.
    Supports both local filesystem and AWS S3.
    
    Args:
        knowledge_base_path: Path to knowledge base directory (for local filesystem)
                            If None and use_s3 is True, will load from S3
        
    Returns:
        List of loaded documents
    """
    # Check if S3 should be used
    if settings.use_s3:
        if not settings.s3_bucket_name:
            raise ValueError("S3_BUCKET_NAME must be set when USE_S3 is True")
        # Use approved prefix if configured, otherwise use base prefix
        s3_prefix = settings.s3_approved_prefix or settings.s3_prefix
        # If approved prefix is empty but base prefix is set, default to approved subfolder
        if not s3_prefix and settings.s3_prefix:
            s3_prefix = f"{settings.s3_prefix}approved/"
        return load_documents_from_s3(settings.s3_bucket_name, s3_prefix)
    
    # Otherwise, use local filesystem
    if knowledge_base_path is None:
        knowledge_base_path = settings.knowledge_base_dir
    
    logger.info(f"Loading documents from: {knowledge_base_path}")
    
    documents = []
    
    try:
        # Load markdown files
        md_loader = DirectoryLoader(
            str(knowledge_base_path),
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        documents.extend(md_loader.load())
        
        # Load text files
        txt_loader = DirectoryLoader(
            str(knowledge_base_path),
            glob="**/*.txt",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        documents.extend(txt_loader.load())
        
        # Load PDF files
        pdf_loader = DirectoryLoader(
            str(knowledge_base_path),
            glob="**/*.pdf",
            loader_cls=PyPDFLoader
        )
        documents.extend(pdf_loader.load())
        
        logger.info(f"Found {len(documents)} documents")
        
    except Exception as e:
        logger.error(f"Error loading documents: {e}")
        raise
    
    return documents


def chunk_documents(documents: List) -> List:
    """
    Split documents into smaller chunks for embedding.
    
    Args:
        documents: List of documents to chunk
        
    Returns:
        List of document chunks
    """
    logger.info("Chunking documents...")
    
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        chunks = text_splitter.split_documents(documents)
        
        # Add modification time to chunk metadata for tracking
        for chunk in chunks:
            source_path = chunk.metadata.get('source', '')
            if source_path:
                try:
                    file_path = Path(source_path)
                    if file_path.exists():
                        chunk.metadata['mtime'] = file_path.stat().st_mtime
                except Exception:
                    pass  # If we can't get mtime, that's okay
        
        logger.info(f"Created {len(chunks)} chunks")
        
        return chunks
        
    except Exception as e:
        logger.error(f"Error chunking documents: {e}")
        raise


def create_qdrant_client() -> QdrantClient:
    """
    Create and return Qdrant client.
    
    Returns:
        QdrantClient instance
    """
    if not settings.qdrant_url or not settings.qdrant_api_key:
        raise ValueError("Qdrant configuration missing. Set QDRANT_URL and QDRANT_API_KEY in .env")
    
    try:
        client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
        )
        logger.info(f"Connected to Qdrant at {settings.qdrant_url}")
        return client
        
    except Exception as e:
        logger.error(f"Error connecting to Qdrant: {e}")
        raise


def create_vector_store(chunks: List, collection_name: Optional[str] = None) -> Qdrant:
    """
    Create Qdrant vector store from document chunks.
    
    Args:
        chunks: List of document chunks
        collection_name: Optional collection name (defaults to settings)
        
    Returns:
        Qdrant vector store instance
    """
    logger.info("Generating embeddings and storing in Qdrant...")
    
    try:
        # Initialize embeddings
        embeddings = OpenAIEmbeddings(
            model=settings.embedding_model,
            openai_api_key=settings.openai_api_key
        )
        
        # Get embedding dimension
        # text-embedding-3-small has 1536 dimensions
        embedding_dimension = 1536
        
        # Create Qdrant client
        client = create_qdrant_client()
        
        # Collection name
        collection = collection_name or settings.qdrant_collection_name
        
        # Check if collection exists, create if not
        collection_exists = False
        try:
            client.get_collection(collection)
            collection_exists = True
            logger.info(f"Using existing collection: {collection}")
        except Exception:
            # Collection doesn't exist or version compatibility issue - try to create
            logger.info(f"Attempting to create collection: {collection}")
            try:
                client.create_collection(
                    collection_name=collection,
                    vectors_config=VectorParams(
                        size=embedding_dimension,
                        distance=Distance.COSINE
                    )
                )
                collection_exists = True
                logger.info(f"Created new collection: {collection}")
            except Exception as create_error:
                # If creation fails with 409, collection already exists - that's fine
                error_str = str(create_error)
                if "already exists" in error_str or "409" in error_str or "Conflict" in error_str:
                    logger.info(f"Collection {collection} already exists, using it")
                    collection_exists = True
                else:
                    logger.warning(f"Could not create collection, will attempt to use existing: {create_error}")
                    collection_exists = True  # Assume it exists and try anyway
        
        # Create vector store from documents
        vector_store = Qdrant.from_documents(
            documents=chunks,
            embedding=embeddings,
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
            collection_name=collection,
        )
        
        logger.info(f"✅ Vector store created/updated in Qdrant collection: {collection}")
        return vector_store
        
    except Exception as e:
        logger.error(f"Error creating vector store: {e}")
        raise


def get_ingested_files(collection_name: Optional[str] = None) -> Dict[str, float]:
    """
    Get list of already ingested files with their modification times.
    
    Args:
        collection_name: Optional collection name (defaults to settings)
        
    Returns:
        Dictionary mapping file paths to modification timestamps
    """
    collection = collection_name or settings.qdrant_collection_name
    
    try:
        client = create_qdrant_client()
        
        # Check if collection exists
        try:
            client.get_collection(collection)
        except Exception:
            logger.info(f"Collection {collection} does not exist, no files ingested yet")
            return {}
        
        # Scroll through all points to get metadata
        ingested_files = {}
        offset = None
        limit = 100
        
        while True:
            result = client.scroll(
                collection_name=collection,
                limit=limit,
                offset=offset,
                with_payload=True,
                with_vectors=False
            )
            
            points = result[0]
            if not points:
                break
            
            for point in points:
                if point.payload and 'source' in point.payload:
                    source_path = point.payload['source']
                    # Store modification time if available, otherwise use 0
                    mtime = point.payload.get('mtime', 0)
                    if source_path not in ingested_files or mtime > ingested_files[source_path]:
                        ingested_files[source_path] = mtime
            
            offset = result[1]
            if offset is None:
                break
        
        logger.info(f"Found {len(ingested_files)} already ingested files")
        return ingested_files
        
    except Exception as e:
        logger.warning(f"Error getting ingested files: {e}")
        return {}


def get_file_hash(file_path: Path) -> str:
    """Get file hash for change detection."""
    try:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return ""


def filter_new_or_changed_documents(
    documents: List, 
    ingested_files: Dict[str, float]
) -> List:
    """
    Filter documents to only include new or changed files.
    
    Args:
        documents: List of all documents
        ingested_files: Dictionary of already ingested files with mtimes
        
    Returns:
        List of new or changed documents
    """
    new_documents = []
    
    for doc in documents:
        source_path = doc.metadata.get('source', '')
        if not source_path:
            # If no source, include it (better safe than sorry)
            new_documents.append(doc)
            continue
        
        # Get file modification time
        try:
            file_path = Path(source_path)
            if file_path.exists():
                mtime = file_path.stat().st_mtime
            else:
                # File doesn't exist, skip it
                continue
        except Exception:
            # Can't get mtime, include it to be safe
            new_documents.append(doc)
            continue
        
        # Check if file is new or changed
        if source_path not in ingested_files:
            logger.debug(f"New file: {source_path}")
            new_documents.append(doc)
        elif mtime > ingested_files[source_path]:
            logger.debug(f"Changed file: {source_path}")
            new_documents.append(doc)
        # else: file is unchanged, skip it
    
    return new_documents


def delete_file_chunks(collection_name: str, file_path: str, client: QdrantClient):
    """Delete all chunks for a specific file."""
    try:
        # Scroll to find all points with this source
        offset = None
        limit = 100
        ids_to_delete = []
        
        while True:
            result = client.scroll(
                collection_name=collection_name,
                limit=limit,
                offset=offset,
                with_payload=True,
                with_vectors=False
            )
            
            points = result[0]
            if not points:
                break
            
            for point in points:
                if point.payload and point.payload.get('source') == file_path:
                    ids_to_delete.append(point.id)
            
            offset = result[1]
            if offset is None:
                break
        
        # Delete the points
        if ids_to_delete:
            client.delete(
                collection_name=collection_name,
                points_selector=ids_to_delete
            )
            logger.info(f"Deleted {len(ids_to_delete)} chunks for {file_path}")
        
    except Exception as e:
        logger.warning(f"Error deleting chunks for {file_path}: {e}")


def clear_collection(collection_name: Optional[str] = None) -> bool:
    """
    Clear all documents from a Qdrant collection.
    
    Args:
        collection_name: Optional collection name (defaults to settings)
        
    Returns:
        True if collection was cleared, False if collection doesn't exist
    """
    collection = collection_name or settings.qdrant_collection_name
    
    try:
        client = create_qdrant_client()
        
        # Check if collection exists
        try:
            client.get_collection(collection)
        except Exception:
            logger.info(f"Collection {collection} does not exist, nothing to clear")
            return False
        
        # Delete all points in the collection
        client.delete_collection(collection)
        logger.info(f"Cleared collection: {collection}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error clearing collection: {e}")
        raise


def ingest_knowledge_base(
    collection_name: Optional[str] = None, 
    clear_first: bool = False,
    incremental: bool = True
) -> Qdrant:
    """
    Main ingestion pipeline: Load → Chunk → Embed → Store.
    
    Args:
        collection_name: Optional collection name
        clear_first: If True, clear collection before ingestion (full re-ingest)
        incremental: If True, only process new/changed files (default: True)
        
    Returns:
        Qdrant vector store instance
    """
    logger.info("=" * 50)
    logger.info("Vena RAG Bot - Knowledge Base Ingestion")
    logger.info("=" * 50)
    
    if clear_first:
        logger.info("Mode: Full re-ingestion (clearing collection first)")
    elif incremental:
        logger.info("Mode: Incremental (only new/changed files)")
    else:
        logger.info("Mode: Add all files (may create duplicates)")
    
    # Validate configuration
    if not validate_settings():
        raise ValueError("Configuration validation failed!")
    
    # Check knowledge base exists
    if not settings.knowledge_base_dir.exists():
        logger.error(f"Knowledge base directory not found: {settings.knowledge_base_dir}")
        logger.info("Creating empty directory structure...")
        settings.knowledge_base_dir.mkdir(parents=True, exist_ok=True)
        raise FileNotFoundError("Add documents to knowledge_base/ folder first!")
    
    # Clear collection if requested
    if clear_first:
        logger.info("Clearing existing collection before ingestion...")
        clear_collection(collection_name)
        ingested_files = {}
    elif incremental:
        # Get list of already ingested files
        logger.info("Checking for already ingested files...")
        ingested_files = get_ingested_files(collection_name)
        if ingested_files:
            logger.info(f"Found {len(ingested_files)} already ingested files")
    else:
        ingested_files = {}
    
    # Load documents (from S3 or local filesystem)
    all_documents = load_documents()
    
    if len(all_documents) == 0:
        logger.error("No documents found in knowledge base!")
        logger.info("Add .md or .txt files to knowledge_base/ folder")
        raise FileNotFoundError("No documents to ingest!")
    
    # Filter to only new/changed documents if incremental
    if incremental and ingested_files:
        documents = filter_new_or_changed_documents(all_documents, ingested_files)
        logger.info(f"Processing {len(documents)} new/changed files out of {len(all_documents)} total")
        
        if len(documents) == 0:
            logger.info("No new or changed files to ingest. All files are up to date!")
            # Return existing vector store
            collection = collection_name or settings.qdrant_collection_name
            embeddings = OpenAIEmbeddings(
                model=settings.embedding_model,
                openai_api_key=settings.openai_api_key
            )
            client = create_qdrant_client()
            return Qdrant(
                client=client,
                collection_name=collection,
                embeddings=embeddings,
            )
        
        # Delete old chunks for changed files
        collection = collection_name or settings.qdrant_collection_name
        client = create_qdrant_client()
        changed_files = set()
        for doc in documents:
            source_path = doc.metadata.get('source', '')
            if source_path and source_path in ingested_files:
                changed_files.add(source_path)
        
        for file_path in changed_files:
            delete_file_chunks(collection, file_path, client)
    else:
        documents = all_documents
        logger.info(f"Processing {len(documents)} files")
    
    # Chunk documents
    chunks = chunk_documents(documents)
    
    # Create vector store
    vector_store = create_vector_store(chunks, collection_name)
    
    logger.info("=" * 50)
    logger.info("✅ Ingestion complete!")
    logger.info(f"   Documents: {len(documents)}")
    logger.info(f"   Chunks: {len(chunks)}")
    logger.info("=" * 50)
    
    return vector_store


if __name__ == "__main__":
    import sys
    
    # Set up basic logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    # Check flags
    clear_first = "--clear" in sys.argv or "-c" in sys.argv or "--full" in sys.argv
    incremental = not clear_first  # Default to incremental unless --clear/--full is specified
    
    if "--incremental" in sys.argv or "-i" in sys.argv:
        incremental = True
        clear_first = False
    
    if clear_first:
        logger.info("Full re-ingestion mode: will clear collection before ingestion")
    else:
        logger.info(f"Incremental mode: will only process new/changed files")
    
    ingest_knowledge_base(clear_first=clear_first, incremental=incremental)

