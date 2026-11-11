"""Error for post content that breaks a rule of the domain."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PostProblem:
    """One broken rule: the field it concerns and a readable message."""

    field: str
    message: str


class InvalidPostError(ValueError):
    """The content of a post is not acceptable."""

    def __init__(self, problems: list[PostProblem]) -> None:
        """Remember every problem found, not only the first."""
        summary = "; ".join(
            f"{problem.field}: {problem.message}" for problem in problems
        )
        super().__init__(f"Invalid blog post ({summary}).")
        self.problems = tuple(problems)
