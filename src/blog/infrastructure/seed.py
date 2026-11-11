"""Example posts for a new database."""

from datetime import date

from blog.domain.entities.blog_post import BlogPost
from blog.domain.repositories.blog_post_repository import BlogPostRepository

SEED_POSTS: tuple[BlogPost, ...] = (
    BlogPost(
        title="Why I keep a learning log",
        subtitle="Short notes beat good intentions.",
        posted_on=date(2026, 3, 2),
        body=(
            "<p>Every evening I write three lines: what I tried, what broke and "
            "what I will try next.</p><p>After a month the log answered questions "
            "I would otherwise have searched for again.</p>"
        ),
        author="Mira Holt",
        img_url="https://picsum.photos/seed/learning-log/1200/600",
    ),
    BlogPost(
        title="Small functions, small surprises",
        subtitle="What refactoring a 200-line script taught me.",
        posted_on=date(2026, 4, 14),
        body=(
            "<p>The script worked, yet nobody dared to touch it.</p>"
            "<p>Splitting it into functions with one purpose each made the "
            "bugs easy to find and the tests easy to write.</p>"
        ),
        author="Tomas Wren",
        img_url="https://picsum.photos/seed/small-functions/1200/600",
    ),
    BlogPost(
        title="A weekend with SQLite",
        subtitle="One file, no server, plenty of power.",
        posted_on=date(2026, 5, 23),
        body=(
            "<p>SQLite stores a whole database in one file.</p>"
            "<p>For a small blog that is all you need, and you can switch to "
            "a server database later by changing one setting.</p>"
        ),
        author="Mira Holt",
        img_url="https://picsum.photos/seed/sqlite-weekend/1200/600",
    ),
)


def seed_if_empty(repository: BlogPostRepository) -> int:
    """Insert the example posts when there are none; return how many were added."""
    if repository.list_all():
        return 0
    for post in SEED_POSTS:
        repository.add(post)
    return len(SEED_POSTS)
