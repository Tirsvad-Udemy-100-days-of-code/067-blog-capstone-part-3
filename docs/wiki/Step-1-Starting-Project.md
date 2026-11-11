**English** · [Dansk](Step-1-Starting-Project-da) · [Bahasa Malaysia](Step-1-Starting-Project-ms)

# 1. The starting project

![The starting project](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-1.png)

*Screenshot of this repository's blog running with example data, captured in a headless browser in a Docker container (see the README). It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/` |

## What the lecture does

- Download the starting archive, create a virtual environment (`python -m pip install -r requirements.txt`) and open the project.
- Look at `main.py`, the templates and the `posts.db` SQLite database; inspect its fields (id, title, subtitle, date, body, author, img_url) in a database viewer.
- The three sample posts replace the npoint JSON bin used before.

## What we gained

- A project is easier to understand when you first look at its files and its data.
- A database replaces a remote JSON bin: one local file, same fields.

## Where it is in the code

- App factory — `src/blog/presentation/app_factory.py` (`create_app`, `seed-db`)
- Model — `src/blog/infrastructure/persistence/blog_post_model.py`
- Example posts — `src/blog/infrastructure/seed.py`

Unlike the lecture, there is no downloaded `posts.db`: the `seed-db` command fills a new database with example posts, and the app is built by `create_app`.

---

Previous: [Home](Home) · Next: [All posts from the database](Step-2-All-Posts)
