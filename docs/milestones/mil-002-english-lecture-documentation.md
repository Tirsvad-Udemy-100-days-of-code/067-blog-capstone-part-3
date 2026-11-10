# G2 English lecture documentation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-10 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [58e2942] |
| 2026-11-10 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-005; autonomous, not independent | [58e2942] |

---

## Purpose

Decide whether the Day 67 lecture is documented in English: every lecture step has a README section and an English wiki page, each with a screenshot and an explanation of what was gained.

## Deliverable

The English wiki (`Home`, nine step pages, `_Sidebar`) in `docs/wiki/`, the nine step sections with screenshots in the README, and the screenshot files in `docs/images/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The README has 9 lecture step sections | 9 | Fewer |
| 2 | Each English wiki step page has a screenshot and a section "What we gained" | 9 of 9 | Fewer |
| 3 | The wiki reviews `Go` against QC-WIKI-001 | Go | Any other verdict |
| 4 | No solution code or lecture archive is reproduced | None found | Any found |
| 5 | The source of each screenshot is recorded | 9 of 9 | Fewer |
| 6 | opengrep reports no High or Critical finding | 0 | Any |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The README skeleton and folders must exist first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2: every step documented with a screenshot | [BC-001] |
| Objective 3: wiki, here the English authoritative text | [BC-001] |
| Concern CN-001, CN-003 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-14 — after MIL-001 and inside the one-week constraint of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Obtain step screenshots | Create one screenshot per lecture step as an illustration with example data (labelled as such), or use captures that S01 supplies, store them in `docs/images/` and record each source. The blog is not run because no code is written. | No | |
| 2 | Write English wiki Home and sidebar | Write the Home page with CRUD and the HTTP verbs GET, POST, PUT, PATCH and DELETE explained, including why an HTML form only sends GET or POST, the step list and the language line, plus `_Sidebar.md` in the shape the wiki process prescribes. | No | |
| 3 | Write English wiki pages for steps 1 to 4 | Document the starting project, listing all posts from `posts.db` with Flask-SQLAlchemy, reading one post by its id, and the new-post form with WTForms and Flask-CKEditor: what each does, and what was gained. | No | |
| 4 | Write English wiki pages for steps 5 to 9 | Document saving a new post (the formatted date, the Jinja `safe` filter), the edit route, pre-populating the form, saving an edit with POST (HTML forms cannot send PUT) without changing the date, and deleting a post, each with what was gained. | No | |
| 5 | Add lecture steps and screenshots to README | Add the nine step sections to the README, each short, with its screenshot and a link to the wiki page, and state plainly that the repository holds no application code. | No | |
| 6 | Review English wiki against QC-WIKI-001 | Review the English wiki and record the `RC-*`. | No | |
| 7 | Run opengrep scan before push | Run opengrep over the repository before pushing the branch. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[58e2942]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/58e2942815801ad36122a1209bcbede2614a07e3
