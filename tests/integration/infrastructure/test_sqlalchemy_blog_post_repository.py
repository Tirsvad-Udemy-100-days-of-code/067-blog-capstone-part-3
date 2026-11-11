from collections.abc import Iterator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from blog.infrastructure.persistence import blog_post_model  # noqa: F401
from blog.infrastructure.persistence.database import Base
from blog.infrastructure.repositories.sqlalchemy_blog_post_repository import (
    SqlAlchemyBlogPostRepository,
)
from blog.infrastructure.seed import SEED_POSTS, seed_if_empty
from tests.unit.domain.test_blog_post import make_post


@pytest.fixture
def repository() -> Iterator[SqlAlchemyBlogPostRepository]:
    engine = create_engine(
        "sqlite:///:memory:",
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield SqlAlchemyBlogPostRepository(session)
    engine.dispose()


def test_add_returns_post_with_assigned_id(
    repository: SqlAlchemyBlogPostRepository,
) -> None:
    stored = repository.add(make_post())

    assert stored.post_id == 1
    assert repository.find_by_id(1) == stored


def test_find_by_id_returns_none_when_unknown(
    repository: SqlAlchemyBlogPostRepository,
) -> None:
    assert repository.find_by_id(42) is None


def test_list_all_is_ordered_by_id(
    repository: SqlAlchemyBlogPostRepository,
) -> None:
    for _ in range(3):
        repository.add(make_post())

    assert [post.post_id for post in repository.list_all()] == [1, 2, 3]


def test_seed_if_empty_inserts_once(
    repository: SqlAlchemyBlogPostRepository,
) -> None:
    assert seed_if_empty(repository) == len(SEED_POSTS)
    assert seed_if_empty(repository) == 0
    assert len(repository.list_all()) == len(SEED_POSTS)
