from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_INITDB_ROOT_USERNAME: str = ""
    MONGO_INITDB_ROOT_PASSWORD: str = ""
    MONGO_INITDB_DATABASE: str = ""
    DATABASE_URL: str = ""


settings = Settings()
