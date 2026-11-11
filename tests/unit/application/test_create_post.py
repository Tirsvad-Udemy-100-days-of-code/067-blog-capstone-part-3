from datetime import date

import pytest

from blog.application.dto.post_content import PostContent
from blog.application.use_cases.create_post import CreatePost
from blog.domain.errors.invalid_post_error import InvalidPostError
from tests.unit.application.fake_blog_post_repository import FakeBlogPostRepository

TODAY = date(2026, 5, 6)


def make_content(title: str = "Title") -> PostContent:
    return PostContent(
        title=title,
        subtitle="Subtitle",
        author="Author",
        img_url="https://example.com/a.png",
        body="<p>Body</p>",
    )


def test_create_post_stores_post_dated_by_the_clock() -> None:
    repository = FakeBlogPostRepository()

    created = CreatePost(repository, clock=lambda: TODAY).execute(make_content())

    assert created.post_id == 1
    assert created.posted_on == TODAY
    assert created.title == "Title"
    assert repository.find_by_id(1) == created


def test_create_post_uses_today_by_default() -> None:
    created = CreatePost(FakeBlogPostRepository()).execute(make_content())

    assert created.posted_on == date.today()


def test_create_post_rejects_invalid_content_and_stores_nothing() -> None:
    repository = FakeBlogPostRepository()

    with pytest.raises(InvalidPostError):
        CreatePost(repository, clock=lambda: TODAY).execute(make_content(" "))

    assert repository.list_all() == []
