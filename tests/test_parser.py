import pytest
from src.token.parser import JWTParser
from src.core.exceptions import MalformedTokenError
from src.utils.b64 import json_b64encode

def test_parse_token():
    h = json_b64encode({"alg": "HS256", "typ": "JWT"})
    p = json_b64encode({"sub": "alice", "iat": 1700000000})
    token = f"{h}.{p}.fakesig"
    hdr, payload, sig = JWTParser.parse_unverified(token)
    assert hdr["alg"] == "HS256"
    assert payload["sub"] == "alice"
    assert sig == "fakesig"
    
    with pytest.raises(MalformedTokenError):
        JWTParser.parse_unverified("invalid.token")
