from src.crypto.hs256 import sign_hs256, verify_hs256

def test_hs256_sign_and_verify():
    secret = "super-secret-key-999"
    data = "header.payload"
    sig = sign_hs256(data, secret)
    assert verify_hs256(data, sig, secret) is True
    assert verify_hs256(data, sig, "wrong-key") is False
    assert verify_hs256("tampered.payload", sig, secret) is False
