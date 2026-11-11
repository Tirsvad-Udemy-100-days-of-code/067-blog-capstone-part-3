from flask.testing import FlaskClient

from blog.infrastructure.seed import SEED_POSTS


def test_delete_redirects_to_index_and_removes_the_post(client: FlaskClient) -> None:
    response = client.get("/delete/1")

    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    page = client.get("/").get_data(as_text=True)
    assert SEED_POSTS[0].title not in page
    assert client.get("/post/1").status_code == 404


def test_delete_keeps_the_other_posts(client: FlaskClient) -> None:
    client.get("/delete/1")

    page = client.get("/").get_data(as_text=True)
    for post in SEED_POSTS[1:]:
        assert post.title in page


def test_delete_unknown_post_gives_404(client: FlaskClient) -> None:
    assert client.get("/delete/999").status_code == 404


def test_delete_twice_gives_404_the_second_time(client: FlaskClient) -> None:
    assert client.get("/delete/1").status_code == 302
    assert client.get("/delete/1").status_code == 404


def test_index_has_a_delete_link_for_each_post(client: FlaskClient) -> None:
    page = client.get("/").get_data(as_text=True)

    for post_id in range(1, len(SEED_POSTS) + 1):
        assert f'href="/delete/{post_id}"' in page
    assert page.count('title="Delete post"') == len(SEED_POSTS)
