from fastapi import FastAPI
from sqlalchemy import text
from app.config.database import engine
from app.models.base import Base
from app.api.routes import auth, books, reviews, ai
from app.config.settings import settings
import os


app = FastAPI(title="Book Management System")


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


app.include_router(auth.router)
app.include_router(books.router)
app.include_router(reviews.router)
app.include_router(ai.router)
