# Review of the wiki and README after the application

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-019 |
| CrossReference | [MIL-006], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [dcb624d] |

---

## Artifact Under Review

- Instance reviewed: the trilingual wiki in `docs/wiki/` (English, Danish, Bahasa Malaysia; 30 pages and `_Sidebar.md`) and the `README.md`, after the application code landed in G4 to G6
- Checklist used: [QC-WIKI-001]; the README is checked with `framework/scripts/check-readme.sh`
- Scope: delta review. The sidebar, page names and language lines are unchanged since [RC-008]. G6 added a "Where it is in the code" section to the 27 step pages, rewrote the "no application code" sentence on the 3 Home pages, and updated the README (Overview, Setup, Run, Tests, step 1 text)
- Language and domain: en, da, ms / it
- Language reviewer: none named; the Danish and Bahasa Malaysia text was written by the AI and has not been read by a native speaker
- Mode: supervised. This record is the AI's review; confirmed by S01 in chat on 2026-11-11; criterion 14 can only be closed after the merge.

## Checks run

| Check | Command | Result |
| --- | --- | --- |
| README | `bash framework/scripts/check-readme.sh` | exit 0 |
| Wiki structure | a local script over `docs/wiki/` | flat folder; 10 English pages, each with `-da` and `-ms`; every page has the language line; 0 dead links; the new section is present on all 27 step pages |
| Names in the new sections | read against `src/blog` | every file and function named exists, including `delete_post.py`, `delete_post` and the ✘ link in `index.html` |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | `_Sidebar.md` exists | Pass | Unchanged. |
| 2 | Sidebar: bold title, one English list, `Home` first | Pass | Unchanged. |
| 3 | Every English page in the list; no dead link | Pass | 10 English pages; 0 dead links across all pages. |
| 4 | `**Related**` section only when related wikis exist | Pass | None exists; none added. |
| 5 | `**Languages**` is the last sidebar section | Pass | Unchanged. |
| 6 | Sidebar does not repeat the list per language | Pass | Unchanged. |
| 7 | Generated sidebar carries a generator comment | Pass | Hand-written; no generator. |
| 8 | Language line on each page | Pass | Present on all pages. |
| 9 | English plus the PO language | Pass | English is the PO language. |
| 10 | Identical page sets | Pass | 10 pages in each of en, da and ms. |
| 11 | Language line on every page | Pass | Checked by script. |
| 12 | Page naming `<Page>-<code>.md` | Pass | `-da`, `-ms`; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English | Pass | Routes, commands, paths and class names in the new sections are English in every language. |
| 14 | Sidebar, pages and links checked on the published wiki after the change | Pending | The publish workflow runs after the merge. To be checked on the published wiki then, as done in [RC-008]. |
| 15 | Layout rule changes made in the generator and the checklist together | N-A | Optional; no layout rule changed. |
| 16 | Wiki folder is flat | Pass | All files directly in `docs/wiki/`. |

## README

| Item | Result |
| --- | --- |
| `check-readme.sh` | Pass (exit 0) |
| Overview, Setup, Run and Tests describe the working app | Pass: the commands match those used in the checks (`pip install -e ".[dev]"`, `seed-db`, `run`, `pytest`) |
| Every lecture step names its implementing file through the wiki | Pass: the intro says so; step 1 text no longer mentions the lecture's `main.py` |
| The images are still illustrations | Unchanged and stated; S01 may supply real captures |

## Overall Verdict

Go, with one condition: criterion 14 (published wiki) stays pending until after the merge. Every other criterion passes. The Danish and Bahasa Malaysia language criteria remain with S01 as in [RC-008]; the Bahasa Malaysia terms "kes guna", "kilang aplikasi", "port repositori" and "peraturan domain" need a native reader. Mode: supervised, AI draft.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| After the merge, check all pages and the sidebar on the published wiki and close criterion 14 | S01 | 2026-11-18 |
| Have a native reader confirm the Bahasa Malaysia terms listed above | S01 | 2026-11-18 |
| Read the Danish additions | S01 | 2026-11-18 |

---

[MIL-006]: ../../milestones/mil-006-delete-and-documentation-sync.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[RC-008]: ./rc-008-wiki-all-languages.md
[dcb624d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/dcb624dfc80e7f8600fede54fb1c648d7f95d2a3
