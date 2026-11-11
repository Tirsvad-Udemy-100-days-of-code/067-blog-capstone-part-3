# Review of the wiki and README after G7

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-025 |
| CrossReference | [MIL-007], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [62bc053] |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Criterion 14 confirmed on the published wiki; verdict Go | [24e19a7] |

---

## Artifact Under Review

- Instance reviewed: the 27 wiki step pages (English, Danish, Bahasa Malaysia), the README and the nine images in `docs/images/`
- Checklist used: [QC-WIKI-001]
- Scope: delta review. G7 replaced the illustration disclaimer on the 27 step pages, added the README "Screenshots" section, and replaced the nine images. The sidebar, page names and language lines are unchanged since [RC-019].
- Mode: supervised. This record is the AI's review.

## Checks run

| Check | Command | Result |
| --- | --- | --- |
| README | `bash framework/scripts/check-readme.sh` | exit 0 |
| Wording | search of the README and `docs/wiki` for "illustration" in the three languages | 0 hits |
| Wiki structure | a local script over `docs/wiki/` | 0 dead links; 30 pages and the sidebar; the new disclaimer on all 27 step pages |
| Images | viewed with the Read tool | all nine show the screen their step describes; steps 1 and 2 are identical, as the README says |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | `_Sidebar.md` exists | Pass | Unchanged. |
| 2 | Sidebar: bold title, one English list, `Home` first | Pass | Unchanged. |
| 3 | Every English page listed; no dead link | Pass | 0 dead links. |
| 4 | `**Related**` only when related wikis exist | Pass | None. |
| 5 | `**Languages**` is the last sidebar section | Pass | Unchanged. |
| 6 | Sidebar does not repeat the list per language | Pass | Unchanged. |
| 7 | Generated sidebar carries a generator comment | Pass | Hand-written. |
| 8 | Language line on each page | Pass | Unchanged. |
| 9 | English plus the PO language | Pass | Unchanged. |
| 10 | Identical page sets | Pass | 10 pages in each of en, da and ms. |
| 11 | Language line on every page | Pass | Unchanged. |
| 12 | Page naming | Pass | Unchanged. |
| 13 | Code, commands, file names and IDs stay in English | Pass | The new disclaimer text is prose; names are unchanged. |
| 14 | Checked on the published wiki after the change | Pass | Checked on the published wiki on 2026-11-11 after PR 56 merged: all 30 pages return 200; the step 1 pages in en, da and ms carry the new screenshot disclaimer and show `step-1.png`; all nine images return 200 from the `main` branch. |
| 15 | Layout rule changes made in the generator | N-A | Optional; no layout rule changed. |
| 16 | Wiki folder is flat | Pass | Unchanged. |

## Overall Verdict

Go — every criterion passes; criterion 14 was confirmed on the published wiki after the merge (delta check, criterion 14 only). The Danish and Bahasa Malaysia disclaimer sentences were written by the AI and have not been read by a native speaker. This is the AI's verdict in supervised mode. S01's go-ahead ("Yes, all of it") was given before the images existed, so S01 confirms by viewing the screenshots and the script in the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read the new Danish and Bahasa Malaysia disclaimer sentences | S01 | 2026-11-19 |

---

[MIL-007]: ../../milestones/mil-007-real-screenshots.md
[RC-019]: ./rc-019-g6-wiki-and-readme.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[62bc053]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/62bc05333e9f6d5f480230cc59bb756611750b41
[24e19a7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/24e19a78d5794f956b260e5071d25008ac6d379f
