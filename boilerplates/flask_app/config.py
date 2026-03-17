from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str = ""
    openrouter_api_key: str = ""
    gemini_api_key: str = ""
    database_url: str = "sqlite:///./app.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
