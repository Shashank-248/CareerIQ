import asyncio
from httpx import AsyncClient
from app.main import app
import uuid

async def run_flow():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_id = str(uuid.uuid4())
        # Device register
        r = await ac.post("/api/v1/device/register", json={"user_id": user_id, "ram_mb": 4096, "cpu_cores": 4})
        assert r.status_code == 200
        # Create profile
        r = await ac.post("/api/v1/profile/create", json={"user_id": user_id, "name": "Test", "degree": "BTech", "semester": "5", "interests": ["data"], "language": "en"})
        assert r.status_code == 200
        # Upsert skills
        r = await ac.post("/api/v1/skills/upsert", json={"user_id": user_id, "skills": [{"name": "Python", "score": 80, "evidence": ["resume"]}]})
        assert r.status_code == 200
        # Chat
        r = await ac.post("/api/v1/chat/ask", json={"user_id": user_id, "query": "Suggest careers", "language": "en", "device_tier": "mid_range"})
        assert r.status_code == 200
        # Opportunities
        r = await ac.get("/api/v1/opportunities/list")
        assert r.status_code == 200
        # Challenges
        r = await ac.get("/api/v1/challenges/daily")
        assert r.status_code == 200

if __name__ == "__main__":
    asyncio.run(run_flow())
