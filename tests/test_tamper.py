import pytest
from src.crypto.tamper import detect_tampering
from src.jwt import JWTKeymaster
from src.core.exceptions import InvalidSignatureError
from src.utils.b64 import json_b64encode

def test_tampering_caught():
    km = JWTKeymaster(secret="secret456")
    tok = km.encode({"sub": "user"})
    tampered = detect_tampering(tok, json_b64encode({"sub": "admin"}))
    with pytest.raises(InvalidSignatureError):
        km.decode(tampered)
