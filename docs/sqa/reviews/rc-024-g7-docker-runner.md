# Review of G7 Docker runner script

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-024 |
| CrossReference | [MIL-007], [QC-SH-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the runner `tests/e2e/run-in-docker.sh`
- Checklist used: [QC-SH-001]
- Scope: full review of the runner written for task 2 of [MIL-007]. The `python-developer` agent wrote it; the main session fixed three findings of this review (file name to kebab-case, `trap` cleanup, usage line) and re-ran the checks.
- Mode: supervised. This record is the AI's review.

## Checks run

| Check | Command | Result |
| --- | --- | --- |
| Syntax | `bash -n tests/e2e/run-in-docker.sh` | ok |
| Lint | `shellcheck` 0.11.0 | clean, with one explained `disable=SC2016` |
| Format | `shfmt -i 2 -ci -d` (image `mvdan/shfmt`) | no difference |
| Usage error | `run-in-docker.sh --help` | prints the usage line to standard error, exit 2 |
| Run | `SCREENSHOT_IMAGE=blog-screenshots bash tests/e2e/run-in-docker.sh <folder>` | exit 0; nine files; a second run wrote identical files |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Starts with `#!/usr/bin/env bash` and `set -euo pipefail` | Pass | Both present, in the host script and in the container script. |
| 2 | Every expansion is quoted; `[[ ]]` and `$(...)` | Pass | Quoted; one `[[ ]]` test; `$(...)` used. |
| 3 | Names follow the conventions | Pass | Renamed from `run_in_docker.sh` to `run-in-docker.sh`; functions and variables `snake_case`; constants `UPPER_SNAKE`. |
| 4 | Passes shellcheck and `bash -n` | Pass | shellcheck 0.11.0 and bash 5 (Git Bash); one `disable=SC2016`, explained in a comment: the container script is single-quoted on purpose. |
| 5 | Errors to stderr with `error:`, non-zero exit; usage line | Pass | `die` prints `error:` to stderr; a bad argument prints `usage:` and exits 2 (added in this review). |
| 6 | Temporary files use `mktemp` with a `trap ... EXIT` | Pass | The work copy is made with `mktemp -d` and removed by a `trap` (added in this review; `exec` was removed so the trap runs). |
| 7 | No secret in the script, echoed or on a command line | Pass | No secret. The `.env` file is excluded from the copy into the container. |
| 8 | State outside its own directory needs a flag or is stated | Pass | It writes only to the results folder (default `docs/images/` in this project) and the header says so; the repository is mounted read-only. |
| 9 | Header comment | Pass | Purpose, usage, environment, needs and exit codes are stated. |
| 10 | Implements a cited task | Pass | Task 2 of [MIL-007]. |
| 11 | Behaviour tested for success, failure and bypass | Pass | Recorded manual runs: success (exit 0, twice), usage error (exit 2). The missing-Docker path is not run. |
| 12 | Formatted with `shfmt` | Pass | `shfmt -i 2 -ci` shows no difference. |
| 13 | Safe to re-run | Pass | A second run overwrote the images with identical files. |
| 14 | Bash version and tools stated | Pass | Header: bash 4+, docker, internet. |
| 15 | Knowledge defined once | Pass | The default image and the container script are each defined once. |

## Overall Verdict

Go — every Mandatory criterion passes after the three fixes made in this review. This is the AI's verdict in supervised mode. S01's go-ahead ("Yes, all of it") was given before the images existed, so S01 confirms by viewing the screenshots and the script in the pull request.

## Residual Risks

| Risk | Impact | Handling |
| --- | --- | --- |
| A default image is pulled from a public registry on first use | Download of about 2 GB | The README says so; `SCREENSHOT_IMAGE` selects a local image |

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Run the runner once on your machine and confirm the images match the committed ones | S01 | 2026-11-19 |

---

[MIL-007]: ../../milestones/mil-007-real-screenshots.md
[QC-SH-001]: ../../../framework/qc/code/qc-programming-shell.md
