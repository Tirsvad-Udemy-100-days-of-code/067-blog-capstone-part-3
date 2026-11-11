# Project Plan

## Metadata
| Key | Value |
| --- | --- |
| ID | PP-001 |
| CrossReference | [BC-001], [SA-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | S01 | Added gateways G4 to G6 for the blog application; end date moved to 2026-11-18; Go on RC-011, supervised | [bb4ab74] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Added gateway G7 (real screenshots); end date moved to 2026-11-19; stale open issues removed; Go on RC-021, supervised | pending |

---

## Purpose

This plan schedules seven gateways: G1 to G3 delivered the Day 67 README and trilingual wiki; G4 to G6 build the blog application and bring the documentation in line with it; G7 replaces the illustrations with screenshots captured from the running app. The project runs from 2026-11-10 to 2026-11-19 ([BC-001]).

## Planning Assumptions

- The project starts 2026-11-10 and ends by 2026-11-19, per the revised Business Case constraint. G4 to G6 were delivered on 2026-11-11, ahead of their decision dates.
- Each gateway is one branch and one pull request. Gateway length is two to three days.
- S01 owns and approves every gateway, as in [SA-001]; the AI acts as stand-in in autonomous mode.
- Screenshots are illustrations with example data until G7 replaces them with captures of the running app. The captures are taken in a Docker container with a headless browser, as `framework/process/gui-testing.md` requires.

## Gateway Schedule

| Gateway | Document | Window | Decision date | Owner | Stories | Main deliverable | Milestone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G1 Repository foundation | [MIL-001] | 2026-11-10 to 2026-11-12 | 2026-11-12 | S01 | none (technical tasks) | Repository metadata, project configuration, README skeleton, scan | not yet synced |
| G2 English lecture documentation | [MIL-002] | 2026-11-12 to 2026-11-14 | 2026-11-14 | S01 | none (documentation tasks) | English wiki, README steps, screenshots | not yet synced |
| G3 Danish and Bahasa Malaysia wiki | [MIL-003] | 2026-11-14 to 2026-11-16 | 2026-11-16 | S01 | none (documentation tasks) | Danish and Bahasa Malaysia wiki, language links | not yet synced |
| G4 Application core and read routes | [MIL-004] | 2026-11-11 to 2026-11-13 | 2026-11-13 | S01 | US-001.01, US-001.02 | Layers, persistence, app factory, read routes, tests | not yet synced |
| G5 Create and edit posts | [MIL-005] | 2026-11-13 to 2026-11-16 | 2026-11-16 | S01 | US-001.03, US-001.04 | Form, create and edit routes, tests | not yet synced |
| G6 Delete posts and documentation sync | [MIL-006] | 2026-11-16 to 2026-11-18 | 2026-11-18 | S01 | US-001.05 | Delete route, README Run section, wiki aligned with code | not yet synced |
| G7 Real screenshots | [MIL-007] | 2026-11-12 to 2026-11-19 | 2026-11-19 | S01 | none (technical and documentation tasks) | Capture script, nine real screenshots, wiki and README updated | not yet synced |

```plantuml
@startgantt
Project starts 2026-11-10
[G1 Repository foundation] starts 2026-11-10 and ends 2026-11-12
[G1 Go/No-Go] happens 2026-11-12
[G2 English lecture documentation] starts 2026-11-12 and ends 2026-11-14
[G2 Go/No-Go] happens 2026-11-14
[G3 Danish and Bahasa Malaysia wiki] starts 2026-11-14 and ends 2026-11-16
[G3 Go/No-Go] happens 2026-11-16
[G4 Application core and read routes] starts 2026-11-11 and ends 2026-11-13
[G4 Go/No-Go] happens 2026-11-13
[G5 Create and edit posts] starts 2026-11-13 and ends 2026-11-16
[G5 Go/No-Go] happens 2026-11-16
[G6 Delete posts and documentation sync] starts 2026-11-16 and ends 2026-11-18
[G6 Go/No-Go] happens 2026-11-18
[G7 Real screenshots] starts 2026-11-12 and ends 2026-11-19
[G7 Go/No-Go] happens 2026-11-19
@endgantt
```

## Scope Coverage

| Business Case scope item | Gateway |
| --- | --- |
| Repository setup (description, topics, .gitignore, pyproject.toml, Doxyfile, folders) | G1 |
| README with lecture steps, screenshots, venv, run and test instructions | G1 (skeleton and instructions), G2 (steps and screenshots) |
| Wiki in English | G2 |
| Wiki in Danish and Bahasa Malaysia | G3 |
| A screenshot for each lecture step | G2 (README and English wiki, illustrations), G3 (translated pages, illustrations), G7 (real captures replace them) |
| Opengrep scan and AI prompt log | G1 to G6 |
| Blog application with layers and tests (read) | G4 |
| Blog application (create and edit) | G5 |
| Blog application (delete), README and wiki aligned with the code | G6 |
| Real screenshots of the running app in the README and the wiki | G7 |

## Dependencies

```
G1 → G2 → G3 → G4 → G5 → G6 → G7
```

A No-Go at a gateway returns that gateway to S01 for rework; later gateways move by the same number of days. S01 alone decides to move the end date of 2026-11-19.

## Plan Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Real screenshots are not available (BC-001 risk 1) | G2 cannot reach Go | Illustrations are labelled as such; S01 confirms the approach at plan acceptance |
| A pending language criterion needs S01 | A gateway is Go-with-conditions only | S01 confirms the pending criteria at plan acceptance or at the gateway |
| Translations take longer than planned | G3 slips | G3 has a one-day buffer before 2026-11-17 |
| The app takes longer than three small gateways | G6 slips past 2026-11-18 | One route per task; the layers stay thin; S01 decides on moving the end date |
| The headless browser cannot load CKEditor from its CDN in the container | The new-post and edit screenshots show a plain text area | The capture script waits for the editor and fails loudly; the container needs internet access |

## Open Issues

- Until G7 is merged, the screenshots are illustrations with example data drawn for this repository; G7 replaces them with captures of the running app.
- The Python coding rules (`constants.py`, pytest tests, Doxygen comments) apply from G4, when code is added.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-001]: ./milestones/mil-001-repository-foundation.md
[MIL-002]: ./milestones/mil-002-english-lecture-documentation.md
[MIL-003]: ./milestones/mil-003-danish-and-malay-wiki.md
[MIL-004]: ./milestones/mil-004-application-core-and-read.md
[MIL-005]: ./milestones/mil-005-create-and-edit-posts.md
[MIL-006]: ./milestones/mil-006-delete-and-documentation-sync.md
[MIL-007]: ./milestones/mil-007-real-screenshots.md
[US-001]: ./user-stories.md
[58e2942]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/58e2942815801ad36122a1209bcbede2614a07e3
[bb4ab74]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/bb4ab74b3e8d54bf96382b87bba9c277df4c8b09
