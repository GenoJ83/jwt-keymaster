class JWTError(Exception):
    """Base exception for JWT operations."""

class TokenExpiredError(JWTError):
    """Raised when exp timestamp has passed."""

class InvalidSignatureError(JWTError):
    """Raised when signature verification fails."""

class MalformedTokenError(JWTError):
    """Raised when token structure is invalid."""
