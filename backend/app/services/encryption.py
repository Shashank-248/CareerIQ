from cryptography.fernet import Fernet
from typing import Optional
import base64, hashlib

class EncryptionService:
    def __init__(self, master_key: str):
        # Derive 32-byte key
        digest = hashlib.sha256(master_key.encode()).digest()
        self._fernet = Fernet(base64.urlsafe_b64encode(digest))

    def encrypt(self, data: bytes) -> bytes:
        return self._fernet.encrypt(data)

    def decrypt(self, token: bytes) -> bytes:
        return self._fernet.decrypt(token)

# Prototype global instance (stateless server, future: per-user key derivation)
