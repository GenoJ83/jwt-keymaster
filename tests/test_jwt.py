import time
import pytest
from src.jwt import JWTKeymaster
from src.core.exceptions import InvalidSignatureError

def test_jwt_encode_decode():
    km = JWTKeymaster(secret="topsecret")
    payload = {"sub": "alice", "role": "admin", "exp": time.time() + 600}
    token = km.encode(payload)
    
    decoded = km.decode(token)
    assert decoded["sub"] == "alice"
    assert decoded["role"] == "admin"
    
    bad_km = JWTKeymaster(secret="wrongsecret")
    with pytest.raises(InvalidSignatureError):
        bad_km.decode(token)
