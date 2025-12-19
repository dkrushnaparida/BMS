from fastapi import FastAPI
from sqlalchemy import text

from app.config.database import engine
from app.models.base import Base

app = FastAPI(title="Book Management System", version="1.0.0")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(text("SELECT 1"))


@app.get("/health")
async def health_check():
    return {"status": "ok"}
