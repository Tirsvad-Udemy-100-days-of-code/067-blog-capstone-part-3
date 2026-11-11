"""Plain data a template needs to show one post."""

from dataclasses import dataclass
from typing import Self

from blog.constants import DATE_DISPLAY_FORMAT
from blog.domain.entities.blog_post import BlogPost


@dataclass(frozen=True, slots=True)
class PostViewModel:
    """One post prepared for display.

    ``body_html`` is trusted HTML written by the blog author; only the template
    marks it ``safe``.
    """

    post_id: int
    title: str
    subtitle: str
    posted_on_text: str
    body_html: str
    author: str
    img_url: str

    @classmethod
    def from_entity(cls, post: BlogPost) -> Self:
        """Map a stored post; raise ``ValueError`` if it has no id yet."""
        if post.post_id is None:
            raise ValueError("A post without an id cannot be shown.")
        return cls(
            post_id=post.post_id,
            title=post.title,
            subtitle=post.subtitle,
            posted_on_text=post.posted_on.strftime(DATE_DISPLAY_FORMAT),
            body_html=post.body,
            author=post.author,
            img_url=post.img_url,
        )
