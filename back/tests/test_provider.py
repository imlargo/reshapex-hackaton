import pytest
from langchain_deepseek import ChatDeepSeek

from agentsprint_starter.config import Settings
from agentsprint_starter.provider import create_deepseek_model


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
    settings = Settings(_env_file=None, llm_api_key="")

    with pytest.raises(ValueError, match="LLM_API_KEY"):
        create_deepseek_model(settings)
