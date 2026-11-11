"""Routes that read posts."""

from flask import Blueprint, abort, render_template

from blog.constants import HTTP_NOT_FOUND
from blog.domain.errors.post_not_found_error import PostNotFoundError
from blog.presentation.composition_root import build_get_post, build_list_posts
from blog.presentation.features.posts.post_view_model import PostViewModel

posts_blueprint = Blueprint("posts", __name__, template_folder="templates")


@posts_blueprint.get("/")
def show_all_posts() -> str:
    """List every post."""
    posts = [PostViewModel.from_entity(post) for post in build_list_posts().execute()]
    return render_template("index.html", posts=posts)


@posts_blueprint.get("/post/<int:post_id>")
def show_post(post_id: int) -> str:
    """Show one post, or answer 404 when the id is unknown."""
    try:
        post = build_get_post().execute(post_id)
    except PostNotFoundError:
        abort(HTTP_NOT_FOUND)
    return render_template("post.html", post=PostViewModel.from_entity(post))
