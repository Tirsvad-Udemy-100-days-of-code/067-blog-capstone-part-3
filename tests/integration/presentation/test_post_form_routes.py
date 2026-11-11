from datetime import date

from flask.testing import FlaskClient

from blog.infrastructure.seed import SEED_POSTS

VALID_FORM = {
    "title": "My new post",
    "subtitle": "A subtitle",
    "author": "Ada",
    "img_url": "https://example.com/pic.png",
    "body": "<p>Hello <strong>world</strong></p>",
}
FIELD_NAMES = ["title", "subtitle", "author", "img_url", "body"]
NEW_POST_ID = len(SEED_POSTS) + 1


def test_new_post_form_shows_all_fields(client: FlaskClient) -> None:
    response = client.get("/new-post")

    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "<h1>New Post</h1>" in page
    for name in FIELD_NAMES:
        assert f'name="{name}"' in page
    assert "ckeditor" in page.lower()


def test_valid_new_post_redirects_and_is_listed_with_todays_date(
    client: FlaskClient,
) -> None:
    response = client.post("/new-post", data=VALID_FORM)

    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    assert "My new post" in client.get("/").get_data(as_text=True)
    page = client.get(f"/post/{NEW_POST_ID}").get_data(as_text=True)
    assert date.today().strftime("%B %d, %Y") in page
    assert "<strong>world</strong>" in page


def test_invalid_new_post_shows_errors_and_saves_nothing(
    client: FlaskClient,
) -> None:
    response = client.post("/new-post", data={**VALID_FORM, "title": "  "})

    assert response.status_code == 200
    assert "This field is required" in response.get_data(as_text=True)
    assert client.get(f"/post/{NEW_POST_ID}").status_code == 404


def test_new_post_with_bad_image_url_shows_error(client: FlaskClient) -> None:
    response = client.post("/new-post", data={**VALID_FORM, "img_url": "nope"})

    assert response.status_code == 200
    assert "Invalid URL" in response.get_data(as_text=True)
    assert client.get(f"/post/{NEW_POST_ID}").status_code == 404


def test_edit_form_is_prefilled(client: FlaskClient) -> None:
    response = client.get("/edit-post/1")

    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "<h1>Edit Post</h1>" in page
    assert SEED_POSTS[0].title in page
    assert SEED_POSTS[0].author in page
    assert SEED_POSTS[0].img_url in page


def test_valid_edit_redirects_keeps_date_and_shows_changes(
    client: FlaskClient,
) -> None:
    response = client.post("/edit-post/1", data=VALID_FORM)

    assert response.status_code == 302
    assert response.headers["Location"] == "/post/1"
    page = client.get("/post/1").get_data(as_text=True)
    assert "My new post" in page
    assert "March 02, 2026" in page


def test_invalid_edit_shows_errors_and_changes_nothing(client: FlaskClient) -> None:
    response = client.post("/edit-post/1", data={**VALID_FORM, "author": ""})

    assert response.status_code == 200
    assert "This field is required" in response.get_data(as_text=True)
    assert SEED_POSTS[0].title in client.get("/post/1").get_data(as_text=True)


def test_edit_unknown_post_gives_404_for_get_and_post(client: FlaskClient) -> None:
    assert client.get("/edit-post/999").status_code == 404
    assert client.post("/edit-post/999", data=VALID_FORM).status_code == 404


def test_pages_link_to_new_and_edit(client: FlaskClient) -> None:
    assert 'href="/new-post"' in client.get("/").get_data(as_text=True)
    assert 'href="/edit-post/1"' in client.get("/post/1").get_data(as_text=True)
