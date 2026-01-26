"""
Example: How to update RAG pipeline to use LLM provider compatibility layer.

This shows the changes needed in rag.py to support multiple LLM providers.
"""

# BEFORE (current implementation):
"""
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

def __init__(self):
    # Initialize embeddings
    self.embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        openai_api_key=settings.openai_api_key
    )
    
    # Initialize LLM
    self.llm = ChatOpenAI(
        model=settings.openai_model,
        temperature=settings.temperature,
        max_tokens=settings.max_tokens,
        openai_api_key=settings.openai_api_key
    )
"""

# AFTER (with compatibility layer):
"""
from langchain_openai import OpenAIEmbeddings
from ..services.llm_provider import create_llm_provider

def __init__(self):
    # Initialize embeddings (can still use OpenAI even with Claude LLM)
    self.embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        openai_api_key=settings.openai_api_key
    )
    
    # Initialize LLM using compatibility layer
    # Automatically selects provider based on LLM_PROVIDER env var
    llm_provider_instance = create_llm_provider(
        provider=settings.llm_provider,
        api_key=(
            settings.openai_api_key if settings.llm_provider == "openai"
            else settings.anthropic_api_key or ""
        ),
        model=(
            settings.openai_model if settings.llm_provider == "openai"
            else settings.anthropic_model
        ),
        temperature=settings.temperature,
        max_tokens=settings.max_tokens,
    )
    
    self.llm = llm_provider_instance.get_chat_model()
    self.llm_provider_name = llm_provider_instance.get_provider_name()
    self.llm_model_name = llm_provider_instance.get_model_name()
    
    logger.info(
        f"Initialized LLM: {self.llm_provider_name}/{self.llm_model_name}"
    )
"""
