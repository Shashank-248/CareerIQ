from fastapi import APIRouter, HTTPException
from .routes_profile import PROFILES
from ..services.gamification import GamificationEngine

router = APIRouter()
engine = GamificationEngine()

@router.get("/status/{user_id}")
async def gamification_status(user_id: str):
    if user_id not in PROFILES:
        raise HTTPException(status_code=404, detail="Profile not found")
    profile = PROFILES[user_id]
    return engine.evaluate(profile)
