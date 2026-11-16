# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-008] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | S01 | Scope now includes the working Day 67 blog application (G4 to G6), runtime dependencies and end date 2026-11-18; Go on RC-009, supervised | [bb4ab74] |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | S01 | Risk 1 and the end date updated for G7 (real screenshots, end date 2026-11-19); Go on RC-020, supervised | [0d98508] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 8, success criterion 10, a scope item, an out-of-scope item, a risk and two constraints for the baseline milestone MIL-008; set the PO domain to education; reviewed in autonomous mode, not independent | [5fdd0df] |

---

## Executive Summary

This project documents the learning outcome of Day 67 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp", the lecture "Building a RESTful Blog with Editing" (a Flask blog that can read, create, edit and delete posts). The deliverables are a README and a trilingual wiki (English, Danish, Bahasa Malaysia) that walk through each lecture step with a screenshot and explain what was learned, and, from revision 2, the working blog application itself, written by S01 in layers under `src/` with pytest tests under `tests/`. The repository is published on the Tirsystem Gitea host so that fellow course participants and GitHub viewers can read it.

## Methodological and Standards Foundation

- Process: the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist, one pull request per milestone).
- Quality model: ISO/IEC 25010:2023 characteristics tag every QC criterion.
- Documentation: Markdown, reviewed against `QC-WIKI-001` for the wiki and checked with `framework/scripts/check-readme.sh` for the README.
- Repository hygiene: a Python `.gitignore`, `pyproject.toml`, a Doxyfile and a static-analysis scan with opengrep before every push.

## Problem Statement

A course participant learns the Day 67 concepts (CRUD over HTTP routes, Flask-SQLAlchemy, WTForms, Flask-CKEditor, Bootstrap-Flask forms, post-ids in URLs, form pre-population, deleting by route) but keeps no structured record of them. Participants who want to compare solutions find scattered code and no explanation of the lecture steps in context, and none in Danish or Bahasa Malaysia.

## Business Opportunity

A clear, illustrated walk-through of the lecture steps lets S01 consolidate the learning, lets S02 compare against a readable reference, and lets S03 find a well-described repository. A trilingual wiki widens the audience at low cost.

## Objectives

1. Publish a repository with a description, topics, README and licence on the Tirsystem Gitea host.
2. Document each Day 67 lecture step (starting project, all posts, one post, the new-post form, saving a new post, the edit route, the pre-populated form, saving an edit, deleting a post) in the README with one screenshot per step.
3. Publish a wiki in English, Danish and Bahasa Malaysia with the same page set, each page explaining what was gained in that step.
4. Document how to create and use a local `.venv` and run `python -m pip install --upgrade pip`, and how to run the project and its tests.
5. Scan the repository with opengrep before each push.
6. Build the Day 67 blog application (read, create, edit and delete posts) in `src/`, in layers that keep the business rules independent of Flask, with pytest tests for every route and use case.
7. Keep the README and the wiki consistent with the code: each wiki step page names the file that implements it.
8. Bring the finished project to the common baseline of the framework: the adopted framework release, a README that lists only the documents of the repository, project URL and licence metadata, the editor settings of the baseline, an `.env.example` in the framework's form that also lists the environment variables of the program, a shell script formatted as the baseline says, and a traceability matrix that covers the documents ([MIL-008]).

## Scope

### In Scope

- Repository setup: description, topics, Python `.gitignore`, `pyproject.toml` (Python 3.13 or newer, pytest configuration, and the runtime dependencies of the app: Flask, Flask-SQLAlchemy, Flask-WTF, Flask-CKEditor and Bootstrap-Flask), `Doxyfile`, and the folders `docs/`, `src/` and `tests/` as the layout the project uses.
- README from the framework template with the lecture steps, screenshots, venv instructions and run and test instructions.
- Wiki pages in English, Danish and Bahasa Malaysia, one page per lecture step.
- A screenshot for each lecture step in the README and the wiki.
- A local opengrep scan before each push; the AI prompt log under `docs/ai-prompts/`.
- The blog application: domain, application, infrastructure and presentation layers under `src/`, a SQLite database seeded with example posts, the routes `/`, `/post/<post_id>`, `/new-post`, `/edit-post/<post_id>` and `/delete/<post_id>`, and `pytest` tests (added in G4 to G6).
- The baseline milestone [MIL-008]: the framework release, the README without the private framework files in its appendix, project URL and licence metadata, `.editorconfig`, `.env.example`, the indentation of the Docker runner script `tests/e2e/run-in-docker.sh`, a new traceability matrix, review records and a review of the wiki. It changes no behaviour of the program.

### Out of Scope

- Hosting the blog on a public server, user accounts and login (later lecture days), and any copy of the course starting archive or of the course solutions; the code is written for this repository.
- Secrets: `.env` holds personal tokens and is never read into the project, tested or committed.
- Any change to `src/`, `docs/images/` or the wiki pages in the baseline milestone [MIL-008], and any change to `tests/` other than the indentation of `tests/e2e/run-in-docker.sh`. That milestone starts the program on no public address, retakes no screenshot and runs the tests only.

## Expected Benefits

### Tangible Benefits

- One README and a three-language wiki that cover all nine lecture steps.
- A repository that other participants can read without installing anything.

### Intangible Benefits

