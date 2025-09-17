from fastapi import APIRouter
from pydantic import BaseModel
import uuid
from typing import List

router = APIRouter()

class Challenge(BaseModel):
    id: str
    topic: str
    question: str
    difficulty: str

@router.get("/daily", response_model=List[Challenge])
async def get_daily():
    # Placeholder fixed set
    return [
        Challenge(id=str(uuid.uuid4()), topic="sql", question="What does SELECT * do?", difficulty="easy"),
        Challenge(id=str(uuid.uuid4()), topic="python", question="Explain list comprehension.", difficulty="medium"),
    ]
