from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from config import API_KEYS

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header and any(api_key_header.replace("Bearer ", "") == key for key in API_KEYS.values()):
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
