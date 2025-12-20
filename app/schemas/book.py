from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    year_published: Optional[int] = None
    summary: Optional[str] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    year_published: Optional[int] = None
    summary: Optional[str] = None


class BookRead(BaseModel):
    id: int
    title: str
    author: str
    genre: Optional[str]
    year_published: Optional[int]
    summary: Optional[str]

    class Config:
        from_attributes = True
