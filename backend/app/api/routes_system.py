from fastapi import APIRouter
import httpx
from ..core.config import get_settings

router = APIRouter()
settings = get_settings()

async def _probe(host: str, model: str = "gemma3:270m"):
    url = f"{host}/api/generate"
    payload = {"model": model, "prompt": "ping", "stream": False}
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.post(url, json=payload)
            r.raise_for_status()
            return {"host": host, "ok": True}
    except Exception as e:
        return {"host": host, "ok": False, "error": str(e)}

@router.get("/system/model/health")
async def model_health():
    primary = await _probe(settings.model_server_primary)
    secondary = await _probe(settings.model_server_secondary) if settings.model_server_secondary else None
    localhost = await _probe("http://127.0.0.1:11434")
    return {"primary": primary, "secondary": secondary, "localhost": localhost}
