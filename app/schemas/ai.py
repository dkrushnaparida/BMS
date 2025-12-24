from pydantic import BaseModel, Field


class SummaryResponse(BaseModel):
    summary: str = Field(..., min_length=10, max_length=1000)
