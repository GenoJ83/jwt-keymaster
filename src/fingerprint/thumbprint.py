import hashlib

def compute_thumbprint(token: str) -> str:
    return hashlib.sha256(token.encode("ascii")).hexdigest()[:16]
