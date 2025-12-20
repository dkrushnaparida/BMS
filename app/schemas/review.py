from pydantic import BaseModel


class ReviewCreate(BaseModel):
    review_text: str
    rating: int


class ReviewRead(BaseModel):
    id: int
    book_id: int
    user_id: int
    review_text: str
    rating: int

    class Config:
        from_attributes = True
