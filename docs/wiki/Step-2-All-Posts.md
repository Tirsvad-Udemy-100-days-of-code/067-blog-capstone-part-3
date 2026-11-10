**English**

# 2. All posts from the database

![All posts from the database](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-2.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/` |

## What the lecture does

- In the `/` route, query every `BlogPost` row with Flask-SQLAlchemy instead of reading a JSON bin.
- Pass the rows to `index.html`, which loops over them.

## What we gained

- A SELECT of all rows gives the Read of CRUD for a list.
- The template does not care where the data came from, only that the rows have the same fields.

---

Previous: [The starting project](Step-1-Starting-Project) · Next: [One post by its id](Step-3-One-Post)
