from src.utils.b64 import urlsafe_b64encode, urlsafe_b64decode, json_b64encode, json_b64decode

def test_b64_roundtrip():
    msg = b"hello jwt world 12345"
    enc = urlsafe_b64encode(msg)
    assert "=" not in enc
    assert urlsafe_b64decode(enc) == msg
    
    payload = {"sub": "user_42", "admin": True}
    b64_str = json_b64encode(payload)
    assert json_b64decode(b64_str) == payload
