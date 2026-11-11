"""The one rule that decides whether the content of a post is acceptable."""

from blog.constants import (
    AUTHOR_MAX_LENGTH,
    BODY_MAX_LENGTH,
    IMG_URL_MAX_LENGTH,
    IMG_URL_SCHEMES,
    SUBTITLE_MAX_LENGTH,
    TITLE_MAX_LENGTH,
)
from blog.domain.entities.blog_post import BlogPost
from blog.domain.errors.invalid_post_error import InvalidPostError, PostProblem

_REQUIRED_FIELDS_WITH_LIMIT = (
    ("title", TITLE_MAX_LENGTH),
    ("subtitle", SUBTITLE_MAX_LENGTH),
    ("author", AUTHOR_MAX_LENGTH),
    ("body", BODY_MAX_LENGTH),
)


def _text_problems(field: str, value: str, max_length: int) -> list[PostProblem]:
    if not value.strip():
        return [PostProblem(field, "must not be blank")]
    if len(value) > max_length:
        return [PostProblem(field, f"must have at most {max_length} characters")]
    return []


def _img_url_problems(value: str) -> list[PostProblem]:
    if not value.startswith(IMG_URL_SCHEMES):
        schemes = " or ".join(IMG_URL_SCHEMES)
        return [PostProblem("img_url", f"must start with {schemes}")]
    if len(value) > IMG_URL_MAX_LENGTH:
        return [
            PostProblem("img_url", f"must have at most {IMG_URL_MAX_LENGTH} characters")
        ]
    return []


def validate_post(post: BlogPost) -> None:
    """Check the editable fields of ``post``.

    Raises:
        InvalidPostError: one or more fields break a rule; it lists all of them.

    """
    problems: list[PostProblem] = []
    for field, max_length in _REQUIRED_FIELDS_WITH_LIMIT:
        problems.extend(_text_problems(field, getattr(post, field), max_length))
    problems.extend(_img_url_problems(post.img_url))
    if problems:
        raise InvalidPostError(problems)
