from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.parsing import ResumeParser
from .routes_profile import PROFILES
from ..schemas.common import Skill
from typing import List

router = APIRouter()
parser = ResumeParser()

@router.post("/resume", response_model=List[Skill])
async def parse_resume(user_id: str, file: UploadFile = File(...)):
    if user_id not in PROFILES:
        raise HTTPException(status_code=404, detail="Profile not found")
    content = await file.read()
    text = parser.extract_text(content, file.filename)
    inferred = parser.infer_skills(text)
    # Return as Skill models (scores already 0-100 scale assumption)
    return [Skill(**s) for s in inferred]
