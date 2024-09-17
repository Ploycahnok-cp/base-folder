from fastapi import APIRouter, Depends

from app.configs.config import Settings, get_settings
from app.schemas.base import ResponseBase

router = APIRouter(prefix="/api/v1", tags=["network"])


@router.get("/ping", response_model=ResponseBase)
async def check_connection() -> dict:
    return {"msg": "pong"}


@router.get("/settings", response_model=ResponseBase)
async def check_settings(settings: Settings = Depends(get_settings)) -> dict:

    return {
        "data": {
            "env": settings.ENV,
            "log_level": settings.LOG_LEVEL,
        }
    }
