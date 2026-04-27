import time
from typing import Dict

class TokenBlacklist:
    def __init__(self):
        self._revoked_jti: Dict[str, float] = {}
        
    def revoke(self, jti: str, expires_at: float) -> None:
        self._revoked_jti[jti] = expires_at
        
    def is_revoked(self, jti: str) -> bool:
        if jti not in self._revoked_jti:
            return False
        exp = self._revoked_jti[jti]
        if time.time() > exp:
            del self._revoked_jti[jti]
            return False
        return True
