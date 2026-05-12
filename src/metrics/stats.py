from typing import Dict, Any

class JWTStats:
    def __init__(self):
        self.verified_ok = 0
        self.expired_count = 0
        self.invalid_sig_count = 0
        
    def record_ok(self): self.verified_ok += 1
    def record_expired(self): self.expired_count += 1
    def record_invalid_sig(self): self.invalid_sig_count += 1
    
    def export(self) -> Dict[str, int]:
        return {
            "ok": self.verified_ok,
            "expired": self.expired_count,
            "invalid_sig": self.invalid_sig_count
        }
