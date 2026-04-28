import time
from src.revocation.blacklist import TokenBlacklist

def test_blacklist_lifecycle():
    bl = TokenBlacklist()
    bl.revoke("jti_123", time.time() + 60)
    assert bl.is_revoked("jti_123") is True
    assert bl.is_revoked("jti_clean") is False
    
    bl.revoke("jti_expired", time.time() - 10)
    assert bl.is_revoked("jti_expired") is False
