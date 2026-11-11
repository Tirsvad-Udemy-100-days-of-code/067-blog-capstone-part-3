from flask.testing import FlaskClient

from blog.infrastructure.seed import SEED_POSTS


def test_index_lists_every_seeded_title(client: FlaskClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    for post in SEED_POSTS:
        assert post.title in page


def test_post_page_shows_full_body_as_html(client: FlaskClient) -> None:
    response = client.get("/post/1")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert SEED_POSTS[0].title in page
    assert SEED_POSTS[0].body in page


def test_post_page_formats_the_date(client: FlaskClient) -> None:
    page = client.get("/post/1").get_data(as_text=True)

    assert "March 02, 2026" in page


def test_unknown_post_gives_404_page(client: FlaskClient) -> None:
    response = client.get("/post/999")

    assert response.status_code == 404
    assert "Post not found" in response.get_data(as_text=True)


def test_non_numeric_post_id_gives_404(client: FlaskClient) -> None:
    assert client.get("/post/abc").status_code == 404
