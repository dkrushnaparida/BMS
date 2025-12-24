from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    review_text: str = Field(..., min_length=1)
    rating: int = Field(..., ge=1, le=5)


class ReviewRead(BaseModel):
    id: int
    book_id: int
    user_id: int
    review_text: str
    rating: int

    class Config:
        from_attributes = True
