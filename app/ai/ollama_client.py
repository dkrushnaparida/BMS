import asyncio
from langchain_ollama import ChatOllama
from app.config.settings import settings
from app.schemas.ai import SummaryResponse


class OllamaClient:
    def __init__(self):
        self.llm = ChatOllama(
            model=settings.AI_MODEL_NAME,
            temperature=0.3,
            num_predict=300,
        )

    def _generate_sync(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content

    async def generate(self, prompt: str, timeout: int = 30) -> SummaryResponse:
        try:
            text = await asyncio.wait_for(
                asyncio.to_thread(self._generate_sync, prompt),
                timeout=timeout,
            )
            return SummaryResponse(summary=text)
        except asyncio.TimeoutError:
            raise RuntimeError("AI generation timed out")
