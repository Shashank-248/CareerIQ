from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import time

PRIMARY_HEAVY = {"llama3.2:3b", "llama3.2:1b"}
LIGHT_MODELS = {"smollm:135m", "gemma3:270m"}

@dataclass
class ModelDecision:
    model: str
    route: str  # 'primary' | 'secondary' | 'local'
    reason: str

class ModelRouter:
    def __init__(self):
        self.primary_load = 0
        self.secondary_load = 0

    def decide(self, requested: Optional[str], tier: str, allow_local: bool) -> ModelDecision:
        now = time.time()
        # Basic heuristic: if heavy or not allowed local -> server
        if requested in PRIMARY_HEAVY:
            return ModelDecision(model=requested or "llama3.2:1b", route="primary", reason="heavy_model")
        if allow_local and requested in LIGHT_MODELS and tier in {"premium", "mid_range"}:
            return ModelDecision(model=requested, route="local", reason="local_capable")
        # fallback selection
        if tier in {"legacy", "budget"} and requested == "gemma3:270m":
            return ModelDecision(model="gemma3:270m", route="primary", reason="needs_server")
        # default light
        return ModelDecision(model=requested or "smollm:135m", route="secondary", reason="light_distributed")
