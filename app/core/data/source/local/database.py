from sqlalchemy.engine import URL, create_engine
from app.core.config.env_config import EnvConfig
from sqlalchemy.orm import sessionmaker

from app.core.data.source.local.base import Base


class Database:
    def __init__(self, config: EnvConfig):
        url = URL.create(
            drivername="postgresql+psycopg2",
            username=config.db_user,
            password=config.db_password,
            host=config.db_host,
            port=config.db_port,
            database=config.db_name,
        )
        self.engine = create_engine(url, echo=True)
        self.session = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)
        self.Base = Base()
