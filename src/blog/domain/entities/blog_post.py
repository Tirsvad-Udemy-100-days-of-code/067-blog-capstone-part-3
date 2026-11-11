"""The blog post entity."""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class BlogPost:
    """One post of the blog.

    ``post_id`` is ``None`` until the repository has stored the post.
    """

    title: str
    subtitle: str
    posted_on: date
    body: str
    author: str
    img_url: str
    post_id: int | None = None
