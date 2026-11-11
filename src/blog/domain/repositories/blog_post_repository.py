"""Port through which the application reads and stores posts."""

from typing import Protocol

from blog.domain.entities.blog_post import BlogPost


class BlogPostRepository(Protocol):
    """Storage of blog posts; an infrastructure adapter implements it."""

    def list_all(self) -> list[BlogPost]:
        """Return every post, oldest id first."""
        ...

    def find_by_id(self, post_id: int) -> BlogPost | None:
        """Return the post with ``post_id``, or ``None`` if there is none."""
        ...

    def add(self, post: BlogPost) -> BlogPost:
        """Store a new post and return it with its id set."""
        ...
