import hmac
import hashlib
from src.utils.b64 import urlsafe_b64encode, urlsafe_b64decode

def sign_hs256(signing_input: str, secret: str) -> str:
    sig = hmac.new(secret.encode("utf-8"), signing_input.encode("ascii"), hashlib.sha256).digest()
    return urlsafe_b64encode(sig)

def verify_hs256(signing_input: str, signature: str, secret: str) -> bool:
    expected = sign_hs256(signing_input, secret)
    return hmac.compare_digest(expected, signature)
