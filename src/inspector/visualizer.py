import json
import datetime
from typing import Dict, Any
from src.token.parser import JWTParser

class JWTVisualizer:
    @staticmethod
    def inspect_text(token: str) -> str:
        hdr, pld, sig = JWTParser.parse_unverified(token)
        lines = ["=== HEADER ===", json.dumps(hdr, indent=2), "=== PAYLOAD ==="]
        # annotate timestamps
        pld_copy = dict(pld)
        for t_claim in ["exp", "iat", "nbf"]:
            if t_claim in pld_copy:
                ts = float(pld_copy[t_claim])
                readable = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc).isoformat()
                pld_copy[f"_{t_claim}_human"] = readable
        lines.append(json.dumps(pld_copy, indent=2))
        lines.append(f"=== SIGNATURE ===\n{sig[:16]}... (truncated)")
        return "\n".join(lines)
