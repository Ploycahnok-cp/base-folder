from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["users"])

@router.get("/ping")
async def check_connection():
    return {"msg": "pong", "code": 200}
