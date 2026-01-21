"""
Query endpoints for RAG queries.
"""

import time
import logging
from typing import List, Optional
from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Request
from pydantic import BaseModel, Field

from ...core.rag import get_rag_pipeline
from ...utils.config import settings
from ...services.cache import get_cached_response, cache_response
from ...services.kill_switch import is_kill_switch_enabled, get_kill_switch_message
from ...services.rate_limiter import limit_query

logger = logging.getLogger(__name__)
router = APIRouter()


def extract_text_from_file(file: UploadFile) -> str:
    """
    Extract text from uploaded file.
    Supports .docx (Word), .txt, and .venaql files.
    
    Args:
        file: Uploaded file
        
    Returns:
        Extracted text content
    """
    content = file.file.read()
    file.file.seek(0)  # Reset file pointer
    
    filename = file.filename or ""
    file_extension = filename.split('.')[-1].lower() if '.' in filename else ''
    
    if file_extension == 'docx':
        # Handle Word documents
        try:
            from docx import Document
            import io
            doc = Document(io.BytesIO(content))
            # Extract text from all paragraphs
            text_parts = [para.text for para in doc.paragraphs]
            return '\n'.join(text_parts)
        except ImportError:
            raise HTTPException(
                status_code=400,
                detail="python-docx library is required for Word document support. Install with: pip install python-docx"
            )
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Error reading Word document: {str(e)}"
            )
    elif file_extension in ['txt', 'venaql', 'calc']:
        # Handle text files
        try:
            return content.decode('utf-8')
        except UnicodeDecodeError:
            raise HTTPException(
                status_code=400,
                detail="File encoding error. Please ensure the file is UTF-8 encoded."
            )
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file_extension}. Supported types: .docx, .txt, .venaql, .calc"
        )


class QueryRequest(BaseModel):
    """Request model for RAG query."""
    question: str = Field(..., description="The question to ask", min_length=1, max_length=10000)  # Increased to support long code snippets
    top_k: Optional[int] = Field(None, description="Number of documents to retrieve (default: 5)", ge=1, le=10)
    skip_cache: bool = Field(default=False, description="Skip cache and force fresh response")
    calc_script: Optional[str] = Field(None, description="Optional VenaQL calculation script to analyze (paste text here)", max_length=50000)


class Source(BaseModel):
    """Source document model."""
    name: str
    content: Optional[str] = None


class QueryResponse(BaseModel):
    """Response model for RAG query."""
    answer: str
    sources: List[Source]
    latency_ms: float
    model: str


@router.post("/query", response_model=QueryResponse)
@limit_query()
async def query_rag(http_request: Request, request: QueryRequest):
    """
    Query the RAG system (JSON request).
    
    Takes a question and returns an answer with source citations.
    
    Supports calc script analysis via calc_script field (paste text directly).
    For file uploads, use /api/query/upload endpoint.
    """
    return await _process_query(
        question=request.question,
        calc_script=request.calc_script,
        top_k=request.top_k,
        skip_cache=request.skip_cache
    )


@router.post("/query/upload", response_model=QueryResponse)
@limit_query()
async def query_rag_with_file(
    request: Request,
    question: str = Form(...),
    calc_script: Optional[str] = Form(None),
    calc_script_file: Optional[UploadFile] = File(None),
    top_k: Optional[int] = Form(None),
    skip_cache: bool = Form(False)
):
    """
    Query the RAG system with file upload support.
    
    Supports calc script analysis via:
    - calc_script: Paste script text directly (Form field)
    - calc_script_file: Upload Word doc (.docx) or text file (.txt, .venaql, .calc)
    
    If both calc_script and calc_script_file are provided, calc_script takes precedence.
    """
    # Extract text from uploaded file if provided
    calc_script_text = calc_script
    if calc_script_file and not calc_script_text:
        logger.info(f"Extracting text from uploaded file: {calc_script_file.filename}")
        calc_script_text = extract_text_from_file(calc_script_file)
    
    return await _process_query(
        question=question,
        calc_script=calc_script_text,
        top_k=top_k,
        skip_cache=skip_cache
    )


