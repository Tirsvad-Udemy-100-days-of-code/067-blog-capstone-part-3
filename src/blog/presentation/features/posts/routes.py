"""Routes that read, create and edit posts."""

from flask import Blueprint, abort, redirect, render_template, url_for
from werkzeug.wrappers import Response

from blog.constants import HTTP_NOT_FOUND
from blog.domain.errors.invalid_post_error import InvalidPostError
from blog.domain.errors.post_not_found_error import PostNotFoundError
from blog.presentation.composition_root import (
    build_create_post,
    build_delete_post,
    build_get_post,
    build_list_posts,
    build_update_post,
)
from blog.presentation.features.posts.post_form import PostForm
from blog.presentation.features.posts.post_view_model import PostViewModel

posts_blueprint = Blueprint("posts", __name__, template_folder="templates")

NEW_POST_HEADING = "New Post"
EDIT_POST_HEADING = "Edit Post"


@posts_blueprint.get("/")
def show_all_posts() -> str:
    """List every post."""
    posts = [PostViewModel.from_entity(post) for post in build_list_posts().execute()]
    return render_template("index.html", posts=posts)


@posts_blueprint.get("/post/<int:post_id>")
def show_post(post_id: int) -> str:
    """Show one post, or answer 404 when the id is unknown."""
    return render_template("post.html", post=_load_post_or_404(post_id))


@posts_blueprint.route("/new-post", methods=["GET", "POST"])
def add_new_post() -> str | Response:
    """Show the empty form; a valid submission creates the post."""
    form = PostForm()
    if form.validate_on_submit():
        try:
            build_create_post().execute(form.to_content())
        except InvalidPostError as error:
            form.show_problems(error)
        else:
            return redirect(url_for("posts.show_all_posts"))
    return render_template("make-post.html", form=form, heading=NEW_POST_HEADING)


@posts_blueprint.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id: int) -> str | Response:
    """Show the form filled with the post; a valid submission updates it."""
    stored = _load_post_or_404(post_id)
    form = PostForm.prefilled(stored)
    if form.validate_on_submit():
        try:
            build_update_post().execute(post_id, form.to_content())
        except PostNotFoundError:
            abort(HTTP_NOT_FOUND)
        except InvalidPostError as error:
            form.show_problems(error)
        else:
            return redirect(url_for("posts.show_post", post_id=post_id))
    return render_template("make-post.html", form=form, heading=EDIT_POST_HEADING)


# A state-changing GET is not safe: a browser or proxy that prefetches links, or
# a crawler, can delete posts by following them. The course uses a link, so this
# does too; a real application prefers POST or DELETE with a confirmation.
@posts_blueprint.get("/delete/<int:post_id>")
def delete_post(post_id: int) -> Response:
    """Delete the post and go back to the list; answer 404 for an unknown id."""
    try:
        build_delete_post().execute(post_id)
    except PostNotFoundError:
        abort(HTTP_NOT_FOUND)
    return redirect(url_for("posts.show_all_posts"))


def _load_post_or_404(post_id: int) -> PostViewModel:
    try:
        return PostViewModel.from_entity(build_get_post().execute(post_id))
    except PostNotFoundError:
        abort(HTTP_NOT_FOUND)
