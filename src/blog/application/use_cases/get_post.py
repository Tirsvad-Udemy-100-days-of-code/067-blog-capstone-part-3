"""Use case: read one post by its id."""

from blog.domain.entities.blog_post import BlogPost
from blog.domain.errors.post_not_found_error import PostNotFoundError
from blog.domain.repositories.blog_post_repository import BlogPostRepository


class GetPost:
    """Return one post, or raise when the id is unknown."""

    def __init__(self, repository: BlogPostRepository) -> None:
        """Receive the repository the post is read from."""
        self._repository = repository

    def execute(self, post_id: int) -> BlogPost:
        """Return the post with ``post_id``.

        Raises:
            PostNotFoundError: no post has that id.

        """
        post = self._repository.find_by_id(post_id)
        if post is None:
            raise PostNotFoundError(post_id)
        return post
