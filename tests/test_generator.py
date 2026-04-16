from src.generator.secret import generate_hmac_secret, generate_key_id

def test_secret_generator():
    s1 = generate_hmac_secret(32)
    s2 = generate_hmac_secret(32)
    assert len(s1) == 32 and len(s2) == 32
    assert s1 != s2
    kid = generate_key_id()
    assert kid.startswith("key_") and len(kid) == 16
