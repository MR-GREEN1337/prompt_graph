from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "app_"
    
    # OpenAI API
    OPENAI_API_KEY: str

    # Groq
    GROQ_API_KEY: str

    # CORS
    ALLOWED_ORIGINS: list[str]
    SECRET_KEY: str

settings = AppSettings() # type: ignore[call-arg]