- Consolidated understanding of CRUD routes, forms and database access in Flask for S01.
- A reusable pattern for documenting the remaining bootcamp days.

## Strategic Alignment

The repository belongs to the Tirsvad Udemy 100 Days of Code collection, one repository per day. It follows the same framework, wiki and review conventions as the other repositories of the Tirsystem host.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lecture steps documented | 9 of 9 steps in the README and in each wiki language | Count of step sections |
| 2 | Screenshots | 1 per lecture step in the README and the wiki | Count of images referenced |
| 3 | Wiki languages | 3 (en, da, ms) with identical page sets | Page list comparison |
| 4 | Repository metadata | Description set and at least 5 topics | Gitea API response |
| 5 | Security scan | 0 findings of High or Critical severity | opengrep output before each push |
| 6 | Runtime dependencies | Only the five named in scope | `dependencies` list in `pyproject.toml` |
| 7 | Reviews | 100 percent of artifacts have an `RC-*` verdict | Files in `docs/sqa/reviews/` |
| 8 | Application routes | 5 of 5 work | Route tests pass in `python -m pytest` |
| 9 | Code review | Every code milestone has a `Go` against its `qc-programming-*` checklist | Files in `docs/sqa/reviews/` |
| 10 | The baseline milestone is done (objective 8) | `framework/scripts/check-readme.sh`, `check-languages.sh` and `check-editorconfig.sh` exit with code 0, `shfmt -d` finds no difference, `python -m pytest` passes, 100 % of the continuous integration (CI) checks of the pull request of [MIL-008] pass | The script exit codes and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Screenshots of lecture steps are illustrations, not captures of the running app | Objective 2 met only in part | G7 captures the nine screens from the running app in a Docker container with a headless browser and replaces the illustrations; until G7 is merged the illustrations stay, labelled as such |
| The lecture material is copyrighted by the course author | Legal exposure | Summarise in own words, never reproduce solution code or the starting archive |
| Danish or Bahasa Malaysia text is machine quality | Misleading translation | English is authoritative; S01 reviews the languages S01 reads; Bahasa Malaysia is flagged as not reviewed by a native speaker |
| A token leaks into the repository | Account compromise | `.env` is in `.gitignore`, is never opened by project tooling, and an opengrep scan runs before each push |
| Gitea wiki publishing is not enabled | Wiki not visible | Keep the wiki in `docs/wiki/`, enable the wiki in the repository settings, verify after merge |
| The documents of the baseline milestone [MIL-008] change documents that were accepted earlier, and an AI stand-in for S01 reviews them | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, `src/` is not changed, the only change in `tests/` is the indentation of one script, the tests run before and after, and the end-of-run summary lists the reviews for challenge |

## Assumptions

- S01 is Product Owner, developer and reviewer; the AI acts as stand-in reviewer in autonomous mode.
- The Product Owner (PO) language is English; the PO domain is education since [MIL-008] (it was information technology (IT) until then; the documents that [MIL-008] does not change keep the domain `it`, see the Open Issues of [PP-001]).
- The Gitea repository exists and `.env` holds tokens for the personal use of S01.
- Wiki pages are published by the `publish-wiki-pages.yml` workflow after merge.

## Constraints

- Python 3.13 or newer, `venv`, `pytest`, `pyproject.toml`; runtime dependencies only the five named in scope.
- Folder structure `src/`, `tests/`, `docs/`.
- Application code is written layer by layer with tests; the code follows `coding-conventions` and `clean-architecture`.
- One branch and one pull request per milestone.
- Duration: 2026-11-10 to 2026-11-19 (extended from 2026-11-17 for the application milestones G4 to G6, and to 2026-11-19 for the screenshot milestone G7).
- The baseline milestone [MIL-008] starts 2026-11-16 and is finished within one week, by 2026-11-23, so the end date of the plan moves from 2026-11-19 to 2026-11-23. An AI stand-in for S01 reviews and accepts the changed documents.
- The program has no secret in the repository: the secret key and the database address are read from the environment variables `BLOG_SECRET_KEY` and `BLOG_DATABASE_URI` at run time (both optional; without a key a random one is made per start), and `.env.example` holds empty placeholders only.

## Cost–Benefit Assessment

A qualitative assessment is justified: the project is a personal learning record with no revenue.

| Costs | Benefits |
| --- | --- |
| About 8 hours of S01 review and screenshot work, plus AI drafting effort | Consolidated learning, a shareable reference for S02 and S03, reach in three languages |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owner, developer and reviewer; wants a record of the learning |
| S02 | Reads the README, compares solutions and runs the instructions |
| S03 | Browses the repository for ideas; needs description, topics and README |

## Recommendation

Proceed — G1 to G3 delivered the documentation; the application is three further small gateways (G4 to G6) that end on 2026-11-18.

---

[SA-001]: ./stakeholder-analysis.md
[58e2942]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/58e2942815801ad36122a1209bcbede2614a07e3
[bb4ab74]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/bb4ab74b3e8d54bf96382b87bba9c277df4c8b09
[0d98508]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/0d98508c418c87e70142a6ee48f4030e88538cf4
[PP-001]: ./project-plan.md
[MIL-008]: ./milestones/mil-008-framework-baseline.md
[5fdd0df]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/5fdd0df00e7b3e3bf40c95942b5a3f57f249e1d2
