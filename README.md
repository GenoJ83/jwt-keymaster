# jwt-keymaster

Production-ready JWT debugger, signature verification utility, JWKS caching rotator, and token claims auditor.

[![CI](https://github.com/GenoJ83/jwt-keymaster/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/jwt-keymaster/actions)

## Features
- **HS256 Sign & Verify**: Constant-time HMAC SHA-256 verification and tampering defense
- **Claims Enforcement**: Standard validation for `exp`, `nbf`, `iss`, and `aud` with configurable leeway
- **JWKS Management**: In-memory JSON Web Key Set export and ID routing
- **Security Auditor**: Heuristic audit detecting weak secrets, missing exp, and `alg: none` flaws

## Quick Start
```python
from src.jwt import JWTKeymaster
import time

km = JWTKeymaster(secret="your-secret-key")
token = km.encode({"sub": "user_101", "exp": time.time() + 3600})
payload = km.decode(token)
print(payload["sub"])
```
