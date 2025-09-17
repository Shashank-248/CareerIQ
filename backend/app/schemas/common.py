from pydantic import BaseModel, Field
from typing import List, Optional
import uuid

class Message(BaseModel):
    role: str
    content: str

class Skill(BaseModel):
    name: str
    score: int = Field(ge=0, le=100)  # 0-100 scale
    evidence: List[str] = []  # sources: resume, chat:<id>, quiz:<id>
    last_updated: Optional[str] = None

class CareerPath(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: Optional[str] = None
    relevance: int = Field(ge=0, le=100, default=0)
    required_skills: List[str] = []

class Opportunity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    match_score: int = Field(ge=0, le=100, default=0)
    source: Optional[str] = None
    url: Optional[str] = None

class Challenge(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    question: str
    topic: str
    difficulty: str = "easy"
    expected_answer: Optional[str] = None

class ChallengeResult(BaseModel):
    challenge_id: str
    correct: bool
    score_delta: int
    skill_impacts: List[str] = []

class ChatRequest(BaseModel):
    user_id: str
    query: str
    language: str = "en"

class ChatResponse(BaseModel):
    answer: str
    used_model: str
    citations: List[str] = []

class ProfileCreate(BaseModel):
    user_id: str
    name: Optional[str] = None
    degree: Optional[str] = None
    semester: Optional[str] = None
    interests: List[str] = []
    language: str = "en"
    nickname: Optional[str] = None

class Profile(ProfileCreate):
    skills: List[Skill] = []
    career_paths: List[CareerPath] = []
