from fastapi import APIRouter, Depends
from app.ai.summary_service import SummaryService
from app.auth.dependencies import require_role

router = APIRouter(tags=["AI"])


@router.post(
    "/generate-summary",
    dependencies=[Depends(require_role("admin"))],
)
async def generate_summary(
    title: str,
    author: str,
    description: str | None = None,
):
    ai = SummaryService()
    summary = await ai.generate_book_summary(title, author, description)
    return {"summary": summary}
