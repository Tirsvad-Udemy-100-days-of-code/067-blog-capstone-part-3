# Review of US-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [US-001], [QC-US-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [US-001]
- Checklist used: [QC-US-001]
- Scope: full review. First version of the user stories, five stories for the blog application.
- Language and domain: en / it
- Language reviewer: S01 (confirmed criteria 3, 5 and 9 of QC-LANG-001)
- Mode: supervised; the AI drafted the review and S01 accepted the plan in chat, 2026-11-11

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Follows INVEST | Pass | INVEST Check section confirms all six; each story is one route. |
| 2 | As a / I want / so that form | Pass | All five stories use the form. |
| 3 | Testable acceptance criteria | Pass | Given/When/Then, including the 404 and invalid-form cases. |
| 4 | Traceable to a use case or epic | Pass | Each story traces to MIL-004, MIL-005 or MIL-006 (a gateway is an epic). |
| 5 | Sized for one iteration | Pass | One route each. |
| 6 | No implementation detail | Pass | Route paths appear because they are the lecture's names (CN-003); no code design. |
| 7 | Role matches an actor in the Use Case Diagram | N/A | The project has no Use Case Diagram. The actor is S02 from SA-001; S01 accepts this by accepting the plan. |
| 8 | One actor goal per story | Pass | One goal per story. |
| 9 | MoSCoW priority with reason | Pass | All Must, with the lecture step as the reason. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | AI proposal: the content is English throughout. Only S01 may confirm. Confirmed by S01 by accepting the plan in chat, 2026-11-11. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is the one the registry gives for this type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | AI proposal: only common IT terms are used and no domain dictionary exists yet. Only S01 may confirm. Confirmed by S01 by accepting the plan in chat, 2026-11-11. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | Language and domain are unchanged (en / it). |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | AI proposal: terms are used correctly. Confirmed by S01 by accepting the plan in chat, 2026-11-11. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Fail | Optional. Acronyms such as PO, SQA, QC and API are used without being spelled out on first use. |

## Overall Verdict

Go — every Mandatory criterion passes; criterion 7 is N/A (no Use Case Diagram exists). Language criteria 3, 5 and 9 were confirmed by S01 (plan acceptance in chat, 2026-11-11). Only the Optional criterion 10 (acronyms) fails and does not block.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Spell out acronyms on first use (optional criterion 10) | S01 | 2026-11-18 |

---

[US-001]: ../../user-stories.md
[QC-US-001]: ../../../framework/qc/artifacts/qc-user-story.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
