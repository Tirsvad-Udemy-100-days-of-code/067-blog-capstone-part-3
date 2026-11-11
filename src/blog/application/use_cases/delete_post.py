"""Use case: delete a post."""

from blog.domain.errors.post_not_found_error import PostNotFoundError
from blog.domain.repositories.blog_post_repository import BlogPostRepository


class DeletePost:
    """Remove one post from the blog."""

    def __init__(self, repository: BlogPostRepository) -> None:
        """Receive the repository the post is removed from."""
        self._repository = repository

    def execute(self, post_id: int) -> None:
        """Delete the post with ``post_id``.

        Raises:
            PostNotFoundError: no post has that id.

        """
        if not self._repository.delete(post_id):
            raise PostNotFoundError(post_id)
