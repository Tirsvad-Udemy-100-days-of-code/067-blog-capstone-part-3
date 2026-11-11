# src

The source code of the Day 67 blog, in the package `blog`, in the layers of the clean architecture: `domain` (entities, repository ports, errors), `application` (use cases), `infrastructure` (SQLAlchemy persistence, settings, seed data) and `presentation` (the Flask app factory, routes, templates). Imports point inward.

The project rules apply: Python 3.13 or newer, constants in `constants.py`, Doxygen-readable docstrings, and tests in `tests/`.
