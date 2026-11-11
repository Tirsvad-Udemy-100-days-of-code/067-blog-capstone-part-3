from blog.application.use_cases.list_posts import ListPosts
from tests.unit.application.fake_blog_post_repository import FakeBlogPostRepository
from tests.unit.domain.test_blog_post import make_post


def test_list_posts_returns_all_posts_in_id_order() -> None:
    repository = FakeBlogPostRepository([make_post(), make_post()])

    posts = ListPosts(repository).execute()

    assert [post.post_id for post in posts] == [1, 2]


def test_list_posts_returns_empty_list_when_no_posts() -> None:
    assert ListPosts(FakeBlogPostRepository()).execute() == []
