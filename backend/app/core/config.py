from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "CareerIQ Backend"
    api_v1_prefix: str = "/api/v1"
    environment: str = "dev"
    encryption_key: str = "dev-change-me"  # For prototype only
    allow_origins: list[str] = ["*"]
    model_server_primary: str = "http://192.168.1.100:11434"
    model_server_secondary: str = "http://192.168.1.101:11434"

    class Config:
        env_file = ".env"
        # Avoid warning about protected namespace 'model_'
        protected_namespaces = ("settings_",)

@lru_cache
def get_settings() -> Settings:
    return Settings()
