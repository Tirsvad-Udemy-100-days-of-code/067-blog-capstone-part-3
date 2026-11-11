"""Table model of a blog post."""

from datetime import date

from sqlalchemy import Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from blog.constants import SHORT_TEXT_MAX_LENGTH
from blog.infrastructure.persistence.database import Base


class BlogPostModel(Base):
    """Row of the ``blog_post`` table."""

    __tablename__ = "blog_post"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(SHORT_TEXT_MAX_LENGTH))
    subtitle: Mapped[str] = mapped_column(String(SHORT_TEXT_MAX_LENGTH))
    posted_on: Mapped[date] = mapped_column(Date)
    body: Mapped[str] = mapped_column(Text)
    author: Mapped[str] = mapped_column(String(SHORT_TEXT_MAX_LENGTH))
    img_url: Mapped[str] = mapped_column(String(SHORT_TEXT_MAX_LENGTH))
