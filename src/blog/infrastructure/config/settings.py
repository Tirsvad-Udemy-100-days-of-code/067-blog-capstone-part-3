"""Default configuration values, read from the environment."""

import os

from blog.constants import DATABASE_FILE_NAME, DATABASE_URI_ENVIRONMENT_VARIABLE

# A relative SQLite path is resolved by Flask-SQLAlchemy inside the Flask
# instance folder.
DEFAULT_DATABASE_URI = f"sqlite:///{DATABASE_FILE_NAME}"


def load_default_config() -> dict[str, object]:
    """Return the Flask configuration used when no test config overrides it."""
    return {
        "SQLALCHEMY_DATABASE_URI": os.environ.get(
            DATABASE_URI_ENVIRONMENT_VARIABLE, DEFAULT_DATABASE_URI
        ),
    }
