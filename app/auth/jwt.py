from datetime import datetime, timedelta, timezone
import logging
from jose import jwt, JWTError
from app.config.settings import settings

logger = logging.getLogger(__name__)


def create_access_token(data: dict) -> str:
    if "sub" not in data:
        raise ValueError("Token payload must include 'sub'")

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )

        if "sub" not in payload:
            raise ValueError("Invalid token payload: missing 'sub'")

        return payload

    except JWTError as e:
        logger.warning("JWT decoding failed", exc_info=e)
        raise ValueError("Invalid or expired token")
