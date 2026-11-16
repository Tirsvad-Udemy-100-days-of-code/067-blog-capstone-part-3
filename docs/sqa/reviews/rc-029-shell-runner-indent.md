# Review Record: Docker runner script against QC-SH-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-029 |
| CrossReference | [MIL-008], [QC-SH-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record; verdict Go (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: the Docker runner script `tests/e2e/run-in-docker.sh`, as changed by task 6 of [MIL-008]
- Checklist used: [QC-SH-001]
- Scope: delta review against [RC-024]. The change re-indents the script from tabs to two spaces, as the baseline `.editorconfig` says (`shfmt -w`); no word of the script changes.
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checks run

| Check | Command | Result |
| --- | --- | --- |
| Whitespace only | `git diff -w -- tests/e2e/run-in-docker.sh` | empty |
| Syntax | `bash -n tests/e2e/run-in-docker.sh` | ok |
| Lint | `shellcheck tests/e2e/run-in-docker.sh` | no finding |
| Format | `shfmt -d tests/e2e/run-in-docker.sh` (reads `.editorconfig`) | no difference |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Starts with `#!/usr/bin/env bash` and `set -euo pipefail` (or a comment explains the exception) | Pass | Unchanged: `#!/usr/bin/env bash` and `set -euo pipefail` in the host script and in the container script. |
| 2 | Every expansion is quoted; lists are arrays; tests use `[[ ]]` and `$(...)` | Pass | Unchanged: expansions are quoted; one `[[ ]]` test; `$(...)` used. |
| 3 | Names follow the conventions: `kebab-case.sh` files, `snake_case` functions and variables, `UPPER_SNAKE` constants and environment variables | Pass | Unchanged: `run-in-docker.sh` is kebab-case; functions and variables are `snake_case`; constants are `UPPER_SNAKE`. |
| 4 | Passes `shellcheck` and `bash -n` with no unexplained `disable` comments | Pass | `bash -n` is silent and `shellcheck` 0.11 or newer reports nothing on the re-indented file; the one `disable=SC2016` is explained in a comment, as before. |
| 5 | Errors go to standard error with an `error:` message and a non-zero exit code; bad or missing arguments print a usage line | Pass | Unchanged: `die` prints `error:` to stderr; a bad argument prints `usage:` and exits 2. |
| 6 | Temporary files use `mktemp` with a `trap ... EXIT` cleanup; no fixed `/tmp` names | Pass | Unchanged: the work copy is made with `mktemp -d` and removed by a `trap` on EXIT. |
| 7 | No secret is written in the script, echoed, or put on a command line; secrets come from the environment or a gitignored file | Pass | Unchanged: no secret in the script; the `.env` file is excluded from the copy into the container. |
| 8 | A script that changes state outside its own directory defaults to a dry run or needs an explicit flag, and says so in its header | Pass | Unchanged: it writes only to the results folder and the repository is mounted read-only; the header says so. |
| 9 | A header comment states purpose, usage, options, environment variables and exit codes | Pass | Unchanged: the header states purpose, usage, environment, needs and exit codes. |
| 10 | The script implements a task or design it cites; deviations are recorded | Pass | Unchanged: it implements task 2 of [MIL-007]; this change implements task 6 of [MIL-008] and only re-indents. |
| 11 | Behaviour is tested for success, failure and any disabled or bypass path | Pass | Not run again: only the indentation changed (the `git diff -w` of the file is empty and `bash -n` passes); the recorded runs of [RC-024] (success, exit 0; usage error, exit 2) stay valid. A new run needs Docker and internet and was not made. |
| 12 | Formatted with `shfmt` (or the project's formatter) | Pass | `shfmt -d tests/e2e/run-in-docker.sh` finds no difference with the baseline `.editorconfig` (two spaces, indented `case`). |
| 13 | Safe to re-run: a second run does not duplicate or corrupt what the first did | Pass | Unchanged: a second run overwrites the images with identical files (recorded in [RC-024]). |
| 14 | Bash version and external tools it needs are stated; GNU-only options are named | Pass | Unchanged: the header states bash 4+, docker and internet. |
| 15 | A command sequence, constant, path or message used more than once is defined once (a function, a variable or a sourced helper); a helper is shared between scripts only where it expresses the same knowledge | Pass | Unchanged: the default image and the container script are each defined once. |

## Overall Verdict

Go — every Mandatory criterion passes; the change is whitespace only. This is the AI's verdict in autonomous mode (not independent).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No open action | S01 | 2026-11-23 |

---

[MIL-008]: ../../milestones/mil-008-framework-baseline.md
[MIL-007]: ../../milestones/mil-007-real-screenshots.md
[QC-SH-001]: ../../../framework/qc/code/qc-programming-shell.md
[RC-024]: ./rc-024-g7-docker-runner.md
