import secrets
import string

def generate_hmac_secret(length: int = 32) -> str:
    charset = string.ascii_letters + string.digits + "-_.~"
    return "".join(secrets.choice(charset) for _ in range(length))

def generate_key_id(prefix: str = "key") -> str:
    return f"{prefix}_{secrets.token_hex(6)}"
