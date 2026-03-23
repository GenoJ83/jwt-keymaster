import time
import pytest
from src.validator.claims import ClaimsValidator
from src.core.exceptions import TokenExpiredError

def test_claims_validation():
    validator = ClaimsValidator()
    now = time.time()
    valid_p = {"exp": now + 3600, "iss": "auth.example.com", "aud": "api"}
    validator.validate(valid_p, expected_issuer="auth.example.com", expected_audience="api")
    
    expired_p = {"exp": now - 100}
    with pytest.raises(TokenExpiredError):
        validator.validate(expired_p)
        
    wrong_iss = {"exp": now + 100, "iss": "other"}
    with pytest.raises(ValueError):
        validator.validate(wrong_iss, expected_issuer="auth.example.com")
