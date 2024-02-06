"""
 fastapi-tdd/app/main.py
"""

from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()


@app.get('/ping')
def pong(settings: Settings = Depends(get_settings)):
    """_summary_

    Returns:
        _type_: _description_
    """
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
