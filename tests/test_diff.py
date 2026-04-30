from src.diff.comparator import ClaimsDiff

def test_claims_diff():
    c1 = {"sub": "alice", "role": "user", "scope": "read"}
    c2 = {"sub": "alice", "role": "admin", "org": "corp"}
    add, rem, chg = ClaimsDiff.diff(c1, c2)
    assert "org" in add
    assert "scope" in rem
    assert chg["role"] == ("user", "admin")
