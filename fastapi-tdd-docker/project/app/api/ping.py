from typing import Dict

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)) -> Dict[str, str]:
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
