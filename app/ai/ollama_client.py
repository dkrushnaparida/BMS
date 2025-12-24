from langchain_ollama import ChatOllama
from app.config.settings import settings

llm = ChatOllama(
    model=settings.AI_MODEL_NAME,
    temperature=0.3,
)