async def _process_query(
    question: str,
    calc_script: Optional[str] = None,
    top_k: Optional[int] = None,
    skip_cache: bool = False
) -> QueryResponse:
    """
    Internal function to process RAG queries.
    
    Handles both regular queries and calc script analysis.
    """
    # Check kill switch first
    if is_kill_switch_enabled():
        message = get_kill_switch_message() or "System is currently disabled for maintenance. Please try again later."
        logger.warning(f"Query blocked by kill switch: {question[:50]}...")
        raise HTTPException(
            status_code=503,
            detail={
                "error": "Service Unavailable",
                "message": message,
                "kill_switch_enabled": True
            }
        )
    
    start_time = time.time()
    
    try:
        # Build query text - include calc script if provided
        if calc_script:
            query_text = f"""Here's a VenaQL calculation script to analyze:

```venaql
{calc_script.strip()}
```

Question: {question}"""
            logger.info(f"Processing query with calc script ({len(calc_script)} chars)")
        else:
            query_text = question
        
        # Build cache key that includes calc script if provided
        cache_key = question
        if calc_script:
            cache_key = f"{calc_script.strip()}\n\n{question}"
        
        # Check cache first (unless skip_cache is True)
        if not skip_cache:
            cached_response = get_cached_response(cache_key)
            if cached_response:
                # Return cached response (much faster!)
                logger.info(f"Returning cached response (saved {cached_response.get('latency_ms', 0)}ms)")
                return QueryResponse(**cached_response)
        else:
            logger.info("Skipping cache (skip_cache=True)")
        
        # Cache miss - process query
        # Get RAG pipeline
        pipeline = get_rag_pipeline()
        
        # Query the pipeline (async version for better performance)
        # Falls back to sync if async fails
        logger.info(f"Processing query: {query_text[:100]}...")
        try:
            result = await pipeline.query_async(query_text)
            # Ensure result is a tuple with 2 elements
            if isinstance(result, tuple) and len(result) == 2:
                response, documents = result
            else:
                logger.error(f"Unexpected result type from query_async: {type(result)}, length: {len(result) if hasattr(result, '__len__') else 'N/A'}")
                raise ValueError(f"query_async returned unexpected format: {type(result)}")
        except (ValueError, IndexError, TypeError) as async_error:
            logger.warning(f"Async query failed ({type(async_error).__name__}: {async_error}), falling back to sync")
            try:
                result = pipeline.query(query_text)
                # Ensure result is a tuple with 2 elements
                if isinstance(result, tuple) and len(result) == 2:
                    response, documents = result
                else:
                    logger.error(f"Unexpected result type from query: {type(result)}")
                    raise ValueError(f"query returned unexpected format: {type(result)}")
            except Exception as sync_error:
                logger.error(f"Both async and sync queries failed. Async: {async_error}, Sync: {sync_error}")
                raise
        except Exception as async_error:
            logger.warning(f"Async query failed, falling back to sync: {async_error}")
            # Fallback to synchronous version if async fails
            try:
                result = pipeline.query(query_text)
                if isinstance(result, tuple) and len(result) == 2:
                    response, documents = result
                else:
                    raise ValueError(f"query returned unexpected format: {type(result)}")
            except Exception as sync_error:
                logger.error(f"Both async and sync queries failed. Async: {async_error}, Sync: {sync_error}")
                raise
        
        # Check if the response indicates a refusal (missing information)
        # If the LLM refused to answer, don't include sources
        refusal_indicators = [
            "do not contain sufficient information",
            "context documents do not contain",
            "does not contain information",
            "would need documentation",
            "insufficient information to answer"
        ]
        
        is_refusal = any(indicator.lower() in response.lower() for indicator in refusal_indicators)
        
        # Extract sources only if not a refusal
        if is_refusal:
            logger.info("Response indicates refusal - excluding sources")
            sources = []
        else:
            # Ensure documents is a valid list before extracting sources
            if documents and isinstance(documents, list) and len(documents) > 0:
                try:
                    source_names = pipeline.get_sources(documents)
                    sources = [Source(name=name) for name in source_names if name]
                except Exception as source_error:
                    logger.warning(f"Error extracting sources: {source_error}. Continuing without sources.")
                    sources = []
            else:
                logger.warning(f"Invalid documents for source extraction: {type(documents)}, length: {len(documents) if hasattr(documents, '__len__') else 'N/A'}")
                sources = []
        
        # Calculate latency
        latency_ms = (time.time() - start_time) * 1000
        
        logger.info(f"Query completed in {latency_ms:.2f}ms")
        
        # Build response
        query_response = QueryResponse(
            answer=response,
            sources=sources,
            latency_ms=round(latency_ms, 2),
            model=settings.openai_model,
        )
        
        # Cache the response for future queries
        cache_response(cache_key, query_response.dict())
        
        return query_response
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        logger.error(f"Error processing query: {e}", exc_info=True)
        logger.error(f"Full traceback:\n{error_traceback}")
        # Include more detail in the error message for debugging
        error_detail = f"Error processing query: {str(e)}"
        if "tuple index out of range" in str(e).lower():
            error_detail += f"\n\nTraceback:\n{error_traceback[-500:]}"  # Last 500 chars of traceback
        raise HTTPException(
            status_code=500,
            detail=error_detail
        )

