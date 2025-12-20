from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.review import Review


class ReviewRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, review: Review) -> Review:
        self.session.add(review)
        await self.session.commit()
        await self.session.refresh(review)
        return review

    async def get_by_book(self, book_id: int) -> list[Review]:
        stmt = select(Review).where(Review.book_id == book_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
