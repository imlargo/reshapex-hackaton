import pytest
from langchain_anthropic import ChatAnthropic
from langchain_deepseek import ChatDeepSeek

from agentsprint_starter.config import Settings
from agentsprint_starter.provider import create_anthropic_model, create_chat_model, create_deepseek_model


def test_chatdeepseek_receives_v4_and_explicit_non_thinking_configuration() -> None:
    settings = Settings(
        _env_file=None,
        llm_api_key="test-key",
        llm_model="deepseek-v4-flash",
        llm_base_url="https://api.deepseek.com",
        llm_thinking=False,
        llm_max_output_tokens=1800,
    )

    model = create_deepseek_model(settings)

    assert isinstance(model, ChatDeepSeek)
    assert model.model_name == "deepseek-v4-flash"
    assert model.openai_api_base == "https://api.deepseek.com"
    assert model.extra_body == {"thinking": {"type": "disabled"}}
    assert model.max_tokens == 1800


def test_chatdeepseek_configuration_requires_a_key() -> None:
    settings = Settings(_env_file=None, llm_api_key="", llm_provider="deepseek")

    with pytest.raises(ValueError, match="LLM_API_KEY"):
        create_deepseek_model(settings)


def test_chatanthropic_receives_model_and_key() -> None:
    settings = Settings(
        _env_file=None,
        llm_provider="anthropic",
        llm_model="claude-sonnet-4-20250514",
        claude_api_key="test-claude-key",
        llm_max_output_tokens=1800,
    )

    model = create_anthropic_model(settings)

    assert isinstance(model, ChatAnthropic)
    assert model.model == "claude-sonnet-4-20250514"
    assert model.max_tokens == 1800


def test_create_chat_model_selects_provider() -> None:
    anthropic_settings = Settings(
        _env_file=None,
        llm_provider="anthropic",
        llm_model="claude-sonnet-4-20250514",
        claude_api_key="test-claude-key",
    )
    assert isinstance(create_chat_model(anthropic_settings), ChatAnthropic)
