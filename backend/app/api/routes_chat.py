from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from ..schemas.common import ChatRequest, ChatResponse
from .routes_profile import PROFILES
from ..services.model_router import ModelRouter
from ..services.language import TranslationService
from ..services.ollama_client import ollama_client
from .routes_profile import PROFILES

router = APIRouter()
model_router = ModelRouter()
translator = TranslationService()

class ChatRequestExtended(ChatRequest):
    requested_model: Optional[str] = None
    device_tier: Optional[str] = None
    allow_local: bool = True

@router.post("/ask", response_model=ChatResponse)
async def chat(req: ChatRequestExtended):
    if req.user_id not in PROFILES:
        raise HTTPException(status_code=404, detail="Profile not found")
    profile = PROFILES[req.user_id]
    # Language handling
    detection = translator.detect_language(req.query)
    normalized_query = req.query
    if detection != 'en':
        trans = translator.translate(req.query, 'en')
        normalized_query = trans['translated']
    decision = model_router.decide(req.requested_model, req.device_tier or "budget", req.allow_local)
    # Placeholder model response using normalized English query
    # Build lightweight context (skills + interests first few)
    top_skills = sorted(profile.skills, key=lambda s: s.score, reverse=True)[:5]
    skill_summary = ", ".join(f"{s.name}:{s.score}" for s in top_skills) or "None"
    interests = ", ".join(profile.interests[:5]) if profile.interests else "None"
    system_context = (
        "You are CareerIQ, a concise career and skill advisor. "
        "User language may be non-English; respond in same language. "
        f"Known skills (score 0-100): {skill_summary}. Interests: {interests}. "
        "Provide actionable suggestions (careers, next skills, brief resources)."
    )
    generation_prompt = f"{system_context}\n\nUser Query: {normalized_query}\nAnswer:"            
    raw_answer = await ollama_client.generate(decision.model, generation_prompt)
    # If generation failed, provide clearer guidance
    if raw_answer.startswith("(generation error"):
        raw_answer = (
            "Model server unreachable. Ensure Ollama is running and .env MODEL_SERVER_PRIMARY points to the correct host (e.g. http://127.0.0.1:11434). "
            + raw_answer
        )
    # If user language not English translate back
    final_answer = raw_answer
    if detection != 'en':
        back = translator.translate(raw_answer, detection)
        final_answer = back['translated']
    answer = f"[Model {decision.model} via {decision.route}] {final_answer}"
    return ChatResponse(answer=answer, used_model=decision.model, citations=[])
