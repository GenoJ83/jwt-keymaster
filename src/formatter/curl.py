def to_curl_header(token: str) -> str:
    return f"-H \"Authorization: Bearer {token}\""

def to_cookie_header(token: str, cookie_name: str = "access_token") -> str:
    return f"-H \"Cookie: {cookie_name}={token}\""
