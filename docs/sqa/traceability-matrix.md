# Traceability Matrix: RESTful Blog (Day 67)

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [US-001], [MIL-008] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the baseline milestone, with the review records of all documents (autonomous, not independent) | pending |

---

## Purpose

Tracks backward and forward links between the artifact instances of RESTful Blog (Day 67) so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [US-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007], [MIL-008] | [RC-026], [RC-020], [RC-009], [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001], [US-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007] | [RC-010], [RC-002] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007], [MIL-008] | [RC-027], [RC-021], [RC-011], [RC-003] |
| [US-001] | User Story | en | it | [BC-001], [SA-001] | [MIL-004], [MIL-005], [MIL-006], [MIL-007] | [RC-012] |
| [MIL-001] | Milestone | en | it | [BC-001], [SA-001], [PP-001] | - | [RC-004] |
| [MIL-002] | Milestone | en | it | [BC-001], [SA-001], [PP-001] | - | [RC-005] |
| [MIL-003] | Milestone | en | it | [BC-001], [SA-001], [PP-001] | - | [RC-006] |
| [MIL-004] | Milestone | en | it | [BC-001], [SA-001], [PP-001], [US-001] | - | [RC-013], [RC-016] |
| [MIL-005] | Milestone | en | it | [BC-001], [SA-001], [PP-001], [US-001] | - | [RC-014], [RC-017] |
| [MIL-006] | Milestone | en | it | [BC-001], [SA-001], [PP-001], [US-001] | - | [RC-015], [RC-018], [RC-019] |
| [MIL-007] | Milestone | en | it | [BC-001], [SA-001], [PP-001], [US-001] | - | [RC-022], [RC-023], [RC-024], [RC-025] |
| [MIL-008] | Milestone | en | education | [BC-001], [PP-001], [MIL-007] | - | [RC-028], [RC-029] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-002], [MIL-003] | - | [RC-030], [RC-025], [RC-019], [RC-008], [RC-007] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] (Go/No-Go criteria 1, 2 and 5), [MIL-007] (criteria 1 and 3) | - | - | Covered |
| CN-002 | [MIL-001] (Go/No-Go criterion 4), [MIL-006] (criterion 3) | - | - | Covered |
| CN-003 | [MIL-004] (criteria 1 and 2), [MIL-005] (criteria 1 and 3), [MIL-006] (criterion 1) | - | - | Covered |
| CN-004 | [MIL-001] (Go/No-Go criteria 1 and 4) | - | - | Covered |
| CN-005 | [MIL-004] (criterion 5) | - | - | Covered |
| CN-006 | [MIL-003] (Go/No-Go criteria 1 to 3) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

No view, design or test-plan artifact exists (the scope excludes them), so the concerns are covered by the Go/No-Go criteria of the milestones. In Upstream, `-` means foundational; in Downstream, `-` means nothing is built on it. The domain of BC-001, PP-001 and MIL-008 is `education` since MIL-008; the other documents keep the domain `it` they were accepted with (see the Open Issues of PP-001). The wiki row shows the domain of the project (a wiki is not an artifact with a `Domain` row). MIL-008 adds this matrix and changes no source, image or wiki file; of the tests it changes only the indentation of `tests/e2e/run-in-docker.sh`. The framework has no quality checklist for this matrix, so it has no review record of its own. The review records RC-001 to RC-030 are not rows themselves; RC-016, RC-017, RC-018 and RC-023 review the code of the milestones MIL-004 to MIL-007, and RC-024 and RC-029 review the Docker runner script.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[US-001]: ../user-stories.md
[MIL-001]: ../milestones/mil-001-repository-foundation.md
[MIL-002]: ../milestones/mil-002-english-lecture-documentation.md
[MIL-003]: ../milestones/mil-003-danish-and-malay-wiki.md
[MIL-004]: ../milestones/mil-004-application-core-and-read.md
[MIL-005]: ../milestones/mil-005-create-and-edit-posts.md
[MIL-006]: ../milestones/mil-006-delete-and-documentation-sync.md
[MIL-007]: ../milestones/mil-007-real-screenshots.md
[MIL-008]: ../milestones/mil-008-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-wiki-english.md
[RC-008]: ./reviews/rc-008-wiki-all-languages.md
[RC-009]: ./reviews/rc-009-business-case-rev2.md
[RC-010]: ./reviews/rc-010-stakeholder-analysis-rev2.md
[RC-011]: ./reviews/rc-011-project-plan-rev2.md
[RC-012]: ./reviews/rc-012-user-stories.md
[RC-013]: ./reviews/rc-013-mil-004.md
[RC-014]: ./reviews/rc-014-mil-005.md
[RC-015]: ./reviews/rc-015-mil-006.md
[RC-016]: ./reviews/rc-016-g4-source-code.md
[RC-017]: ./reviews/rc-017-g5-source-code.md
[RC-018]: ./reviews/rc-018-g6-source-code.md
[RC-019]: ./reviews/rc-019-g6-wiki-and-readme.md
[RC-020]: ./reviews/rc-020-business-case-rev3.md
[RC-021]: ./reviews/rc-021-project-plan-rev3.md
[RC-022]: ./reviews/rc-022-mil-007.md
[RC-023]: ./reviews/rc-023-g7-capture-script.md
[RC-024]: ./reviews/rc-024-g7-docker-runner.md
[RC-025]: ./reviews/rc-025-g7-wiki-and-readme.md
[RC-026]: ./reviews/rc-026-business-case-baseline.md
[RC-027]: ./reviews/rc-027-project-plan-baseline.md
[RC-028]: ./reviews/rc-028-milestone-008.md
[RC-029]: ./reviews/rc-029-shell-runner-indent.md
[RC-030]: ./reviews/rc-030-wiki-baseline.md
