from sqlalchemy.ext.asyncio import AsyncSession

from app.models.review import Review
from app.repositories.review_repository import ReviewRepository
from app.repositories.book_repository import BookRepository


class ReviewService:
    def __init__(self, session: AsyncSession):
        self.review_repo = ReviewRepository(session)
        self.book_repo = BookRepository(session)

    async def add_review(
        self,
        book_id: int,
        user_id: int,
        review_text: str,
        rating: int,
    ) -> Review:
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        book = await self.book_repo.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found")

        review = Review(
            book_id=book_id,
            user_id=user_id,
            review_text=review_text,
            rating=rating,
        )
        return await self.review_repo.create(review)

    async def get_reviews_for_book(self, book_id: int):
        return await self.review_repo.get_by_book(book_id)
