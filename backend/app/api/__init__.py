from fastapi import APIRouter
from . import routes_profile, routes_chat, routes_device, routes_skills, routes_opportunities, routes_challenges, routes_parsing, routes_gamification, routes_system

api_router = APIRouter()
api_router.include_router(routes_device.router, prefix="/device", tags=["device"])
api_router.include_router(routes_profile.router, prefix="/profile", tags=["profile"])
api_router.include_router(routes_skills.router, prefix="/skills", tags=["skills"])
api_router.include_router(routes_chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(routes_opportunities.router, prefix="/opportunities", tags=["opportunities"])
api_router.include_router(routes_challenges.router, prefix="/challenges", tags=["challenges"])
api_router.include_router(routes_parsing.router, prefix="/parse", tags=["parsing"])
api_router.include_router(routes_gamification.router, prefix="/gamification", tags=["gamification"])
api_router.include_router(routes_system.router, tags=["system"])
