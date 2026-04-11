from src.inspector.visualizer import JWTVisualizer
from src.utils.b64 import json_b64encode

def test_jwt_visualizer():
    h = json_b64encode({"alg": "HS256"})
    p = json_b64encode({"exp": 1700000000, "user": "bob"})
    token = f"{h}.{p}.abcdefghijklmnop"
    text = JWTVisualizer.inspect_text(token)
    assert "=== HEADER ===" in text
    assert "_exp_human" in text
    assert "bob" in text
