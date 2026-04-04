from src.jwks.keyset import JWKSManager

def test_jwks_operations():
    mgr = JWKSManager()
    mgr.register_key("key-1", "RSA", "RS256", "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A")
    k = mgr.get_key("key-1")
    assert k is not None and k["alg"] == "RS256"
    assert mgr.get_key("missing") is None
    jwks = mgr.export_jwks()
    assert len(jwks["keys"]) == 1
