from pydantic_settings import BaseSettings


class Config(BaseSettings):
    database_type: str = "sqlite"
    postgres_user: str = "projectsapi"
    postgres_password: str = "projectsapi"
    postgres_db: str = "projectsapi"
    db_host: str = "db"

    debug: bool = False

    class Config:
        env_file = ".env"


config = Config()
