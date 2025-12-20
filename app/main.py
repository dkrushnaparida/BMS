from fastapi import FastAPI
from sqlalchemy import text
from app.config.database import engine
from app.models.base import Base
from app.api.routes import auth, books, reviews
from app.api.routes import ai
import os


app = FastAPI(title="Book Management System")


# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#         await conn.execute(text("SELECT 1"))


@app.on_event("startup")
async def startup():
    if os.getenv("ENV") == "test":
        return  # DO NOT touch DB during tests

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(books.router)
app.include_router(reviews.router)
app.include_router(ai.router)
