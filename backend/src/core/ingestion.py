"""
Document ingestion pipeline for the Vena RAG Bot Production.

Loads documents from knowledge_base/, chunks them, generates embeddings,
and stores them in Qdrant Cloud for semantic search.
"""

import logging
from pathlib import Path
from typing import List, Optional

from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from ..utils.config import settings, validate_settings

# Set up logging
logger = logging.getLogger(__name__)


def load_documents(knowledge_base_path: Path) -> List:
    """
    Load all markdown and text documents from knowledge base.
    
    Args:
        knowledge_base_path: Path to knowledge base directory
        
    Returns:
        List of loaded documents
    """
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
    
    # Load documents
    documents = load_documents(settings.knowledge_base_dir)
    
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

