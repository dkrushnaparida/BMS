from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.book import Book


class BookRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, book: Book) -> Book:
        self.session.add(book)
        await self.session.commit()
        await self.session.refresh(book)
        return book

    async def get_all(self) -> list[Book]:
        stmt = select(Book)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_id(self, book_id: int) -> Book | None:
        stmt = select(Book).where(Book.id == book_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def delete(self, book: Book) -> None:
        await self.session.delete(book)
        await self.session.commit()
