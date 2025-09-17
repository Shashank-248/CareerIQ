import httpx
from typing import Optional, Dict
from ..core.config import get_settings

settings = get_settings()

class OllamaClient:
    def __init__(self, timeout: float = 60.0):
        self.timeout = timeout

    async def generate(self, model: str, prompt: str) -> str:
        # Decide which server based on model weight
        base = settings.model_server_primary
        if model.startswith("smollm"):
            # attempt secondary first
            base = settings.model_server_secondary or settings.model_server_primary
        url = f"{base}/api/generate"
        payload = {"model": model, "prompt": prompt, "stream": False}
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                r = await client.post(url, json=payload)
                r.raise_for_status()
                data = r.json()
                # Ollama returns {'response': '...'}
                return data.get("response", "")
            except Exception as e:
                # Fallback attempt to localhost if not already localhost
                if "127.0.0.1" not in base and "localhost" not in base:
                    try:
                        fallback_url = "http://127.0.0.1:11434/api/generate"
                        r2 = await client.post(fallback_url, json=payload)
                        r2.raise_for_status()
                        data2 = r2.json()
                        return data2.get("response", "") + " (fallback localhost)"
                    except Exception as e2:
                        return f"(generation error: {e}; localhost fallback: {e2})"
                return f"(generation error: {e})"

ollama_client = OllamaClient()
