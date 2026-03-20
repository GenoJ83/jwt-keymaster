import time
from typing import Dict, Any, Optional, List
from src.core.exceptions import TokenExpiredError

class ClaimsValidator:
    def __init__(self, leeway_seconds: int = 0):
        self.leeway = leeway_seconds
        
    def validate(self, payload: Dict[str, Any], expected_issuer: Optional[str] = None, expected_audience: Optional[str] = None) -> None:
        now = time.time()
        if "exp" in payload:
            exp = float(payload["exp"])
            if now > (exp + self.leeway):
                raise TokenExpiredError(f"Token expired at {exp}, current time is {now}")
        if "nbf" in payload:
            nbf = float(payload["nbf"])
            if now < (nbf - self.leeway):
                raise ValueError(f"Token not valid before {nbf}")
        if expected_issuer and payload.get("iss") != expected_issuer:
            actual_iss = payload.get("iss")
            raise ValueError(f"Issuer mismatch: expected {expected_issuer}, got {actual_iss}")
        if expected_audience:
            aud = payload.get("aud")
            if isinstance(aud, list) and expected_audience not in aud:
                raise ValueError(f"Audience {expected_audience} not in {aud}")
            elif isinstance(aud, str) and aud != expected_audience:
                raise ValueError(f"Audience mismatch: expected {expected_audience}, got {aud}")
