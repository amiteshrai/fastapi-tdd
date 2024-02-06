"""_summary_
"""

from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import AnyUrl

from api.logger import get_logger

log = get_logger()


class Settings(BaseException):
    """_summary_

    Args:
        BaseException (_type_): _description_
    """
    environment: str = "dev"
    testing: bool = bool(0)
    database_url: AnyUrl = None


@lru_cache()
def get_settings() -> BaseException:
    """_summary_
    use lru_cache to cache the settings so get_settings is only called once

    Returns:
        BaseSettings: _description_
    """
    log.info("Loading config settings from the environment...")
    return Settings()
