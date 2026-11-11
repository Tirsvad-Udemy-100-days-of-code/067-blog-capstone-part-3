from datetime import date

import pytest

from blog.application.dto.post_content import PostContent
from blog.application.use_cases.update_post import UpdatePost
from blog.domain.errors.invalid_post_error import InvalidPostError
from blog.domain.errors.post_not_found_error import PostNotFoundError
from tests.unit.application.fake_blog_post_repository import FakeBlogPostRepository
from tests.unit.domain.test_blog_post import make_post

NEW_CONTENT = PostContent(
    title="New title",
    subtitle="New subtitle",
    author="New author",
    img_url="http://example.com/new.png",
    body="<p>New</p>",
)


def test_update_post_replaces_fields_and_keeps_id_and_date() -> None:
    repository = FakeBlogPostRepository([make_post()])

    updated = UpdatePost(repository).execute(1, NEW_CONTENT)

    assert updated.post_id == 1
    assert updated.posted_on == date(2026, 1, 2)
    assert (updated.title, updated.subtitle, updated.author) == (
        "New title",
        "New subtitle",
        "New author",
    )
    assert updated.img_url == NEW_CONTENT.img_url
    assert updated.body == NEW_CONTENT.body
    assert repository.find_by_id(1) == updated


def test_update_post_raises_when_id_is_unknown() -> None:
    with pytest.raises(PostNotFoundError) as raised:
        UpdatePost(FakeBlogPostRepository()).execute(7, NEW_CONTENT)

    assert raised.value.post_id == 7


def test_update_post_rejects_invalid_content_and_changes_nothing() -> None:
    repository = FakeBlogPostRepository([make_post()])
    invalid = PostContent("", "s", "a", "https://x.example", "b")

    with pytest.raises(InvalidPostError):
        UpdatePost(repository).execute(1, invalid)

    assert repository.find_by_id(1) == make_post(post_id=1)
