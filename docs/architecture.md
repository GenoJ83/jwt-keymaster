# JWT Keymaster Architecture

```
Token -> JWTParser -> SignatureVerifier (HS256) -> ClaimsValidator (exp, aud, iss)
                            |
                   SecurityAuditor (heuristics)
```
