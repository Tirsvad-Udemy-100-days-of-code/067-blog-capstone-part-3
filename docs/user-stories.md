# User Story

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [BC-001], [SA-001], [MIL-004], [MIL-005], [MIL-006] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose and Scope

The five things a visitor does in the Day 67 blog: read all posts, read one post, write, edit and delete a post. They are the epics of [MIL-004], [MIL-005] and [MIL-006]. The actor is S02 from [SA-001], running the app locally; there is no login.

## Story List

### US-001.01 — Read all posts

**As a** blog visitor (S02 running the app), **I want** to see every blog post on the home page, **so that** I can browse what has been written.

**Acceptance Criteria**

- Given posts exist in the database, when I open `/`, then every post is listed with title, subtitle, author and date.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-004] | fits one iteration | none | Must | Steps 1 and 2 of the lecture; the base of the app |

### US-001.02 — Read one post

**As a** blog visitor (S02 running the app), **I want** to open a single post by its id, **so that** I can read the whole text.

**Acceptance Criteria**

- Given post 3 exists, when I open `/post/3`, then its full body is shown; given post 99 does not exist, then I get a 404 page.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-004] | fits one iteration | none | Must | Step 3 |

### US-001.03 — Write a new post

**As a** blog visitor (S02 running the app), **I want** to fill in a form with a rich-text body and save it, **so that** a new post appears on the home page.

**Acceptance Criteria**

- Given I open `/new-post`, when I submit a valid form, then the post is saved with today's date and I am redirected to `/`; given a field is empty, then the form shows an error and nothing is saved.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-005] | fits one iteration | none | Must | Steps 4 and 5 |

### US-001.04 — Edit a post

**As a** blog visitor (S02 running the app), **I want** to change an existing post in a pre-filled form, **so that** I do not retype what stays the same.

**Acceptance Criteria**

- Given post 3 exists, when I open `/edit-post/3`, then the form shows its values; when I submit valid changes, then the post is updated, keeps its date and I am redirected to `/post/3`.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-005] | fits one iteration | none | Must | Steps 6 to 8 |

### US-001.05 — Delete a post

**As a** blog visitor (S02 running the app), **I want** to remove a post with one click, **so that** outdated posts leave the blog.

**Acceptance Criteria**

- Given post 3 exists, when I open `/delete/3`, then the post is deleted and I am redirected to `/`; given post 99 does not exist, then I get a 404 page.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-006] | fits one iteration | none | Must | Step 9 |

## INVEST Check

All five stories are Independent once the database exists ([MIL-004]), Negotiable in layout, Valuable to the visitor, Estimable, Small (one route each) and Testable with the Given/When/Then criteria. No exceptions.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-004]: ./milestones/mil-004-application-core-and-read.md
[MIL-005]: ./milestones/mil-005-create-and-edit-posts.md
[MIL-006]: ./milestones/mil-006-delete-and-documentation-sync.md
