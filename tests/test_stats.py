from src.metrics.stats import JWTStats

def test_stats():
    s = JWTStats()
    s.record_ok()
    s.record_expired()
    s.record_invalid_sig()
    out = s.export()
    assert out["ok"] == 1 and out["expired"] == 1 and out["invalid_sig"] == 1
