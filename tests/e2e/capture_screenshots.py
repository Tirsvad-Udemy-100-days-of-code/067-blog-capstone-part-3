"""Capture nine screenshots of the blog with headless Chromium.

Not collected by pytest (the name has no ``test_`` prefix). It needs Playwright
and a browser, so it runs inside a container (see ``run-in-docker.sh``), never
on the host desktop (``framework/process/gui-testing.md``).

Usage: ``python capture_screenshots.py [OUTPUT_FOLDER]`` (default ``/results``).
"""

import logging
import os
import secrets
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

LOGGER = logging.getLogger("capture_screenshots")

DEFAULT_OUTPUT = "/results"
HOST = "127.0.0.1"
VIEWPORT = {"width": 1000, "height": 700}
SERVER_START_TIMEOUT_SECONDS = 30.0
STOP_TIMEOUT_SECONDS = 5.0
EDITOR_TIMEOUT_MS = 30_000
PAGE_TIMEOUT_MS = 15_000
SRC_FOLDER = Path(__file__).resolve().parents[2] / "src"

EXAMPLE_TITLE = "Notes from a rainy Sunday"
EXAMPLE_SUBTITLE = "Three small things worth writing down."
EXAMPLE_AUTHOR = "Alex Example"
EXAMPLE_IMAGE_URL = "https://picsum.photos/seed/rainy-sunday/1200/600"
EXAMPLE_BODY = "<p>Tea tastes better when it rains.</p><p>Write the note today.</p>"
EDITED_TITLE = "Notes from a sunny Monday"


class CaptureError(RuntimeError):
    """A step of the screenshot run failed."""


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.bind((HOST, 0))
        return int(probe.getsockname()[1])


def _app_environment(database_file: Path) -> dict[str, str]:
    environment = dict(os.environ)
    environment["BLOG_DATABASE_URI"] = f"sqlite:///{database_file}"
    environment["BLOG_SECRET_KEY"] = secrets.token_hex(16)
    environment["PYTHONPATH"] = str(SRC_FOLDER)
    return environment


def _flask_command(*arguments: str) -> list[str]:
    return [
        sys.executable,
        "-m",
        "flask",
        "--app",
        "blog.presentation.app_factory:create_app",
        *arguments,
    ]


def _wait_until_up(base_url: str, server: subprocess.Popen[bytes]) -> None:
    deadline = time.monotonic() + SERVER_START_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        if server.poll() is not None:
            raise CaptureError(f"the app exited early with code {server.returncode}")
        try:
            with urllib.request.urlopen(f"{base_url}/", timeout=2):  # noqa: S310
                return
        except (urllib.error.URLError, OSError):
            time.sleep(0.3)
    raise CaptureError(f"the app did not answer at {base_url}/ in time")


