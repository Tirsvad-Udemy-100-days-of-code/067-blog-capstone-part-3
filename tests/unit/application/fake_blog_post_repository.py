from dataclasses import replace

from blog.domain.entities.blog_post import BlogPost


class FakeBlogPostRepository:
    """In-memory stand-in for the BlogPostRepository port."""

    def __init__(self, posts: list[BlogPost] | None = None) -> None:
        self._posts: dict[int, BlogPost] = {}
        for post in posts or []:
            self.add(post)

    def list_all(self) -> list[BlogPost]:
        return [self._posts[key] for key in sorted(self._posts)]

    def find_by_id(self, post_id: int) -> BlogPost | None:
        return self._posts.get(post_id)

    def add(self, post: BlogPost) -> BlogPost:
        new_id = max(self._posts, default=0) + 1
        stored = replace(post, post_id=new_id)
        self._posts[new_id] = stored
        return stored
