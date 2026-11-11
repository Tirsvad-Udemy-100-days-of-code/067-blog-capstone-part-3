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

    def update(self, post: BlogPost) -> BlogPost | None:
        if post.post_id is None or post.post_id not in self._posts:
            return None
        self._posts[post.post_id] = post
        return post

    def delete(self, post_id: int) -> bool:
        return self._posts.pop(post_id, None) is not None
