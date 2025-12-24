from pydantic import BaseModel, Field
from typing import Optional


class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    genre: Optional[str] = Field(None, max_length=100)
    year_published: Optional[int] = Field(None, ge=0)
    summary: Optional[str] = None


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    author: Optional[str] = Field(None, min_length=1, max_length=255)
    genre: Optional[str] = Field(None, max_length=100)
    year_published: Optional[int] = Field(None, ge=0)
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
