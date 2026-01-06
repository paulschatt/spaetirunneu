from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg://spaetirun:spaetirun@localhost:5432/spaetirun"

    class Config:
        env_file = ".env"

settings = Settings()
