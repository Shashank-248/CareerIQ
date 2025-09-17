from fastapi import APIRouter, HTTPException
from ..schemas.common import ProfileCreate, Profile
from typing import Dict

router = APIRouter()

# In-memory store for prototype (stateless server aside from runtime memory)
PROFILES: Dict[str, Profile] = {}

@router.post("/create", response_model=Profile)
async def create_profile(payload: ProfileCreate):
    if payload.user_id in PROFILES:
        return PROFILES[payload.user_id]
    profile = Profile(**payload.model_dump())
    PROFILES[payload.user_id] = profile
    return profile

@router.get("/{user_id}", response_model=Profile)
async def get_profile(user_id: str):
    if user_id not in PROFILES:
        raise HTTPException(status_code=404, detail="Profile not found")
    return PROFILES[user_id]
