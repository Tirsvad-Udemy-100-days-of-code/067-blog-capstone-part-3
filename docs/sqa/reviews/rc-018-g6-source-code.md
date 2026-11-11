# Review of G6 source code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-018 |
| CrossReference | [MIL-006], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the G6 source code (delete post) in `src/blog/` and `tests/`
- Checklist used: [QC-PY-001]
- Scope: full review of the code added or changed in G6. The `python-developer` agent wrote it; the main session re-ran every check and read `routes.py` and `index.html` after the agent reported.
- Mode: supervised. This record is the AI's review, confirmed by S01 in chat on 2026-11-11.

## Checks run

| Check | Command | Result |
| --- | --- | --- |
| Tests | `python -m pytest` | 70 passed (1 warning: Flask-CKEditor reports that `bleach` is not installed) |
| Lint | `python -m ruff check src tests` | no findings |
| Format | `python -m ruff format --check src tests` | 62 files formatted |
| Types | `python -m mypy --strict src tests` | no issues in 60 files |
| Security scan | `opengrep scan .` | exit 0, 0 findings |
| Running app (by the agent) | `seed-db`, `flask run` on a temporary database, `curl` | `/` showed 3 delete links; `GET /delete/1` 302 to `/`; afterwards `/` showed 2 links and `/post/1` was 404; `/delete/999` 404; server stopped by PID, temporary database removed |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | PEP 8 casing | Pass | ruff `N` rules pass. |
| 2 | Names state purpose | Pass | `DeletePost`, `delete_post`, `build_delete_post`. |
| 3 | Formatter and linter pass, no unexplained suppressions | Pass | No new suppression in G6. |
| 4 | Every signature is type-annotated | Pass | `mypy --strict` passes. |
| 5 | No bare except, specific exceptions, cause kept | Pass | Only `PostNotFoundError` is caught, in the route, and becomes a 404. |
| 6 | No mutable defaults, no shadowed builtins | Pass | |
| 7 | Context managers for files and connections | Pass | Sessions are Flask-SQLAlchemy's scoped session. |
| 8 | Public items have docstrings | Pass | ruff `D` rules pass on `src`. |
| 9 | Logging, not print; no secrets in logs | Pass | No `print`, no secret. |
| 10 | Classes trace to the Design Class Diagram | Pass | No DCD exists (see RC-016). `DeletePost` traces to task 1 of [MIL-006]. |
| 11 | Tests for new behaviour, order and network independent | Pass | Unit: deletes, unknown id raises, other posts remain. Integration: repository true/false, route 302, post gone, 404, second delete 404, a delete link per post. |
| 12 | Strict type checker | Pass | `mypy --strict src tests` passes. |
| 13 | Dependencies declared, none unused | Pass | No dependency added. |
| 14 | Each piece of knowledge once | Pass | The not-found rule stays in `DeletePost`; the 404 constant is the shared one. |
| 15 | Imports point inward | Pass | `test_dependency_direction` covers the new use case and the port change. |
| 16 | SOLID | Pass | One use case; the port grew by one narrow method. |
| 17 | Layer folders | Pass | New code is in the existing layers. |
| 18 | File and folder names | Pass | English `snake_case`. |

## Overall Verdict

Go — every Mandatory criterion passes and no Optional criterion fails. Confirmed by S01 in chat, 2026-11-11.

## Residual Risks

| Risk | Impact | Handling |
| --- | --- | --- |
| Delete is a GET link, as in the lecture | A browser prefetch, proxy or crawler can delete posts; there is no confirmation | Documented in a comment at the route and on the wiki page for step 9; the app is local with no login ([BC-001]). A POST form with confirmation would be a later change |
| The ✘ link has no confirmation dialog | An accidental click deletes a post | Same as above |

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether delete should become a POST form with confirmation before any public use | S01 | 2026-11-18 |

---

[MIL-006]: ../../milestones/mil-006-delete-and-documentation-sync.md
[BC-001]: ../../business-case.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
