"""Flask application factory."""

from collections.abc import Mapping

import click
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_wtf import CSRFProtect
from werkzeug.exceptions import NotFound

from blog.constants import APP_TITLE, HTTP_NOT_FOUND
from blog.infrastructure.config.settings import load_default_config
from blog.infrastructure.persistence import blog_post_model  # noqa: F401
from blog.infrastructure.persistence.database import db
from blog.infrastructure.seed import seed_if_empty
from blog.presentation.composition_root import build_repository
from blog.presentation.features.posts.routes import posts_blueprint


def _render_not_found(error: NotFound) -> tuple[str, int]:
    return render_template("404.html"), HTTP_NOT_FOUND


def create_app(test_config: Mapping[str, object] | None = None) -> Flask:
    """Create the app; ``test_config`` overrides the default configuration."""
    app = Flask(__name__, template_folder="shared/templates")
    app.config.from_mapping(load_default_config())
    if test_config is not None:
        app.config.from_mapping(test_config)

    db.init_app(app)
    Bootstrap5(app)
    CKEditor(app)
    CSRFProtect(app)
    app.jinja_env.globals["APP_TITLE"] = APP_TITLE
    with app.app_context():
        db.create_all()

    app.register_blueprint(posts_blueprint)
    app.register_error_handler(HTTP_NOT_FOUND, _render_not_found)
    app.cli.add_command(seed_db_command)
    return app


@click.command("seed-db")
def seed_db_command() -> None:
    """Insert the example posts when the database has none."""
    added = seed_if_empty(build_repository())
    click.echo(f"Added {added} example post(s).")
