import os
import secrets
 
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader
 
# auto_error=False lets us return our own, clearer error message
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
 
 
def require_api_key(api_key: str | None = Security(api_key_header)) -> None:
    """Reject any request that does not carry the correct X-API-Key header."""
    expected = os.environ.get("API_KEY")
    if not expected:
        # Fail safe: if the server has no key configured, nobody gets in.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API key is not configured on the server",
        )
    # compare_digest takes the same time however many characters match (stops timing attacks)
    if not api_key or not secrets.compare_digest(api_key.encode(), expected.encode()):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
