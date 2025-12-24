from fastapi import FastAPI
from sqlalchemy import text
from app.config.database import engine
from app.models.base import Base
from app.api.routes import auth, books, reviews, ai
from app.config.settings import settings
from fastapi.responses import JSONResponse
from fastapi import Request
import os
import logging


app = FastAPI(title="Book Management System")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("bms")


@app.on_event("startup")
async def startup():
    _ = settings.DATABASE_URL
    _ = settings.JWT_SECRET_KEY
    _ = settings.AI_MODEL_NAME

    if os.getenv("ENV") == "test":
        return

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(text("SELECT 1"))


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


app.include_router(auth.router)
app.include_router(books.router)
app.include_router(reviews.router)
app.include_router(ai.router)
