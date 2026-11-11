"""Constants shared by every layer of the blog application."""

from typing import Final

APP_TITLE: Final = "Day 67 Blog"
DATABASE_FILE_NAME: Final = "posts.db"
DATABASE_URI_ENVIRONMENT_VARIABLE: Final = "BLOG_DATABASE_URI"
SECRET_KEY_ENVIRONMENT_VARIABLE: Final = "BLOG_SECRET_KEY"
DATE_DISPLAY_FORMAT: Final = "%B %d, %Y"

# Limits of the post fields. The domain rule, the form validators and the
# database columns all read these, so each limit is defined once.
SHORT_TEXT_MAX_LENGTH: Final = 250
TITLE_MAX_LENGTH: Final = SHORT_TEXT_MAX_LENGTH
SUBTITLE_MAX_LENGTH: Final = SHORT_TEXT_MAX_LENGTH
AUTHOR_MAX_LENGTH: Final = SHORT_TEXT_MAX_LENGTH
IMG_URL_MAX_LENGTH: Final = SHORT_TEXT_MAX_LENGTH
BODY_MAX_LENGTH: Final = 100_000
IMG_URL_SCHEMES: Final = ("http://", "https://")

HTTP_NOT_FOUND: Final = 404
