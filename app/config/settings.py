from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    AI_MODEL_NAME: str = "llama3.2:1b"

    class Config:
        env_file = ".env"
        extra = "forbid"  # declare secret_key explicitly in Settings


settings = Settings()
