# Review of G4 source code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the G4 source code (`src/blog/`, `tests/`, `pyproject.toml`) delivered for [MIL-004]
- Checklist used: [QC-PY-001]
- Scope: full review of the code written in G4. The code was written by the AI (the `python-developer` agent and the main session) and the checks below were re-run by the main session after the agent reported.
- Mode: supervised. This record is the AI's review, confirmed by S01 in chat on 2026-11-11.

## Checks run

| Check | Command | Result |
| --- | --- | --- |
| Tests | `python -m pytest` | 18 passed |
| Lint | `python -m ruff check src tests` | no findings |
| Format | `python -m ruff format --check src tests` | 47 files formatted |
| Types | `python -m mypy --strict src` | no issues in 30 files |
| Security scan | `opengrep scan .` | exit 0, no finding |
| Running app | `flask --app blog.presentation.app_factory:create_app seed-db`, then `run` | `/` 200, `/post/1` 200, `/post/99` 404 |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | PEP 8 casing | Pass | ruff `N` rules pass. |
| 2 | Names state purpose | Pass | `ListPosts`, `GetPost`, `PostNotFoundError`, `BlogPostRepository`; no abbreviations. |
| 3 | Formatter and linter pass, no unexplained suppressions | Pass | One `# noqa: F401` in `app_factory.py`, explained: the model import registers the table before `create_all`. |
| 4 | Every signature is type-annotated | Pass | `mypy --strict` passes. |
| 5 | No bare except, specific exceptions, cause kept | Pass | One `except PostNotFoundError` in `routes.py`; `abort` raises inside the handler, so Python keeps the cause as the implicit context. No explicit `raise ... from`; acceptable here. |
| 6 | No mutable defaults, no shadowed builtins | Pass | The entity field is `post_id`, not `id`. |
| 7 | Context managers for files and connections | Pass | Sessions come from Flask-SQLAlchemy's scoped session, closed by the framework at the end of the request. |
| 8 | Public items have docstrings | Pass | ruff `D` rules pass on `src`. |
| 9 | Logging, not print; no secrets in logs | Pass | No `print`; no logging needed yet. |
| 10 | Classes trace to the Design Class Diagram | Pass | No DCD exists for this project. The classes follow the layers in `clean-architecture`; each traces to a task of [MIL-004]. Recorded here as the deviation. |
| 11 | Tests for new behaviour, named for behaviour, order and network independent | Pass | Unit tests with a fake repository; integration tests on in-memory SQLite and the Flask test client. |
| 12 | Strict type checker | Pass | `mypy --strict src` and `tests` pass; one `ignore_missing_imports` for Bootstrap-Flask, which ships no types. |
| 13 | Dependencies declared, none unused | Fail | Optional. Flask-WTF and Flask-CKEditor are declared but first used in G5. Noted in `pyproject.toml`. |
| 14 | Each piece of knowledge once | Pass | Constants live in `constants.py`; the date format is applied only in the view model; use-case wiring only in `composition_root.py`. |
| 15 | Imports point inward | Pass | `tests/unit/test_dependency_direction.py` parses `domain` and `application` with `ast` and fails on any framework, infrastructure or presentation import. |
| 16 | SOLID | Pass | One responsibility per use case; the repository is a narrow `Protocol`; use cases receive it in the constructor. |
| 17 | Layer folders under `src/` and `tests/` | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/blog/`; `unit` and `integration` under `tests/`. `e2e` is not needed yet. |
| 18 | File and folder names | Pass | English `snake_case`, no spaces. |

## Overall Verdict

Go — every Mandatory criterion passes. Only the Optional criterion 13 fails and does not block. Confirmed by S01 in chat, 2026-11-11.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Use Flask-WTF and Flask-CKEditor in the post form (clears optional criterion 13) | S01 | 2026-11-16 |
| Record the first RC for G5 and G6 code the same way | S01 | 2026-11-18 |

---

[MIL-004]: ../../milestones/mil-004-application-core-and-read.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
