# LLM Provider Compatibility Layer

## Overview

A compatibility layer that abstracts LLM provider implementations (OpenAI, Anthropic Claude) behind a common interface, allowing easy switching between providers via configuration.

## Benefits

### ✅ Provider Flexibility
- Switch between OpenAI GPT-4o and Anthropic Claude via environment variable
- No code changes required to switch providers
- Easy to add new providers in the future

### ✅ A/B Testing & Comparison
- Compare performance, quality, and cost between providers
- Test different models side-by-side
- Make data-driven decisions about which provider to use

### ✅ Fallback & Resilience
- Automatic failover if one provider has issues
- Redundancy for critical production systems
- Graceful degradation

### ✅ Cost Optimization
- Route different query types to different providers
- Use cheaper models for simple queries, premium models for complex ones
- Monitor and optimize costs per provider

### ✅ Future-Proofing
- Easy to add new providers (Gemini, Mistral, etc.)
- Centralized provider management
- Consistent interface across providers

## Architecture

```
┌─────────────────────────────────────┐
│         RAG Pipeline                │
│  (rag.py)                           │
│                                     │
│  Uses: LLMProvider interface       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│    LLM Compatibility Layer           │
│  (services/llm_provider.py)          │
│                                     │
│  - LLMProvider (abstract)           │
│  - OpenAIProvider                   │
│  - AnthropicProvider                │
└──────────────┬──────────────────────┘
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
┌─────────────┐  ┌──────────────┐
│   OpenAI    │  │  Anthropic   │
│   GPT-4o    │  │   Claude     │
└─────────────┘  └──────────────┘
```

## Implementation

### 1. Provider Interface

All providers implement the `LLMProvider` interface:

```python
class LLMProvider(ABC):
    def get_chat_model(self) -> BaseChatModel
    def get_provider_name(self) -> str
    def get_model_name(self) -> str
```

### 2. Configuration

Add to `.env`:

```bash
# LLM Provider Selection
LLM_PROVIDER=openai  # or 'anthropic'

# OpenAI (required if LLM_PROVIDER=openai)
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o

# Anthropic (required if LLM_PROVIDER=anthropic)
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# Embeddings (can use OpenAI even with Claude LLM)
EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=text-embedding-3-small
```

### 3. Usage in RAG Pipeline

```python
from ..services.llm_provider import create_llm_provider

# Initialize provider
llm_provider = create_llm_provider(
    provider=settings.llm_provider,
    api_key=settings.openai_api_key if settings.llm_provider == "openai" else settings.anthropic_api_key,
    model=settings.openai_model if settings.llm_provider == "openai" else settings.anthropic_model,
    temperature=settings.temperature,
    max_tokens=settings.max_tokens,
)

# Get LangChain chat model (works with both providers)
self.llm = llm_provider.get_chat_model()
```

## Important Considerations

### Embeddings

**Note:** Anthropic Claude does not provide embeddings. You should continue using OpenAI embeddings (`text-embedding-3-small`) even when using Claude as the LLM. This is fine because:

- Embeddings are used for semantic search (finding relevant documents)
- LLM is used for response generation (synthesizing answers)
- These are separate concerns and can use different providers

### Prompt Compatibility

Both OpenAI and Anthropic support:
- System messages
- User messages
- Chat history

However, there may be subtle differences:
- Token limits
- Response formats
- Special instructions handling

Test prompts with both providers to ensure compatibility.

### Cost Comparison

| Provider | Model | Input Cost | Output Cost | Notes |
|----------|-------|------------|-------------|-------|
| OpenAI | GPT-4o | $2.50/1M | $10/1M | Fast, high quality |
| Anthropic | Claude 3.5 Sonnet | $3/1M | $15/1M | Excellent reasoning |
| Anthropic | Claude 3 Opus | $15/1M | $75/1M | Best quality, slower |

### Performance Comparison

| Provider | Speed | Quality | Best For |
|----------|-------|---------|----------|
| OpenAI GPT-4o | Fast | High | General queries, code generation |
| Claude 3.5 Sonnet | Medium | Very High | Complex reasoning, synthesis |
| Claude 3 Opus | Slower | Highest | Most complex queries |

## Migration Guide

### Step 1: Install Dependencies

```bash
# For Anthropic support
pip install langchain-anthropic
```

### Step 2: Update Configuration

Add to `backend/env.template`:

```bash
LLM_PROVIDER=openai
ANTHROPIC_API_KEY=
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

### Step 3: Update RAG Pipeline

See `backend/src/core/rag_provider_example.py` for the exact changes needed.

### Step 4: Test Both Providers

```bash
# Test with OpenAI
LLM_PROVIDER=openai python -m backend.src.core.rag

# Test with Anthropic
LLM_PROVIDER=anthropic ANTHROPIC_API_KEY=sk-ant-... python -m backend.src.core.rag
```

## Future Enhancements

### 1. Automatic Fallback

```python
def get_llm_with_fallback():
    try:
        return create_llm_provider("openai", ...)
    except Exception:
        logger.warning("OpenAI failed, falling back to Anthropic")
        return create_llm_provider("anthropic", ...)
```

### 2. Provider Selection by Query Type

```python
def select_provider_for_query(query: str) -> str:
    if is_complex_reasoning_query(query):
        return "anthropic"  # Claude better for complex reasoning
    else:
        return "openai"  # GPT-4o faster for simple queries
```

### 3. Cost Tracking

```python
class LLMProviderWithCostTracking(LLMProvider):
    def track_usage(self, tokens_in: int, tokens_out: int):
        # Track costs per provider
        pass
```

### 4. A/B Testing

```python
def get_llm_for_ab_test(user_id: str) -> LLMProvider:
    # Route 50% to OpenAI, 50% to Anthropic
    if hash(user_id) % 2 == 0:
        return create_llm_provider("openai", ...)
    else:
        return create_llm_provider("anthropic", ...)
```

## Recommendations

1. **Start with OpenAI**: Keep using GPT-4o as default (it's proven and fast)
2. **Test Claude**: Try Claude 3.5 Sonnet for complex queries to compare
3. **Monitor Costs**: Track costs for both providers
4. **Measure Quality**: Compare response quality and user satisfaction
5. **Use Hybrid Approach**: Consider using different providers for different query types

## Conclusion

The compatibility layer provides flexibility without adding significant complexity. It's a good architectural decision that:

- ✅ Maintains backward compatibility (defaults to OpenAI)
- ✅ Requires minimal code changes
- ✅ Provides clear benefits (flexibility, testing, fallback)
- ✅ Is easy to extend with new providers

**Recommendation: Yes, implement the compatibility layer.** It's a low-risk, high-value addition that future-proofs your architecture.
