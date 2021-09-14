from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    production_mode: bool = False
    openapi_url: str = "/openapi.json"
    docs_url: Optional[str] = "/docs"
    redoc_url: Optional[str] = None


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
