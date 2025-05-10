from sqlmodel import create_engine, Session
from app.core.config import config


if config.database_type == "sqlite":
    database_url = "sqlite:///./database.db"

    engine = create_engine(database_url, echo=config.debug)

elif config.database_type == "postgres":
    database_url = ("postgresql://{0}:{1}@{2}:5432/{3}"
                    .format(config.postgres_user,
                            config.postgres_password,
                            config.db_host,
                            config.postgres_db))

    engine = create_engine(database_url, echo=config.debug)


def get_session():
    with Session(engine) as session:
        yield session
