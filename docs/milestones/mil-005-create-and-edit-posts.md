# G5 Create and edit posts

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [SA-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [bb4ab74] |

---

## Purpose

Decide whether a visitor can write a new post and edit an existing one through validated forms, as in lecture steps 4 to 8.

## Deliverable

The `/new-post` and `/edit-post/<post_id>` routes with a WTForms form and a CKEditor body field, the create and update use cases, and the tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `/new-post` shows the form; a valid POST saves the post with today's date and redirects to `/` | Yes | No |
| 2 | An invalid POST shows the field errors and saves nothing | Yes | No |
| 3 | `/edit-post/<post_id>` shows the form pre-filled; a valid POST updates the post, keeps its date and redirects to `/post/<post_id>` | Yes | No |
| 4 | An unknown id on the edit route returns 404 | Yes | No |
| 5 | Every route is covered by a pytest test and `python -m pytest` passes | Pass | Any failure |
| 6 | The code is reviewed Go against its `qc-programming-*` checklist | Go | Other |
| 7 | opengrep reports no High or Critical finding | 0 | Any |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | The domain, persistence and app factory exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| US-001.03 and US-001.04: write and edit a post | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-16 — three days after G4.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Application: create and update post use cases | `CreatePost` sets the date on the server; `UpdatePost` keeps the original date; both validate and raise not-found for an unknown id. | Yes | US-001.03, US-001.04 |
| 2 | Presentation: post form with CKEditor | A WTForms `PostForm` (title, subtitle, author, image URL, body) rendered with Bootstrap-Flask and a CKEditor field, shared by create and edit. | No |  |
| 3 | Presentation: new-post route and template | `/new-post` GET and POST with `make-post.html`, redirect to `/` after saving. | Yes | US-001.03 |
| 4 | Presentation: edit-post route | `/edit-post/<post_id>` reuses `make-post.html` with the heading "Edit Post", pre-fills the form and redirects to the post. | Yes | US-001.04 |
| 5 | Tests for forms, use cases and routes | pytest tests for valid, invalid and unknown-id cases. | No |  |
| 6 | Review against the programming checklist and scan | Review the code against its `qc-programming-*` checklist, record the `RC-*`, run opengrep before the push. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[US-001]: ../user-stories.md
[MIL-004]: ./mil-004-application-core-and-read.md
[bb4ab74]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/bb4ab74b3e8d54bf96382b87bba9c277df4c8b09
