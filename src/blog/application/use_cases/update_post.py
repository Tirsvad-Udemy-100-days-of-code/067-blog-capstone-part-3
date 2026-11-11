"""Use case: edit an existing post."""

from dataclasses import replace

from blog.application.dto.post_content import PostContent
from blog.domain.entities.blog_post import BlogPost
from blog.domain.errors.post_not_found_error import PostNotFoundError
from blog.domain.repositories.blog_post_repository import BlogPostRepository
from blog.domain.rules.post_validation import validate_post


class UpdatePost:
    """Replace the editable fields of a post; its id and date stay."""

    def __init__(self, repository: BlogPostRepository) -> None:
        """Receive the repository the post is read from and stored to."""
        self._repository = repository

    def execute(self, post_id: int, content: PostContent) -> BlogPost:
        """Store the new content and return the updated post.

        Raises:
            PostNotFoundError: no post has that id.
            InvalidPostError: the content breaks a rule; nothing is changed.

        """
        stored = self._repository.find_by_id(post_id)
        if stored is None:
            raise PostNotFoundError(post_id)
        edited = replace(
            stored,
            title=content.title,
            subtitle=content.subtitle,
            author=content.author,
            img_url=content.img_url,
            body=content.body,
        )
        validate_post(edited)
        updated = self._repository.update(edited)
        if updated is None:
            raise PostNotFoundError(post_id)
        return updated
