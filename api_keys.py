from fastapi import HTTPException, status, Security, Header, Depends
from fastapi.security import APIKeyHeader

from core.config import settings

API_KEYS = [
    settings.TEST_X_API_KEY,
    settings.PROD_X_API_KEY
]

_api_key_header = APIKeyHeader(name="x-api-key")


def get_api_key(api_key_header: str = Security(_api_key_header)) -> str:
    if api_key_header in API_KEYS:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )