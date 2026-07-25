from __future__ import annotations

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_deepseek import ChatDeepSeek

from .config import Settings


class ProviderError(RuntimeError):
    """Raised when the configured LangChain model cannot be created."""


def create_deepseek_model(settings: Settings) -> BaseChatModel:
    """Create the required LangChain DeepSeek integration with explicit behavior."""
    settings.require_provider()
    if settings.llm_provider != "deepseek":
        raise ValueError(f"Unsupported provider: {settings.llm_provider}")

    try:
        return ChatDeepSeek(
            model=settings.llm_model,
            api_key=settings.llm_api_key,
            base_url=settings.llm_base_url,
            temperature=settings.llm_temperature,
            timeout=settings.llm_timeout_seconds,
            max_retries=0,
            max_tokens=settings.llm_max_output_tokens,
            streaming=False,
            extra_body={
                "thinking": {
                    "type": "enabled" if settings.llm_thinking else "disabled"
                }
            },
        )
    except Exception as exc:
        raise ProviderError(f"Could not configure ChatDeepSeek: {exc}") from exc
