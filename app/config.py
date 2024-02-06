"""_summary_
"""

from pydantic_settings import BaseSettings
from functools import lru_cache

from app.logger import get_logger

log = get_logger()


class Settings(BaseException):
    """_summary_

    Args:
        BaseException (_type_): _description_
    """
    environment: str = "dev"
    testing: bool = bool(0)


@lru_cache()
def get_settings() -> BaseException:
    """_summary_
    use lru_cache to cache the settings so get_settings is only called once

    Returns:
        BaseSettings: _description_
    """
    log.info("Loading config settings from the environment...")
    return Settings()
