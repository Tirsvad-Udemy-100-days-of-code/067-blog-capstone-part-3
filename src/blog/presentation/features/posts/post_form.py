"""The WTForms form shared by creating and editing a post."""

from typing import Self

from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired, Length

from blog.application.dto.post_content import PostContent
from blog.constants import (
    AUTHOR_MAX_LENGTH,
    BODY_MAX_LENGTH,
    IMG_URL_MAX_LENGTH,
    SUBTITLE_MAX_LENGTH,
    TITLE_MAX_LENGTH,
)
from blog.domain.errors.invalid_post_error import InvalidPostError
from blog.presentation.features.posts.post_view_model import PostViewModel


class PostForm(FlaskForm):  # type: ignore[misc]  # Flask-WTF is untyped
    """Fields a person fills in to write or edit a post."""

    title = StringField(
        "Blog Post Title",
        validators=[DataRequired(), Length(max=TITLE_MAX_LENGTH)],
    )
    subtitle = StringField(
        "Subtitle",
        validators=[DataRequired(), Length(max=SUBTITLE_MAX_LENGTH)],
    )
    author = StringField(
        "Your Name",
        validators=[DataRequired(), Length(max=AUTHOR_MAX_LENGTH)],
    )
    img_url = StringField(
        "Blog Image URL",
        validators=[
            DataRequired(),
            URL(require_tld=False),
            Length(max=IMG_URL_MAX_LENGTH),
        ],
    )
    body = CKEditorField(
        "Blog Content",
        validators=[DataRequired(), Length(max=BODY_MAX_LENGTH)],
    )
    submit = SubmitField("Submit Post")

    @classmethod
    def prefilled(cls, post: PostViewModel) -> Self:
        """Build a form that shows the stored values of ``post``."""
        return cls(
            data={
                "title": post.title,
                "subtitle": post.subtitle,
                "author": post.author,
                "img_url": post.img_url,
                "body": post.body_html,
            }
        )

    def to_content(self) -> PostContent:
        """Map the submitted values to the DTO a use case takes."""
        return PostContent(
            title=self.title.data or "",
            subtitle=self.subtitle.data or "",
            author=self.author.data or "",
            img_url=self.img_url.data or "",
            body=self.body.data or "",
        )

    def show_problems(self, error: InvalidPostError) -> None:
        """Show the problems the domain found as errors on their fields."""
        for problem in error.problems:
            field = getattr(self, problem.field)
            field.errors = [*field.errors, problem.message]
