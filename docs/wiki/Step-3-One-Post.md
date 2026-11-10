**English**

# 3. One post by its id

![One post by its id](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-3.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/post/<int:post_id>` |

## What the lecture does

- Make each post title a link to a route that carries the post's unique id.
- Fetch that one row by id and render `post.html`; an unknown id gives a 404 page.

## What we gained

- A value in the URL (a path parameter) selects one resource.
- Fetching by primary key is the normal way to read one row.

---

Previous: [All posts from the database](Step-2-All-Posts) · Next: [The new-post form](Step-4-New-Post-Form)
