import pytest

from blog.application.use_cases.get_post import GetPost
from blog.domain.errors.post_not_found_error import PostNotFoundError
from tests.unit.application.fake_blog_post_repository import FakeBlogPostRepository
from tests.unit.domain.test_blog_post import make_post


def test_get_post_returns_post_with_matching_id() -> None:
    repository = FakeBlogPostRepository([make_post(), make_post()])

    assert GetPost(repository).execute(2).post_id == 2


def test_get_post_raises_when_id_is_unknown() -> None:
    with pytest.raises(PostNotFoundError) as raised:
        GetPost(FakeBlogPostRepository()).execute(999)

    assert raised.value.post_id == 999
