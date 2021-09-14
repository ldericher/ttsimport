from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    production_mode: bool = False
    openapi_url: str = "/openapi.json"
    docs_url: Optional[str] = "/docs"
    redoc_url: Optional[str] = None


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "mycoolapp"
    LOG_FORMAT: str = "%(levelname)s in %(name)s (#%(process)d): %(message)s"
    LOG_LEVEL: str = "DEBUG" if not settings.production_mode else "INFO"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "ttsimport": {"handlers": ["default"], "level": LOG_LEVEL},
    }


@lru_cache
def get_log_config() -> LogConfig:
    return LogConfig()


log_config = get_log_config()

