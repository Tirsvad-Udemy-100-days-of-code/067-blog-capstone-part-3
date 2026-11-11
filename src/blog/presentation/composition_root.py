"""The one place that wires adapters to use cases."""

from blog.application.use_cases.create_post import CreatePost
from blog.application.use_cases.get_post import GetPost
from blog.application.use_cases.list_posts import ListPosts
from blog.application.use_cases.update_post import UpdatePost
from blog.infrastructure.persistence.database import db
from blog.infrastructure.repositories.sqlalchemy_blog_post_repository import (
    SqlAlchemyBlogPostRepository,
)


def build_repository() -> SqlAlchemyBlogPostRepository:
    """Build the repository on the session of the current request."""
    return SqlAlchemyBlogPostRepository(db.session())


def build_list_posts() -> ListPosts:
    """Build the ``ListPosts`` use case."""
    return ListPosts(build_repository())


def build_get_post() -> GetPost:
    """Build the ``GetPost`` use case."""
    return GetPost(build_repository())


def build_create_post() -> CreatePost:
    """Build the ``CreatePost`` use case with the system clock."""
    return CreatePost(build_repository())


def build_update_post() -> UpdatePost:
    """Build the ``UpdatePost`` use case."""
    return UpdatePost(build_repository())
