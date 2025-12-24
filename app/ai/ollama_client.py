import asyncio
from langchain_ollama import ChatOllama
from app.config.settings import settings


class OllamaClient:
    def __init__(self):
        self.llm = ChatOllama(
            model=settings.AI_MODEL_NAME,
            temperature=0.3,
        )

    def _generate_sync(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content

    async def generate(self, prompt: str, timeout: int = 30) -> str:
        try:
            return await asyncio.wait_for(
                asyncio.to_thread(self._generate_sync, prompt),
                timeout=timeout,
            )
        except asyncio.TimeoutError:
            raise RuntimeError("AI model timed out while generating summary")
        except Exception as exc:
            raise RuntimeError(f"AI generation failed: {exc}")
