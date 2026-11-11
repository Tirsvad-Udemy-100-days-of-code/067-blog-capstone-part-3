"""Error for a post id that does not exist."""


class PostNotFoundError(LookupError):
    """No post has the requested id."""

    def __init__(self, post_id: int) -> None:
        """Remember which id was not found."""
        super().__init__(f"No blog post has the id {post_id}.")
        self.post_id = post_id
