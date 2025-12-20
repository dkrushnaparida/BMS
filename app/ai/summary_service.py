from app.ai.ollama_client import OllamaClient


class SummaryService:
    def __init__(self):
        self.client = OllamaClient()

    async def generate_book_summary(
        self,
        title: str,
        author: str,
        description: str | None = None,
    ) -> str:
        prompt = f"""
You are an assistant that writes short, clear book summaries.

Book title: {title}
Author: {author}
Description: {description or "N/A"}

Write a concise summary in 4–5 sentences.
"""
        return await self.client.generate(prompt)
