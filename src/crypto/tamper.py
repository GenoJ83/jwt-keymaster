def detect_tampering(original_token: str, altered_payload_b64: str) -> str:
    parts = original_token.split(".")
    return f"{parts[0]}.{altered_payload_b64}.{parts[2]}"
