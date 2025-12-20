from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"
        extra = "forbid"  # declare secret_key explicitly in Settings


settings = Settings()
