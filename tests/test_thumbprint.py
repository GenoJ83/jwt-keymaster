from src.fingerprint.thumbprint import compute_thumbprint

def test_thumbprint():
    t1 = "header.payload.sig1"
    t2 = "header.payload.sig2"
    tp1 = compute_thumbprint(t1)
    tp2 = compute_thumbprint(t2)
    assert len(tp1) == 16 and len(tp2) == 16
    assert tp1 != tp2
