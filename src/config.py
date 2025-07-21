from pydantic_settings import BaseSettings, SettingsConfigDict

from typing import Optional
from pathlib import Path


class Settings(BaseSettings):
    PROJECT_NAME: str = "Bring Your Own Agent"
    API_PREFIX: str = "/api/v1"
    DATABASE_URI: Optional[str] = None

    # OpenAI
    OPENAI_BASE_URL: str = "https://api.openai-proxy.org/v1"
    OPENAI_API_KEY: str = "sk-AckdnEtpQ1Cy49EeUXabScHHx4kPIWj1jAouyO68mW8Pso59"
    OPENAI_MODEL: str = "gpt-4.1-nano"

    IS_LOCAL: bool = True
    DEBUG_MODE: bool = True

    model_config = SettingsConfigDict(
        env_prefix="DEV_",  # 默认开发环境
        env_file_encoding="utf-8",
        extra="ignore",  # 忽略未定义变量
    )


settings = Settings()

print(settings.OPENAI_API_KEY)
