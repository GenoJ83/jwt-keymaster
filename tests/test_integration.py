import time
from src.jwt import JWTKeymaster
from src.jwks.keyset import JWKSManager
from src.audit.scanner import JWTSecurityAuditor

def test_full_jwt_suite():
    km = JWTKeymaster("corp_secret")
    tok = km.encode({"sub": "usr_999", "role": "editor", "exp": time.time() + 300})
    dec = km.decode(tok)
    assert dec["sub"] == "usr_999"
    
    hdr, pld, _ = km.decode(tok, verify_sig=False), dec, None
    warnings = JWTSecurityAuditor.audit_token({"alg": "HS256"}, dec)
    assert len(warnings) == 0
