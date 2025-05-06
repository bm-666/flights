from pathlib import Path
from pydantic_settings import BaseSettings

PRODUCTION = False
BASE_DIR = Path(__file__).parent.parent
ENV_FILE = ".env" if PRODUCTION else ".dev.env"
ENV_FILE_PATH = str(BASE_DIR.joinpath(ENV_FILE))

class Config(BaseSettings):
    PSQL_DB: str
    PSQL_USER: str
    PSQL_PASS: str
    PSQL_HOST: str
    PSQL_PORT: str

    class Config:
        env_file = ENV_FILE_PATH

    def get_redis_connect_url(self) -> str:
        return "redis://localhost:6379/0"

    def get_psql_async_connect_url(self) -> str:
        """Получение ссылки подключения к PostgreSQL для асинхронной работы с бд """
        return f"postgresql+asyncpg://{self.PSQL_USER}:{self.PSQL_PASS}@{self.PSQL_HOST}:{self.PSQL_PORT}/{self.PSQL_DB}"

config = Config()