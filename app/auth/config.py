from datetime import timedelta
from app.config.settings import settings
import os

SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

ACCESS_TOKEN_EXPIRE = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY not set in environment")
