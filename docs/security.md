# JWT Security Best Practices

- Reject `alg: "none"` unconditionally.
- Ensure `exp` claim is present with maximum lifespan ≤ 1 hour for access tokens.
- Rotate HMAC signing secrets and JWKS periodically.
- Maintain revocation blacklists for immediate sign-out.
