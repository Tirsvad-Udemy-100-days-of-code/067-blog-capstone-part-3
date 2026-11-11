"""The fields of a post that a person writes or edits."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PostContent:
    """Editable content of a post; the id and the date are not part of it."""

    title: str
    subtitle: str
    author: str
    img_url: str
    body: str
