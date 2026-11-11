import pytest

from blog.application.use_cases.delete_post import DeletePost
from blog.domain.errors.post_not_found_error import PostNotFoundError
from tests.unit.application.fake_blog_post_repository import FakeBlogPostRepository
from tests.unit.domain.test_blog_post import make_post


def test_delete_post_removes_the_post() -> None:
    repository = FakeBlogPostRepository([make_post()])

    DeletePost(repository).execute(1)

    assert repository.find_by_id(1) is None


def test_delete_post_raises_when_id_is_unknown() -> None:
    with pytest.raises(PostNotFoundError) as raised:
        DeletePost(FakeBlogPostRepository()).execute(7)

    assert raised.value.post_id == 7


def test_delete_post_keeps_the_other_posts() -> None:
    repository = FakeBlogPostRepository([make_post(), make_post(), make_post()])

    DeletePost(repository).execute(2)

    assert [post.post_id for post in repository.list_all()] == [1, 3]
