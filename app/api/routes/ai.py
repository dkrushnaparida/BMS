from fastapi import APIRouter
from app.ai.summary_service import SummaryService

router = APIRouter(tags=["AI"])


@router.post("/generate-summary")
async def generate_summary(
    title: str,
    author: str,
    description: str | None = None,
):
    ai = SummaryService()
    summary = await ai.generate_book_summary(title, author, description)
    return {"summary": summary}
