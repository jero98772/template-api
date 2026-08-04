# <Name> - jero98772

import logging
from collections.abc import Sequence

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    # FASTAPI SETTINGS
    TITLE: str = "<NAME>"
    VERSION: str = "1.0.0"

    OPENAPI_URL: str = "/api/openapi.json"
    DOCS_URL: str = "/api/docs"
    REDOCS_URL: str = "/api/redocs"

    # PRINT LOGS
    ENABLE_LOGS: bool = True

    CORS_ALLOWED_ORIGINS: Sequence[str] = []


def setup_logging(settings: AppSettings) -> None:
    if not settings.ENABLE_LOGS:
        logging.disable(logging.CRITICAL)
    else:
        logging.disable(logging.NOTSET)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    )
