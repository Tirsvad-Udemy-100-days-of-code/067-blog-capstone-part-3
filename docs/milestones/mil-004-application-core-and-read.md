# G4 Application core and read routes

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [bb4ab74] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted on a Go review, RC-013; supervised, S01 accepted in chat | [3a93e6e] |

---

## Purpose

Decide whether the Day 67 blog app runs and shows posts from a SQLite database, built in layers so the business rules do not depend on Flask.

## Deliverable

The domain and application layers, the SQLAlchemy persistence, the Flask app factory, the routes `/` and `/post/<post_id>` with their templates, the runtime dependencies in `pyproject.toml`, and pytest tests, all under `src/` and `tests/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The app starts with the command given in the README and `/` lists every seeded post | Yes | No |
| 2 | `/post/<post_id>` shows one post; an unknown id returns 404 | Yes | No |
| 3 | The domain layer imports neither Flask nor SQLAlchemy | Verified by a test | Any import |
| 4 | Every route is covered by a pytest test and `python -m pytest` passes | Pass | Any failure |
| 5 | `pyproject.toml` lists the runtime dependencies with version ranges and the README setup installs them | Yes | No |
| 6 | The code is reviewed Go against its `qc-programming-*` checklist | Go | Other |
| 7 | opengrep reports no High or Critical finding | 0 | Any |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | The documentation baseline is merged before code is added |
| [BC-001] | The revised Business Case allows code and runtime dependencies |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Revised Business Case objectives for the working app | [BC-001] |
| US-001.01 and US-001.02: read all posts, read one post | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-13 — two days after the plan revision, inside the extended Business Case end date of 2026-11-18.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add runtime dependencies and layout | Declare Flask, Flask-SQLAlchemy, Flask-WTF, Flask-CKEditor and Bootstrap-Flask in `pyproject.toml`; create the layer folders under `src/` and `constants.py`; update the README Setup. | No |  |
| 2 | Domain: BlogPost entity and repository port | A `BlogPost` entity (id, title, subtitle, date, body, author, img_url) and a repository interface; no framework imports. | No |  |
| 3 | Persistence: SQLAlchemy repository and seed data | A SQLite `posts.db` repository implementing the port, and a seed script with example posts written for this repository (not the course data). | No |  |
| 4 | Application: list and get post use cases | `ListPosts` and `GetPost` use cases that raise a not-found error for an unknown id. | Yes | US-001.01, US-001.02 |
| 5 | Presentation: app factory and read routes | Flask app factory, routes `/` and `/post/<post_id>` (404 on not found), templates `index.html` and `post.html`. | Yes | US-001.01, US-001.02 |
| 6 | Tests for the domain, use cases and routes | pytest tests in `tests/unit` and `tests/integration` using an in-memory database. | No |  |
| 7 | Review against the programming checklist and scan | Review the code against its `qc-programming-*` checklist, record the `RC-*`, run opengrep before the push. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[US-001]: ../user-stories.md
[MIL-003]: ./mil-003-danish-and-malay-wiki.md
[bb4ab74]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/bb4ab74b3e8d54bf96382b87bba9c277df4c8b09
[3a93e6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/3a93e6e214b76dd96767afa669d649c23225b5f6
