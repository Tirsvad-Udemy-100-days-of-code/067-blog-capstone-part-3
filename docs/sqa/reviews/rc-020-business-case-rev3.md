# Review of BC-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-020 |
| CrossReference | [BC-001], [QC-BC-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [0d98508] |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-BC-001]
- Scope: full review. Revision 3 of the Business Case: risk 1 and the end date (2026-11-19) updated for G7.
- Language and domain: en / it
- Language reviewer: S01 (confirmed criteria 3, 5 and 9 of QC-LANG-001)
- Mode: supervised; the AI drafted the review and S01 accepted the plan in chat, 2026-11-11

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Cost-benefit justified | Pass | Unchanged; qualitative assessment still justified. |
| 2 | Risks with impact and mitigation | Pass | Risk 1 now has impact and a mitigation (G7 captures real screenshots; illustrations stay until G7 merges). |
| 3 | Success criteria measurable | Pass | Unchanged; criterion 2 (one screenshot per step) is what G7 satisfies with real captures. |
| 4 | In scope and Out of scope separated | Pass | Unchanged. |
| 5 | Stakeholders cross-referenced by ID | Pass | Unchanged. |
| 6 | Methodology stated | Pass | Unchanged. |
| 7 | Assumptions and constraints distinct | Pass | The duration constraint now ends 2026-11-19, with the reason. |
| 8 | Clear recommendation | Pass | Unchanged. |

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

Go — every Mandatory criterion passes. Language criteria 3, 5 and 9 were confirmed by S01 (plan acceptance in chat, 2026-11-11). Only the Optional criterion 10 (acronyms) fails and does not block.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Spell out acronyms on first use (optional criterion 10) | S01 | 2026-11-19 |

---

[BC-001]: ../../business-case.md
[QC-BC-001]: ../../../framework/qc/artifacts/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[0d98508]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/0d98508c418c87e70142a6ee48f4030e88538cf4
