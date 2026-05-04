import time
from typing import Optional, Tuple
from src.generator.secret import generate_hmac_secret, generate_key_id

class KeyRotator:
    def __init__(self, rotation_interval_seconds: int = 86400):
        self.interval = rotation_interval_seconds
        self.active_kid = generate_key_id("rot")
        self.active_secret = generate_hmac_secret()
        self.rotated_at = time.time()
        self.retired_keys = {}
        
    def should_rotate(self) -> bool:
        return (time.time() - self.rotated_at) >= self.interval
        
    def rotate(self) -> Tuple[str, str]:
        self.retired_keys[self.active_kid] = self.active_secret
        self.active_kid = generate_key_id("rot")
        self.active_secret = generate_hmac_secret()
        self.rotated_at = time.time()
        return self.active_kid, self.active_secret
