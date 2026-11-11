**English** · [Dansk](Step-2-All-Posts-da) · [Bahasa Malaysia](Step-2-All-Posts-ms)

# 2. All posts from the database

![All posts from the database](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-2.png)

*Screenshot of this repository's blog running with example data, captured in a headless browser in a Docker container (see the README). It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/` |

## What the lecture does

- In the `/` route, query every `BlogPost` row with Flask-SQLAlchemy instead of reading a JSON bin.
- Pass the rows to `index.html`, which loops over them.

## What we gained

- A SELECT of all rows gives the Read of CRUD for a list.
- The template does not care where the data came from, only that the rows have the same fields.

## Where it is in the code

- Route `show_all_posts` — `src/blog/presentation/features/posts/routes.py`
- Use case — `src/blog/application/use_cases/list_posts.py`
- Template — `src/blog/presentation/features/posts/templates/index.html`

The route does not query the database itself: it calls the `ListPosts` use case, which reads through a repository port, and the template gets plain view models.

---

Previous: [The starting project](Step-1-Starting-Project) · Next: [One post by its id](Step-3-One-Post)
