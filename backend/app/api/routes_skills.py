from fastapi import APIRouter, HTTPException
import logging
from pydantic import BaseModel
from typing import List
from ..schemas.common import Skill, Profile
from .routes_profile import PROFILES

router = APIRouter()

class SkillUpsertRequest(BaseModel):
    user_id: str
    skills: List[Skill]

@router.post("/upsert", response_model=List[Skill])
async def upsert_skills(payload: SkillUpsertRequest):
    if payload.user_id not in PROFILES:
        logging.warning(f"Skill upsert for missing profile id={payload.user_id}; existing={list(PROFILES.keys())}")
        raise HTTPException(status_code=404, detail=f"Profile not found: {payload.user_id}. Existing IDs: {list(PROFILES.keys())}")
    profile: Profile = PROFILES[payload.user_id]
    existing = {s.name.lower(): s for s in profile.skills}
    for skill in payload.skills:
        existing[skill.name.lower()] = skill
    profile.skills = list(existing.values())
    return profile.skills

@router.get("/{user_id}", response_model=List[Skill])
async def list_skills(user_id: str):
    if user_id not in PROFILES:
        raise HTTPException(status_code=404, detail=f"Profile not found: {user_id}")
    return PROFILES[user_id].skills
