from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    TESTING: bool = False
    
    class Config:
        env_file = "brilliant-api/.env"

settings = Settings()