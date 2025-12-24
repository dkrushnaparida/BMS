from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.schemas.book import BookCreate, BookRead
from app.schemas.ai import BookSummaryResponse
from app.services.book_service import BookService
from app.auth.dependencies import get_current_user, require_role

router = APIRouter(prefix="/books", tags=["Books"])


@router.post(
    "",
    response_model=BookRead,
    status_code=201,
    dependencies=[Depends(require_role("admin"))],
)
async def create_book(
    book: BookCreate,
    session: AsyncSession = Depends(get_db),
):
    service = BookService(session)
    return await service.create_book(book.model_dump())


@router.get("", response_model=list[BookRead])
async def list_books(session: AsyncSession = Depends(get_db)):
    service = BookService(session)
    return await service.get_all_books()


@router.get("/{book_id}", response_model=BookRead)
async def get_book(book_id: int, session: AsyncSession = Depends(get_db)):
    service = BookService(session)
    try:
        return await service.get_book(book_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete(
    "/{book_id}",
    status_code=204,
    dependencies=[Depends(require_role("admin"))],
)
async def delete_book(
    book_id: int,
    session: AsyncSession = Depends(get_db),
):
    service = BookService(session)
    await service.delete_book(book_id)


@router.get(
    "/{book_id}/summary",
    response_model=BookSummaryResponse,
    dependencies=[Depends(get_current_user)],
)
async def get_book_summary(
    book_id: int,
    session: AsyncSession = Depends(get_db),
):
    service = BookService(session)
    summary = await service.generate_summary_for_book(book_id)
    return {"summary": summary}
