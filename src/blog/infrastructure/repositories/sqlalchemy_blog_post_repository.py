"""Blog post repository backed by a SQLAlchemy session."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from blog.domain.entities.blog_post import BlogPost
from blog.infrastructure.persistence.blog_post_model import BlogPostModel


def _to_entity(model: BlogPostModel) -> BlogPost:
    return BlogPost(
        post_id=model.id,
        title=model.title,
        subtitle=model.subtitle,
        posted_on=model.posted_on,
        body=model.body,
        author=model.author,
        img_url=model.img_url,
    )


def _to_model(post: BlogPost) -> BlogPostModel:
    return BlogPostModel(
        title=post.title,
        subtitle=post.subtitle,
        posted_on=post.posted_on,
        body=post.body,
        author=post.author,
        img_url=post.img_url,
    )


class SqlAlchemyBlogPostRepository:
    """Implements ``BlogPostRepository`` on a relational database."""

    def __init__(self, session: Session) -> None:
        """Use ``session`` for every read and write."""
        self._session = session

    def list_all(self) -> list[BlogPost]:
        """Return every post ordered by id."""
        statement = select(BlogPostModel).order_by(BlogPostModel.id)
        return [_to_entity(model) for model in self._session.scalars(statement)]

    def find_by_id(self, post_id: int) -> BlogPost | None:
        """Return the post with ``post_id``, or ``None``."""
        model = self._session.get(BlogPostModel, post_id)
        return None if model is None else _to_entity(model)

    def add(self, post: BlogPost) -> BlogPost:
        """Store ``post`` and return it with the id the database gave it."""
        model = _to_model(post)
        self._session.add(model)
        self._session.flush()
        stored = _to_entity(model)
        self._session.commit()
        return stored

    def update(self, post: BlogPost) -> BlogPost | None:
        """Overwrite the stored post with the same id, or return ``None``."""
        if post.post_id is None:
            return None
        model = self._session.get(BlogPostModel, post.post_id)
        if model is None:
            return None
        model.title = post.title
        model.subtitle = post.subtitle
        model.posted_on = post.posted_on
        model.body = post.body
        model.author = post.author
        model.img_url = post.img_url
        self._session.flush()
        updated = _to_entity(model)
        self._session.commit()
        return updated

    def delete(self, post_id: int) -> bool:
        """Remove the post with ``post_id``; say whether there was one."""
        model = self._session.get(BlogPostModel, post_id)
        if model is None:
            return False
        self._session.delete(model)
        self._session.commit()
        return True
