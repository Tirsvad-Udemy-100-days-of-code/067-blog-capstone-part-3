from dataclasses import replace
from typing import Any

import pytest

from blog.constants import (
    AUTHOR_MAX_LENGTH,
    BODY_MAX_LENGTH,
    IMG_URL_MAX_LENGTH,
    SUBTITLE_MAX_LENGTH,
    TITLE_MAX_LENGTH,
)
from blog.domain.errors.invalid_post_error import InvalidPostError
from blog.domain.rules.post_validation import validate_post
from tests.unit.domain.test_blog_post import make_post


# Any: field values are str here; mypy cannot type dataclasses.replace(**kwargs).
def problem_fields(**changes: Any) -> list[str]:
    with pytest.raises(InvalidPostError) as raised:
        validate_post(replace(make_post(), **changes))
    return [problem.field for problem in raised.value.problems]


def test_valid_post_passes() -> None:
    validate_post(make_post())


@pytest.mark.parametrize("field", ["title", "subtitle", "author", "body"])
@pytest.mark.parametrize("blank", ["", "   ", "\n\t"])
def test_blank_text_field_is_rejected(field: str, blank: str) -> None:
    assert problem_fields(**{field: blank}) == [field]


@pytest.mark.parametrize(
    ("field", "limit"),
    [
        ("title", TITLE_MAX_LENGTH),
        ("subtitle", SUBTITLE_MAX_LENGTH),
        ("author", AUTHOR_MAX_LENGTH),
        ("body", BODY_MAX_LENGTH),
    ],
)
def test_text_field_accepts_max_length_and_rejects_one_more(
    field: str, limit: int
) -> None:
    too_long: dict[str, Any] = {field: "x" * limit}
    validate_post(replace(make_post(), **too_long))

    assert problem_fields(**{field: "x" * (limit + 1)}) == [field]


@pytest.mark.parametrize("url", ["https://a.example/x.png", "http://a.example/x"])
def test_img_url_with_http_scheme_passes(url: str) -> None:
    validate_post(replace(make_post(), img_url=url))


@pytest.mark.parametrize("url", ["", "ftp://a.example/x", "example.com/x.png"])
def test_img_url_without_http_scheme_is_rejected(url: str) -> None:
    assert problem_fields(img_url=url) == ["img_url"]


def test_img_url_over_max_length_is_rejected() -> None:
    url = "https://a.example/" + "x" * IMG_URL_MAX_LENGTH

    assert problem_fields(img_url=url) == ["img_url"]


def test_every_problem_is_listed() -> None:
    assert problem_fields(title=" ", author="", img_url="no") == [
        "title",
        "author",
        "img_url",
    ]
