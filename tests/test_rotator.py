from src.rotator.rotation import KeyRotator

def test_rotator_transition():
    rotator = KeyRotator(rotation_interval_seconds=10)
    k1 = rotator.active_kid
    assert rotator.should_rotate() is False
    rotator.interval = 0
    assert rotator.should_rotate() is True
    k2, _ = rotator.rotate()
    assert k1 != k2
    assert k1 in rotator.retired_keys
