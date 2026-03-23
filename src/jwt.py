from typing import Dict, Any, Optional
from src.token.parser import JWTParser
from src.crypto.hs256 import sign_hs256, verify_hs256
from src.validator.claims import ClaimsValidator
from src.utils.b64 import json_b64encode
from src.core.exceptions import InvalidSignatureError

class JWTKeymaster:
    def __init__(self, secret: str = "", leeway: int = 0):
        self.secret = secret
        self.claims_validator = ClaimsValidator(leeway_seconds=leeway)
        
    def encode(self, payload: Dict[str, Any], headers: Optional[Dict[str, Any]] = None) -> str:
        h = headers or {"alg": "HS256", "typ": "JWT"}
        h_b64 = json_b64encode(h)
        p_b64 = json_b64encode(payload)
        signing_input = f"{h_b64}.{p_b64}"
        sig = sign_hs256(signing_input, self.secret)
        return f"{signing_input}.{sig}"
        
    def decode(self, token: str, verify_sig: bool = True, expected_issuer: Optional[str] = None, expected_audience: Optional[str] = None) -> Dict[str, Any]:
        parts = token.strip().split(".")
        if len(parts) != 3:
            raise ValueError("Invalid JWT format")
        signing_input = f"{parts[0]}.{parts[1]}"
        sig = parts[2]
        
        if verify_sig:
            if not verify_hs256(signing_input, sig, self.secret):
                raise InvalidSignatureError("Signature mismatch")
                
        hdr, payload, _ = JWTParser.parse_unverified(token)
        self.claims_validator.validate(payload, expected_issuer=expected_issuer, expected_audience=expected_audience)
        return payload
