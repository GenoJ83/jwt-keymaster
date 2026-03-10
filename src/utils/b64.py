import base64
import json
from typing import Any, Dict

def urlsafe_b64encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")

def urlsafe_b64decode(data: str) -> bytes:
    rem = len(data) % 4
    if rem > 0:
        data += "=" * (4 - rem)
    return base64.urlsafe_b64decode(data.encode("ascii"))

def json_b64decode(data: str) -> Dict[str, Any]:
    return json.loads(urlsafe_b64decode(data).decode("utf-8"))

def json_b64encode(obj: Dict[str, Any]) -> str:
    raw = json.dumps(obj, separators=(",", ":")).encode("utf-8")
    return urlsafe_b64encode(raw)
