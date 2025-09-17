from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class DeviceInfo(BaseModel):
    user_id: str
    ram_mb: int
    cpu_cores: int
    cpu_freq_mhz: Optional[int] = None
    antutu_estimate: Optional[int] = None

class DeviceModelPlan(BaseModel):
    tier: str
    local_models: list[str]
    server_models: list[str]
    override_allowed: bool = True

@router.post("/register", response_model=DeviceModelPlan)
def register_device(info: DeviceInfo):
    # Basic heuristic mapping
    antutu = info.antutu_estimate or (info.cpu_cores * 50000 + info.ram_mb * 50)
    if antutu >= 500000:
        tier = "premium"
        local = ["gemma3:270m", "smollm:135m"]
    elif antutu >= 300000:
        tier = "mid_range"
        local = ["smollm:135m"]
    elif antutu >= 100000:
        tier = "budget"
        local = []
    else:
        tier = "legacy"
        local = []
    server = ["smollm:135m", "gemma3:270m", "llama3.2:1b", "llama3.2:3b"]
    return DeviceModelPlan(tier=tier, local_models=local, server_models=server)