def _stop(server: subprocess.Popen[bytes]) -> None:
    server.terminate()
    try:
        server.wait(timeout=STOP_TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        server.kill()
        server.wait()


@contextmanager
def running_app() -> Iterator[str]:
    """Seed a throw-away database, start the app and yield its base URL."""
    with tempfile.TemporaryDirectory() as folder:
        environment = _app_environment(Path(folder) / "screenshots.db")
        subprocess.run(
            _flask_command("seed-db"), env=environment, check=True, timeout=60
        )
        port = _free_port()
        server = subprocess.Popen(  # noqa: S603
            _flask_command("run", "--host", HOST, "--port", str(port)),
            env=environment,
        )
        try:
            base_url = f"http://{HOST}:{port}"
            _wait_until_up(base_url, server)
            yield base_url
        finally:
            _stop(server)


def _wait_for_editor(page: Page) -> None:
    """Wait until CKEditor has rendered; fail loudly when it never does."""
    try:
        page.wait_for_selector(
            ".cke, .ck-editor", state="visible", timeout=EDITOR_TIMEOUT_MS
        )
        page.wait_for_function(
            "() => window.CKEDITOR && CKEDITOR.instances.body"
            " && CKEDITOR.instances.body.status === 'ready'",
            timeout=EDITOR_TIMEOUT_MS,
        )
    except Exception as error:  # Playwright raises its own TimeoutError
        raise CaptureError(
            "the CKEditor editor did not render; is the CDN reachable from the "
            f"container? ({error})"
        ) from error
    # Let the editor finish painting its toolbar before the screenshot.
    page.wait_for_timeout(500)


def _shot(page: Page, output: Path, number: int, *, full_page: bool = False) -> None:
    target = output / f"step-{number}.png"
    page.screenshot(path=str(target), full_page=full_page)
    LOGGER.info("wrote %s", target)


def _open(page: Page, base_url: str, path: str) -> None:
    page.goto(f"{base_url}{path}", wait_until="load")


def _fill_form(page: Page, title: str) -> None:
    page.fill("#title", title)
    page.fill("#subtitle", EXAMPLE_SUBTITLE)
    page.fill("#author", EXAMPLE_AUTHOR)
    page.fill("#img_url", EXAMPLE_IMAGE_URL)


def _newest_post_id(page: Page, title: str) -> int:
    href = page.get_by_role("link", name=title, exact=True).get_attribute("href")
    if href is None:
        raise CaptureError(f"no link for the post {title!r} on the home page")
    return int(href.rsplit("/", 1)[1])


def capture(base_url: str, output: Path) -> None:
    """Drive the nine steps and write ``step-1.png`` to ``step-9.png``."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            context = browser.new_context(viewport=VIEWPORT)
            context.set_default_timeout(PAGE_TIMEOUT_MS)
            page = context.new_page()
            _run_steps(page, base_url, output)
        finally:
            browser.close()


def _run_steps(page: Page, base_url: str, output: Path) -> None:
    _open(page, base_url, "/")
    _shot(page, output, 1)
    _shot(page, output, 2, full_page=True)

    _open(page, base_url, "/post/1")
    _shot(page, output, 3)

    _open(page, base_url, "/new-post")
    _wait_for_editor(page)
    _shot(page, output, 4)

    _fill_form(page, EXAMPLE_TITLE)
    page.evaluate("(html) => CKEDITOR.instances.body.setData(html)", EXAMPLE_BODY)
    page.click("#submit")
    page.wait_for_url(f"{base_url}/")
    page.get_by_role("link", name=EXAMPLE_TITLE, exact=True).wait_for()
    _shot(page, output, 5)
    post_id = _newest_post_id(page, EXAMPLE_TITLE)

    _open(page, base_url, f"/edit-post/{post_id}")
    page.get_by_role("heading", name="Edit Post").wait_for()
    _wait_for_editor(page)
    _shot(page, output, 6)
    _shot(page, output, 7, full_page=True)

    page.fill("#title", EDITED_TITLE)
    page.click("#submit")
    page.wait_for_url(f"{base_url}/post/{post_id}")
    page.get_by_role("heading", name=EDITED_TITLE).first.wait_for()
    _shot(page, output, 8)

    _open(page, base_url, "/")
    page.get_by_role("link", name=f"Delete post: {EDITED_TITLE}").click()
    page.wait_for_url(f"{base_url}/")
    if page.get_by_role("link", name=EDITED_TITLE, exact=True).count() != 0:
        raise CaptureError("the deleted post is still on the home page")
    _shot(page, output, 9)


def main(arguments: list[str]) -> int:
    """Run the capture; return the process exit code."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    output = Path(arguments[0] if arguments else DEFAULT_OUTPUT)
    output.mkdir(parents=True, exist_ok=True)
    try:
        with running_app() as base_url:
            capture(base_url, output)
    except Exception:
        LOGGER.exception("screenshot run failed")
        return 1
    LOGGER.info("all nine screenshots written to %s", output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
