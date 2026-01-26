"""
LLM Provider Compatibility Layer

Abstracts LLM provider implementations (OpenAI, Anthropic Claude) behind a common interface.
Allows switching between providers via configuration without changing RAG pipeline code.
"""

import logging
from typing import Optional, List, Dict, Any
from abc import ABC, abstractmethod

from langchain.schema import BaseMessage, HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate

logger = logging.getLogger(__name__)


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    @abstractmethod
    def get_chat_model(self) -> Any:
        """Get the LangChain chat model instance."""
        pass
    
    @abstractmethod
    def get_provider_name(self) -> str:
        """Get the provider name (e.g., 'openai', 'anthropic')."""
        pass
    
    @abstractmethod
    def get_model_name(self) -> str:
        """Get the model name being used."""
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI GPT provider implementation."""
    
    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4o",
        temperature: float = 0.0,
        max_tokens: Optional[int] = None,
    ):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._chat_model: Optional[Any] = None
    
    def get_chat_model(self) -> Any:
        """Get OpenAI ChatOpenAI instance."""
        if self._chat_model is None:
            from langchain_openai import ChatOpenAI
            
            self._chat_model = ChatOpenAI(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                openai_api_key=self.api_key,
            )
            logger.info(f"Initialized OpenAI provider with model: {self.model}")
        
        return self._chat_model
    
    def get_provider_name(self) -> str:
        return "openai"
    
    def get_model_name(self) -> str:
        return self.model


class AnthropicProvider(LLMProvider):
    """Anthropic Claude provider implementation."""
    
    def __init__(
        self,
        api_key: str,
        model: str = "claude-3-5-sonnet-20241022",
        temperature: float = 0.0,
        max_tokens: Optional[int] = None,
    ):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._chat_model: Optional[Any] = None
    
    def get_chat_model(self) -> Any:
        """Get Anthropic ChatAnthropic instance using direct SDK integration."""
        if self._chat_model is None:
            try:
                from anthropic import Anthropic
                from langchain.schema import HumanMessage, SystemMessage, AIMessage
                from langchain.schema import ChatGeneration, ChatResult
                from langchain_core.language_models.chat_models import BaseChatModel
                from typing import Any, List, Optional, Dict
                
                # Create a simple wrapper class compatible with LangChain 0.1.20
                class AnthropicChatWrapper(BaseChatModel):
                    """Wrapper for Anthropic SDK to work with LangChain 0.1.x"""
                    
                    def __init__(self, client: Anthropic, model: str, temperature: float, max_tokens: Optional[int]):
                        super().__init__()
                        # Use object.__setattr__ to bypass Pydantic validation for these attributes
                        object.__setattr__(self, '_client', client)
                        object.__setattr__(self, '_model_name', model)
                        object.__setattr__(self, '_temperature_value', temperature)
                        object.__setattr__(self, '_max_tokens_value', max_tokens)
                    
                    @property
                    def _llm_type(self) -> str:
                        return "anthropic"
                    
                    def _generate(
                        self,
                        messages: List[Any],
                        stop: Optional[List[str]] = None,
                        **kwargs: Any,
                    ) -> ChatResult:
                        # Convert LangChain messages to Anthropic format
                        system_message = None
                        anthropic_messages = []
                        
                        for msg in messages:
                            if isinstance(msg, SystemMessage):
                                system_message = msg.content
                            elif isinstance(msg, HumanMessage):
                                anthropic_messages.append({"role": "user", "content": msg.content})
                            elif isinstance(msg, AIMessage):
                                anthropic_messages.append({"role": "assistant", "content": msg.content})
                        
                        # Call Anthropic API
                        response = self._client.messages.create(
                            model=self._model_name,
                            max_tokens=self._max_tokens_value or 4096,
                            temperature=self._temperature_value,
                            system=system_message if system_message else None,
                            messages=anthropic_messages,
                        )
                        
                        # Convert response back to LangChain format
                        text = response.content[0].text if response.content else ""
                        message = AIMessage(content=text)
                        generation = ChatGeneration(message=message)
                        return ChatResult(generations=[generation])
                    
                    def invoke(self, messages: List[Any], **kwargs: Any) -> Any:
                        """Invoke method for LangChain compatibility."""
                        result = self._generate(messages, **kwargs)
                        # Return the message object (which has .content attribute)
                        return result.generations[0].message
                
                # Create Anthropic client
                client = Anthropic(api_key=self.api_key)
                self._chat_model = AnthropicChatWrapper(
                    client=client,
                    model=self.model,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )
                logger.info(f"Initialized Anthropic provider with direct SDK, model: {self.model}")
            except ImportError as e:
                raise ImportError(
                    "Anthropic SDK is required for Claude support. "
                    "Install it with: pip install anthropic"
                ) from e
        
        return self._chat_model
    
    def get_provider_name(self) -> str:
        return "anthropic"
    
    def get_model_name(self) -> str:
        return self.model


def create_llm_provider(
    provider: str,
    api_key: str,
    model: Optional[str] = None,
    temperature: float = 0.0,
    max_tokens: Optional[int] = None,
) -> LLMProvider:
    """
    Factory function to create LLM provider instances.
    
    Args:
        provider: Provider name ('openai' or 'anthropic')
        api_key: API key for the provider
        model: Model name (optional, uses defaults if not provided)
        temperature: Temperature setting
        max_tokens: Max tokens setting
        
    Returns:
        LLMProvider instance
        
    Raises:
        ValueError: If provider is not supported
    """
    provider = provider.lower()
    
    if provider == "openai":
        return OpenAIProvider(
            api_key=api_key,
            model=model or "gpt-4o",
            temperature=temperature,
            max_tokens=max_tokens,
        )
    elif provider == "anthropic":
        return AnthropicProvider(
            api_key=api_key,
            model=model or "claude-3-5-sonnet-20241022",
            temperature=temperature,
            max_tokens=max_tokens,
        )
    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}. "
            f"Supported providers: 'openai', 'anthropic'"
        )
