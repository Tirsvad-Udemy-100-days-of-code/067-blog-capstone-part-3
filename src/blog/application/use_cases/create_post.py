"""Use case: write a new post."""

from collections.abc import Callable
from datetime import date

from blog.application.dto.post_content import PostContent
from blog.domain.entities.blog_post import BlogPost
from blog.domain.repositories.blog_post_repository import BlogPostRepository
from blog.domain.rules.post_validation import validate_post


class CreatePost:
    """Validate the content, date it today and store it."""

    def __init__(
        self,
        repository: BlogPostRepository,
        clock: Callable[[], date] = date.today,
    ) -> None:
        """Receive the repository and the clock that tells today's date."""
        self._repository = repository
        self._clock = clock

    def execute(self, content: PostContent) -> BlogPost:
        """Store a new post and return it with its id.

        Raises:
            InvalidPostError: the content breaks a rule; nothing is stored.

        """
        post = BlogPost(
            title=content.title,
            subtitle=content.subtitle,
            posted_on=self._clock(),
            body=content.body,
            author=content.author,
            img_url=content.img_url,
        )
        validate_post(post)
        return self._repository.add(post)
