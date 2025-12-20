from sqlalchemy.ext.asyncio import AsyncSession

from app.models.book import Book
from app.repositories.book_repository import BookRepository


class BookService:
    def __init__(self, session: AsyncSession):
        self.book_repo = BookRepository(session)

    async def create_book(self, data: dict) -> Book:
        book = Book(**data)
        return await self.book_repo.create(book)

    async def get_all_books(self) -> list[Book]:
        return await self.book_repo.get_all()

    async def get_book(self, book_id: int) -> Book:
        book = await self.book_repo.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        return book

    async def delete_book(self, book_id: int) -> None:
        book = await self.get_book(book_id)
        await self.book_repo.delete(book)
