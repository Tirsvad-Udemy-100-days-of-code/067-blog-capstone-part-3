from dataclasses import FrozenInstanceError
from datetime import date

import pytest

from blog.domain.entities.blog_post import BlogPost


def make_post(post_id: int | None = None) -> BlogPost:
    return BlogPost(
        title="Title",
        subtitle="Subtitle",
        posted_on=date(2026, 1, 2),
        body="<p>Body</p>",
        author="Author",
        img_url="https://example.com/a.png",
        post_id=post_id,
    )


def test_post_id_is_none_when_not_stored() -> None:
    assert make_post().post_id is None


def test_post_is_immutable() -> None:
    post = make_post(1)
    with pytest.raises(FrozenInstanceError):
        post.title = "Other"  # type: ignore[misc]  # proves the dataclass is frozen


def test_posts_with_same_values_are_equal() -> None:
    assert make_post(1) == make_post(1)
