# Review of G5 source code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-017 |
| CrossReference | [MIL-005], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [ac11696] |

---

## Artifact Under Review

- Instance reviewed: the G5 source code (`src/blog/`, `tests/`, `pyproject.toml`) delivered for [MIL-005]
- Checklist used: [QC-PY-001]
- Scope: full review of the code added or changed in G5. The `python-developer` agent wrote it; the main session re-ran every check after the agent reported.
- Mode: supervised. This record is the AI's review, confirmed by S01 in chat on 2026-11-11.

## Checks run

| Check | Command | Result |
| --- | --- | --- |
| Tests | `python -m pytest` | 60 passed (1 warning: Flask-CKEditor reports that `bleach` is not installed) |
| Lint | `python -m ruff check src tests` | no findings |
| Format | `python -m ruff format --check src tests` | 59 files formatted |
| Types | `python -m mypy --strict src tests` | no issues in 57 files |
| Security scan | `opengrep scan .` | exit 0, 0 findings |
| Running app (by the agent) | `flask run` on a temporary database, `curl` with a CSRF token | create 302 to `/`; edit 302 to `/post/1`; POST without token 400; `/edit-post/99` 404; server stopped, temporary database removed |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | PEP 8 casing | Pass | ruff `N` rules pass. |
| 2 | Names state purpose | Pass | `CreatePost`, `UpdatePost`, `PostContent`, `InvalidPostError`, `validate_post`. |
| 3 | Formatter and linter pass, no unexplained suppressions | Pass | Two suppressions, both explained: `# noqa: F401` (model import registers the table) and `# type: ignore[misc]` on `FlaskForm` (Flask-WTF is untyped). |
| 4 | Every signature is type-annotated | Pass | `mypy --strict` passes. |
| 5 | No bare except, specific exceptions, cause kept | Pass | Only `PostNotFoundError` and `InvalidPostError` are caught, in the routes. Nothing is swallowed: not-found becomes 404, invalid becomes form errors. No catch-and-re-raise exists, so `raise ... from` does not apply. |
| 6 | No mutable defaults, no shadowed builtins | Pass | `PostContent` is a frozen dataclass; the clock default is a callable. |
| 7 | Context managers for files and connections | Pass | Sessions are Flask-SQLAlchemy's scoped session. |
| 8 | Public items have docstrings | Pass | ruff `D` rules pass on `src`. |
| 9 | Logging, not print; no secrets in logs | Pass | No `print`. No secret is hard-coded; `SECRET_KEY` comes from `BLOG_SECRET_KEY` or `secrets.token_hex()`. |
| 10 | Classes trace to the Design Class Diagram | Pass | No DCD exists for this project (see RC-016). Each class traces to a task of [MIL-005]. |
| 11 | Tests for new behaviour, order and network independent | Pass | Validation, both use cases (fixed clock, date kept, unknown id), repository update and all route cases (valid, invalid, unknown id, pre-fill, redirects). |
| 12 | Strict type checker | Pass | `mypy --strict` passes; `ignore_missing_imports` for the untyped Bootstrap-Flask, Flask-WTF, Flask-CKEditor and WTForms; two `Any` in `test_post_validation.py`, each explained in a comment. |
| 13 | Dependencies declared, none unused | Pass | Flask-WTF and Flask-CKEditor are now used; the Optional failure in RC-016 is cleared. |
| 14 | Each piece of knowledge once | Pass | The five length limits and the URL schemes are named constants used by the domain rule, the form validators and the database columns. The form's `DataRequired` and the domain's blank check express the same rule on purpose: the form gives immediate messages, the domain stays the authority. |
| 15 | Imports point inward | Pass | `test_dependency_direction` covers `domain` (including `domain/rules`) and `application` (including `application/dto`). |
| 16 | SOLID | Pass | One use case per operation; the port stays narrow (`list_all`, `find_by_id`, `add`, `update`); validation is one function. |
| 17 | Layer folders | Pass | The new code is in the existing four layers; tests in `unit` and `integration`. |
| 18 | File and folder names | Pass | English `snake_case`; `make-post.html` keeps the lecture's template name. |

## Overall Verdict

Go — every Mandatory criterion passes and no Optional criterion fails. Confirmed by S01 in chat, 2026-11-11.

## Residual Risks

| Risk | Impact | Handling |
| --- | --- | --- |
| The post body is stored as CKEditor HTML and shown with `| safe`, with no sanitising (as in the lecture) | Stored XSS if the app is ever exposed to other users | Out of scope by [BC-001] (no hosting, no login); the README says to run it locally only. A sanitiser would be a sixth dependency and needs a Business Case change |
| CKEditor loads from a CDN | The form needs internet in the browser | Stated in the README; the markup is tested, the editor itself is not |
| A random `SECRET_KEY` per start when `BLOG_SECRET_KEY` is unset | Sessions and CSRF tokens do not survive a restart | Stated in the README |
| Whitespace around values is stored as typed | Cosmetic | Accepted; blank values are rejected |

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether a sanitiser (and so a Business Case change) is wanted before any public use | S01 | 2026-11-18 |
| Record the RC for the G6 code the same way | S01 | 2026-11-18 |

---

[MIL-005]: ../../milestones/mil-005-create-and-edit-posts.md
[BC-001]: ../../business-case.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ac11696]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/ac11696bc9343031b4a1b1709b2a7243adc3b982
