# Review of G7 capture script

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-023 |
| CrossReference | [MIL-007], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [62bc053] |

---

## Artifact Under Review

- Instance reviewed: the capture script `tests/e2e/capture_screenshots.py` and the mypy override for Playwright in `pyproject.toml`
- Checklist used: [QC-PY-001]
- Scope: full review of the script written for task 1 of [MIL-007]. The `python-developer` agent wrote it; the main session re-ran the checks and viewed the nine images.
- Mode: supervised. This record is the AI's review.

## Checks run

| Check | Command | Result |
| --- | --- | --- |
| Tests | `python -m pytest` | 70 passed (the script is not collected by pytest) |
| Lint | `python -m ruff check src tests` | no findings |
| Format | `python -m ruff format --check src tests` | 63 files formatted |
| Types | `python -m mypy --strict src tests` | no issues in 61 files |
| Security scan | `opengrep scan .` | exit 0, 0 findings |
| Capture | `SCREENSHOT_IMAGE=blog-screenshots bash tests/e2e/run-in-docker.sh` | exit 0 twice; nine PNGs each time, byte-identical between the runs; CKEditor 4 rendered in steps 4, 6 and 7 |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | PEP 8 casing | Pass | ruff `N` rules pass. |
| 2 | Names state purpose | Pass | `capture`, `running_app`, `_wait_for_editor`, `_newest_post_id`. |
| 3 | Formatter and linter pass, no unexplained suppressions | Pass | Two `# noqa` comments on the subprocess and URL calls; both are on lines that start the local app or poll it. |
| 4 | Every signature is type-annotated | Pass | `mypy --strict` passes. |
| 5 | No bare except, specific exceptions, cause kept | Pass | A `CaptureError` with a clear message (for example when the editor never renders); no bare `except`. |
| 6 | No mutable defaults, no shadowed builtins | Pass | None found. |
| 7 | Context managers | Pass | `running_app` is a context manager that stops the app in a `finally`; Playwright is used with `with`. |
| 8 | Public items have docstrings | Pass | Module, `CaptureError`, `running_app`, `capture` and `main` have docstrings; private helpers have none (Optional). |
| 9 | Logging, not print; no secrets | Pass | Uses `logging`; the secret key is generated with `secrets.token_hex` at run time. |
| 10 | Traces to the Design Class Diagram | Pass | No DCD exists (see RC-016); the script implements task 1 of [MIL-007]. |
| 11 | Tests for new behaviour | Pass | The script is the end-to-end test: two container runs, both exit 0 with identical images. It has no unit tests of its own. |
| 12 | Strict type checker | Pass | `mypy --strict src tests` passes; `playwright` is in the existing `ignore_missing_imports` override because the host has no Playwright. |
| 13 | Dependencies declared, none unused | Pass | Playwright is provided and pinned by the container image (1.55); the README names the version. |
| 14 | Each piece of knowledge once | Pass | Viewport, timeouts, example texts and paths are named constants at the top of the script. |
| 15 | Imports point inward | Pass | The script imports no `blog` module; it starts the app as a subprocess. |
| 16 | SOLID | Pass | Small functions: start the app, open a page, fill the form, take a shot. |
| 17 | Layer folders | Pass | `tests/e2e/` is one of the three test folders the checklist names. |
| 18 | File and folder names | Pass | `capture_screenshots.py` is English `snake_case`. |

## Overall Verdict

Go — every Mandatory criterion passes and no Optional criterion fails. This is the AI's verdict in supervised mode. S01's go-ahead ("Yes, all of it") was given before the images existed, so S01 confirms by viewing the screenshots and the script in the pull request.

## Residual Risks

| Risk | Impact | Handling |
| --- | --- | --- |
| The script needs internet for PyPI, the CKEditor CDN and the picture host | The capture fails, or the images lack pictures | The script fails loudly when the editor does not render; the README names the three sources |
| The CKEditor version comes from an unpinned CDN | A later run may look different | Accepted; the images record the capture date in the README |

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Look at the nine screenshots in the pull request and confirm each shows its step | S01 | 2026-11-19 |

---

[MIL-007]: ../../milestones/mil-007-real-screenshots.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[62bc053]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/commit/62bc05333e9f6d5f480230cc59bb756611750b41
