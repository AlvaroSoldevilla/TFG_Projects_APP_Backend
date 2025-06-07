from pydantic_settings import BaseSettings


class Config(BaseSettings):
    database_type: str = "sqlite"
    postgres_user: str = "your_postgres_user"
    postgres_password: str = "your_postgres_password"
    postgres_db: str = "your_postgres_db"
    db_host: str = "db"
    secret: str = "your_secret_token_password"
    algorithm: str = "HS256"

    debug: bool = False

    class Config:
        env_file = ".env"


config = Config()
