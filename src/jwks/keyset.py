from typing import Dict, Any, List, Optional
import time

class JWKSManager:
    def __init__(self, cache_ttl: int = 3600):
        self.keys: Dict[str, Dict[str, Any]] = {}
        self.last_fetch: float = 0.0
        self.cache_ttl = cache_ttl
        
    def register_key(self, kid: str, kty: str, alg: str, public_material: str) -> None:
        self.keys[kid] = {
            "kid": kid,
            "kty": kty,
            "alg": alg,
            "pub": public_material,
            "registered_at": time.time()
        }
        
    def get_key(self, kid: str) -> Optional[Dict[str, Any]]:
        return self.keys.get(kid)
        
    def export_jwks(self) -> Dict[str, List[Dict[str, Any]]]:
        return {"keys": list(self.keys.values())}
