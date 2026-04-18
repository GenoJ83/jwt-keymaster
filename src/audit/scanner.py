from typing import Dict, Any, List

class JWTSecurityAuditor:
    @staticmethod
    def audit_token(header: Dict[str, Any], payload: Dict[str, Any]) -> List[str]:
        warnings = []
        alg = header.get("alg", "").lower()
        if alg in ["none", ""]: 
            warnings.append("CRITICAL: Insecure alg none accepted or missing algorithm.")
        if "exp" not in payload:
            warnings.append("WARNING: Token lacks an expiration (exp) claim.")
        elif payload["exp"] - payload.get("iat", payload["exp"]) > 86400 * 30:
            warnings.append("WARNING: Token expiration exceeds 30 days.")
        if header.get("jku") or header.get("x5u"):
            warnings.append("NOTICE: Remote key URL headers present; ensure domain allowlisting.")
        return warnings
