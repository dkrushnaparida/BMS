from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    author = Column(String(255), index=True, nullable=False)
    genre = Column(String(100), index=True, nullable=True)
    year_published = Column(Integer, nullable=True)
    summary = Column(Text, nullable=True)

    reviews = relationship(
        "Review",
        back_populates="book",
        cascade="all, delete-orphan",
    )
