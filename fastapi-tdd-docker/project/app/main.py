from fastapi import FastAPI, Depends
from typing import Dict

from app.config import get_settings, Settings


app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)) -> Dict[str, str]:
    return {
        'ping': 'pong!',
        'environment': settings.environment,
        'testing': settings.testing
    }
