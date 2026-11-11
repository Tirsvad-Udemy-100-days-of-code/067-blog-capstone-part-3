# G6 Delete posts and documentation sync

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [SA-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the app is complete (delete) and whether the README and wiki now match the working code.

## Deliverable

The `/delete/<post_id>` route and use case with tests, a README Run section that starts the app, and updated wiki pages and screenshots where the code differs from the illustrations.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `/delete/<post_id>` deletes the post and redirects to `/`; an unknown id returns 404 | Yes | No |
| 2 | Every route is covered by a pytest test and `python -m pytest` passes | Pass | Any failure |
| 3 | The README Run and Tests sections work as written on a clean clone | Yes | No |
| 4 | Each wiki step page names the file or function in `src/` that implements it, in all three languages | 11 of 11 each | Any missing |
| 5 | The wiki and README review Go against QC-WIKI-001 and `check-readme.sh` | Go | Other |
| 6 | The code is reviewed Go against its `qc-programming-*` checklist | Go | Other |
| 7 | opengrep reports no High or Critical finding | 0 | Any |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-005] | Create and edit exist before delete and the final documentation |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| US-001.05: delete a post | [US-001] |
| Objectives 2, 3 and 4 of the revised Business Case | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-18 — the extended Business Case end date.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Application and presentation: delete post | `DeletePost` use case and the `/delete/<post_id>` route with a ✘ link on the post list. | Yes | US-001.05 |
| 2 | Tests for delete | pytest tests for deleting an existing post and an unknown id. | No |  |
| 3 | Update README Run and Tests sections | Replace "nothing to run" with the command that starts the app, the seed command and the test command. | No |  |
| 4 | Update wiki pages in three languages | Add the implementing file or function to each step page in English, Danish and Bahasa Malaysia; replace illustrations with real screenshots if S01 supplies them. | No |  |
| 5 | Review, scan and close the project | Review code and documentation, run opengrep, record the `RC-*`. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[US-001]: ../user-stories.md
[MIL-005]: ./mil-005-create-and-edit-posts.md
