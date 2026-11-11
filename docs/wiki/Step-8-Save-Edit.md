**English** · [Dansk](Step-8-Save-Edit-da) · [Bahasa Malaysia](Step-8-Save-Edit-ms)

# 8. Save an edit

![Save an edit](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-8.png)

*Screenshot of this repository's blog running with example data, captured in a headless browser in a Docker container (see the README). It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `POST` | `/edit-post/<int:post_id>` |

## What the lecture does

- On a valid submit, copy the form values onto the existing post and commit; leave the date unchanged.
- Redirect to the post's page. HTML forms cannot send PUT or PATCH, so the edit is accepted as POST.

## What we gained

- An edit changes an existing row, so no new object is added.
- Plain forms limit you to GET and POST; the verb's intent (update) still shows in the route and the code.

## Where it is in the code

- Route `edit_post` (POST) — `src/blog/presentation/features/posts/routes.py`
- Use case `UpdatePost` — `src/blog/application/use_cases/update_post.py`

The `UpdatePost` use case replaces only title, subtitle, author, image URL and body, so the id and the original date stay; the edit is sent as POST and protected by CSRF.

---

Previous: [Pre-populated form](Step-7-Prefill-Form) · Next: [Delete a post](Step-9-Delete-Post)
