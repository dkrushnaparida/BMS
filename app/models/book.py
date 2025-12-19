from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    author: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    genre: Mapped[str] = mapped_column(String(100), index=True)
    year_published: Mapped[int] = mapped_column(Integer)
    summary: Mapped[str] = mapped_column(Text)
