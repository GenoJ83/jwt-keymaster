from src.audit.scanner import JWTSecurityAuditor

def test_security_audit():
    w1 = JWTSecurityAuditor.audit_token({"alg": "none"}, {"sub": "1"})
    assert any("CRITICAL" in w for w in w1)
    
    w2 = JWTSecurityAuditor.audit_token({"alg": "HS256"}, {"sub": "1", "exp": 1000})
    assert not any("CRITICAL" in w for w in w2)
