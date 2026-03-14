from typing import Dict, Any, Tuple
from src.core.exceptions import MalformedTokenError
from src.utils.b64 import json_b64decode

class JWTParser:
    @staticmethod
    def parse_unverified(token: str) -> Tuple[Dict[str, Any], Dict[str, Any], str]:
        parts = token.strip().split(".")
        if len(parts) != 3:
            raise MalformedTokenError(f"JWT must contain exactly 3 segments, found {len(parts)}")
        header_b64, payload_b64, signature = parts
        try:
            header = json_b64decode(header_b64)
            payload = json_b64decode(payload_b64)
        except Exception as e:
            raise MalformedTokenError(f"Failed to decode token segments: {e}")
        return header, payload, signature
