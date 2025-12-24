from fastapi import APIRouter, Depends
from app.ai.summary_service import SummaryService
from app.auth.dependencies import require_role
from app.schemas.ai import SummaryRequest

router = APIRouter(tags=["AI"])


@router.post(
    "/generate-summary",
    dependencies=[Depends(require_role("admin"))],
)
async def generate_summary(payload: SummaryRequest):
    ai = SummaryService()
    summary = await ai.generate_book_summary(
        payload.title,
        payload.author,
        payload.description,
    )
    return {"summary": summary}
