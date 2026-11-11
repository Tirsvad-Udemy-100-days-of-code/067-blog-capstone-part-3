from collections.abc import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient

from blog.infrastructure.persistence.database import db
from blog.infrastructure.seed import seed_if_empty
from blog.presentation.app_factory import create_app
from blog.presentation.composition_root import build_repository


@pytest.fixture
def app() -> Iterator[Flask]:
    application = create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    )
    with application.app_context():
        seed_if_empty(build_repository())
        yield application
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
