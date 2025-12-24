from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.schemas.review import ReviewCreate, ReviewRead
from app.services.review_service import ReviewService
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/books/{book_id}/reviews", tags=["Reviews"])


@router.post(
    "",
    response_model=ReviewRead,
    status_code=201,
)
async def add_review(
    book_id: int,
    review: ReviewCreate,
    session: AsyncSession = Depends(get_db),
    user=Depends(get_current_user),
):
    service = ReviewService(session)
    try:
        return await service.add_review(
            book_id=book_id,
            user_id=user.id,
            data=review.model_dump(),
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("", response_model=list[ReviewRead])
async def list_reviews(
    book_id: int,
    session: AsyncSession = Depends(get_db),
):
    service = ReviewService(session)
    return await service.get_reviews_for_book(book_id)
