#!/usr/bin/env bash
# Run tests/e2e/capture_screenshots.py in a Docker container (headless
# Chromium), never on the host desktop (framework/process/gui-testing.md).
#
# Usage: run-in-docker.sh [RESULTS_FOLDER]   (default: docs/images)
# Env:   SCREENSHOT_IMAGE  image with Playwright 1.55 and Chromium
#                          (default mcr.microsoft.com/playwright/python:v1.55.0-noble)
# Needs: bash 4+, docker; the container needs internet (PyPI, CKEditor CDN).
# Exit:  0 success, 1 failure, 2 usage error.
# The repository is mounted read-only; only RESULTS_FOLDER is written.
set -euo pipefail

readonly DEFAULT_IMAGE="mcr.microsoft.com/playwright/python:v1.55.0-noble"

die() {
	echo "error: $*" >&2
	exit 1
}

# The script that runs inside the container. Single quotes are deliberate: the
# variables are expanded there, not here.
# shellcheck disable=SC2016
readonly CONTAINER_SCRIPT='
set -euo pipefail
work="$(mktemp -d)"
trap '"'"'rm -rf "$work"'"'"' EXIT
tar -C /repo \
  --exclude=.venv --exclude=.git --exclude=.mypy_cache \
  --exclude=__pycache__ --exclude=instance --exclude=.env -cf - . | tar -C "$work" -xf -
cd "$work"
pip install --quiet --disable-pip-version-check .
python tests/e2e/capture_screenshots.py /results
'

main() {
	if [[ $# -gt 1 || "${1:-}" == -* ]]; then
		echo "usage: run-in-docker.sh [RESULTS_FOLDER]" >&2
		exit 2
	fi
	local results="${1:-docs/images}"
	local image="${SCREENSHOT_IMAGE:-$DEFAULT_IMAGE}"
	local root
	root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

	command -v docker >/dev/null 2>&1 || die "docker is not installed or not on PATH."
	mkdir -p "$results"
	results="$(cd "$results" && pwd)"

	# MSYS_NO_PATHCONV stops Git Bash on Windows from rewriting /repo and /results.
	# On Windows, pwd gives /c/..., which Docker Desktop accepts.
	MSYS_NO_PATHCONV=1 docker run --rm \
		--ipc=host \
		-v "$root:/repo:ro" \
		-v "$results:/results" \
		"$image" \
		bash -c "$CONTAINER_SCRIPT"
}

main "$@"
