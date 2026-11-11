# G7 Real screenshots

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-007 |
| CrossReference | [BC-001], [SA-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [0d98508] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted on a Go review, RC-022; supervised, S01 accepted in chat | [0d98508] |

---

## Purpose

Decide whether the nine lecture steps are shown with real screenshots of the running blog instead of illustrations, taken in an isolated container so that the host desktop is never driven.

## Deliverable

A capture script under `tests/e2e/`, a documented way to run it in a Docker container with a headless browser, nine PNG files in `docs/images/` captured from the running app, and the README and the 27 step pages (English, Danish, Bahasa Malaysia) saying that the images are screenshots of the running app.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The capture script runs in a Docker container and writes `step-1.png` to `step-9.png` to a folder shared with the host | 9 of 9 files | Fewer |
| 2 | The host desktop and the Browser pane are not used for the capture | Yes | No |
| 3 | Each image shows the screen its step describes (list, one post, empty form, saved post, edit form, pre-filled form, edited post, list after delete) | S01 confirms by viewing | Any wrong screen |
| 4 | The CKEditor field is rendered in the form screenshots, not a plain text area | Yes | No |
| 5 | No page in the README or the wiki calls the images illustrations | 0 pages | Any |
| 6 | The source of each screenshot (script, date, image) is recorded in the README | Yes | No |
| 7 | `python -m pytest`, ruff and `mypy --strict` pass, and the script is reviewed Go against its `qc-programming-*` checklist | Go | Other |
| 8 | The wiki and README review Go against QC-WIKI-001 and `check-readme.sh`; the published wiki is checked after the merge | Go | Other |
| 9 | opengrep reports no High or Critical finding | 0 | Any |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-006] | The running app with all five routes exists |
| [MIL-003] | The wiki pages in all three languages exist and are edited here |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2: every step documented with a screenshot | [BC-001] |
| Success criterion 2: one screenshot per step in the README and the wiki | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-19 — after MIL-006 and on the extended Business Case end date.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture script for the nine screens | A Playwright script in `tests/e2e/` that starts the app with a throw-away database seeded with the example posts, walks through the nine steps (list, one post, new-post form, save, edit form, pre-filled form, save edit, list after delete) and writes `step-1.png` to `step-9.png`. Environment: Docker container with a headless browser (`framework/process/gui-testing.md`). | No |  |
| 2 | Docker run instructions | Document in the README how to run the script in a container (image, mounts, results folder), so anyone can regenerate the images; the container needs internet for the CKEditor CDN. | No |  |
| 3 | Capture and store the screenshots | Run the script in the container and replace the nine files in `docs/images/` with the captures; record script, date and image used. | No |  |
| 4 | Update README and wiki texts | Remove the illustration disclaimers from the README and the 27 step pages in English, Danish and Bahasa Malaysia and say the images are screenshots of the running app. | No |  |
| 5 | Review, scan and publish check | Review the script against its `qc-programming-*` checklist and the documents against QC-WIKI-001, record the `RC-*`, run opengrep, and check the published wiki after the merge. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[US-001]: ../user-stories.md
[US-001]: ../user-stories.md
[MIL-003]: ./mil-003-danish-and-malay-wiki.md
[MIL-006]: ./mil-006-delete-and-documentation-sync.md
[0d98508]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/0d98508c418c87e70142a6ee48f4030e88538cf4
