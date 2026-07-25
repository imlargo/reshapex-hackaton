from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    llm_provider: Literal["deepseek"] = "deepseek"
    llm_model: str = "deepseek-v4-flash"
    llm_api_key: str = ""
    llm_base_url: str = "https://api.deepseek.com"
    llm_temperature: float = 0.0
    llm_timeout_seconds: float = Field(default=60.0, gt=0)
    llm_max_output_tokens: int = Field(default=1800, ge=256, le=16000)
    llm_thinking: bool = False

    agent_max_steps: int = Field(default=6, ge=2, le=12)
    agent_max_retries: int = Field(default=1, ge=0, le=1)
    tool_timeout_seconds: float = Field(default=8.0, gt=0, le=60)

    @property
    def provider_is_configured(self) -> bool:
        return bool(self.llm_api_key.strip() and self.llm_model.strip())

    def require_provider(self) -> None:
        if not self.provider_is_configured:
            raise ValueError(
                "DeepSeek is not configured. Copy .env.example to .env and set LLM_API_KEY."
            )


@lru_cache
def get_settings() -> Settings:
    return Settings()
