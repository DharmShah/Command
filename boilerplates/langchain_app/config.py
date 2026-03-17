from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str = ""
    openrouter_api_key: str = ""
    gemini_api_key: str = ""
    model_provider: str = "openai"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
