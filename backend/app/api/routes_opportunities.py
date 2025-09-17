from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter()

class Opportunity(BaseModel):
    id: str
    title: str
    company: str
    match_score: int
    url: str

MOCK_OPPS = [
    Opportunity(id=str(uuid.uuid4()), title="Data Analyst Intern", company="StartupX", match_score=82, url="https://example.com/1"),
    Opportunity(id=str(uuid.uuid4()), title="Junior Python Developer", company="TechNova", match_score=76, url="https://example.com/2"),
    Opportunity(id=str(uuid.uuid4()), title="Product Management Fellow", company="InnovateHub", match_score=71, url="https://example.com/3"),
]

@router.get("/list", response_model=List[Opportunity])
async def list_opportunities():
    return MOCK_OPPS
