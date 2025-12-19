from fastapi import FastAPI
from sqlalchemy import text

from app.config.database import engine

app = FastAPI(title="Intelligent Book Management System", version="1.0.0")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))


@app.get("/health")
async def health_check():
    return {"status": "ok"}
