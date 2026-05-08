from src.formatter.curl import to_curl_header, to_cookie_header

def test_curl_formatters():
    assert to_curl_header("tok123") == '-H "Authorization: Bearer tok123"'
    assert to_cookie_header("tok123", "jwt") == '-H "Cookie: jwt=tok123"'
