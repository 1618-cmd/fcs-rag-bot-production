"""
Document ingestion pipeline for the Vena RAG Bot Production.

Loads documents from knowledge_base/, chunks them, generates embeddings,
and stores them in Qdrant Cloud for semantic search.
"""

import logging
import io
from pathlib import Path
from typing import List, Optional

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


def ingest_knowledge_base(collection_name: Optional[str] = None) -> Qdrant:
    """
    Main ingestion pipeline: Load → Chunk → Embed → Store.
    
    Args:
        collection_name: Optional collection name
        
    Returns:
        Qdrant vector store instance
    """
    logger.info("=" * 50)
    logger.info("🚀 Vena RAG Bot - Knowledge Base Ingestion")
    logger.info("=" * 50)
    
    # Validate configuration
    if not validate_settings():
        raise ValueError("Configuration validation failed!")
    
    # Check knowledge base exists
    if not settings.knowledge_base_dir.exists():
        logger.error(f"Knowledge base directory not found: {settings.knowledge_base_dir}")
        logger.info("Creating empty directory structure...")
        settings.knowledge_base_dir.mkdir(parents=True, exist_ok=True)
        raise FileNotFoundError("Add documents to knowledge_base/ folder first!")
    
    # Load documents (from S3 or local filesystem)
    documents = load_documents()
    
    if len(documents) == 0:
        logger.error("No documents found in knowledge base!")
        logger.info("Add .md or .txt files to knowledge_base/ folder")
        raise FileNotFoundError("No documents to ingest!")
    
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
    # Set up basic logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    ingest_knowledge_base()

