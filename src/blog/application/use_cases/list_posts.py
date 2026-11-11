"""Use case: list every post."""

from blog.domain.entities.blog_post import BlogPost
from blog.domain.repositories.blog_post_repository import BlogPostRepository


class ListPosts:
    """Return all posts of the blog."""

    def __init__(self, repository: BlogPostRepository) -> None:
        """Receive the repository the posts are read from."""
        self._repository = repository

    def execute(self) -> list[BlogPost]:
        """Return every post."""
        return self._repository.list_all()
