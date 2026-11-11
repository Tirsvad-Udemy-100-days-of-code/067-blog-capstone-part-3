**English** · [Dansk](Step-6-Edit-Route-da) · [Bahasa Malaysia](Step-6-Edit-Route-ms)

# 6. The edit route

![The edit route](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-6.png)

*Screenshot of this repository's blog running with example data, captured in a headless browser in a Docker container (see the README). It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/edit-post/<int:post_id>` |

## What the lecture does

- Create the `/edit-post/<post_id>` route and point the Edit Post button on `post.html` at it with the post's id.
- Change the `<h1>` of `make-post.html`: "New Post" when creating, "Edit Post" when editing.

## What we gained

- One template can serve two jobs when a flag changes the text.
- The route name and the id in the URL say what is edited.

## Where it is in the code

- Route `edit_post` — `src/blog/presentation/features/posts/routes.py`
- Template — `src/blog/presentation/features/posts/templates/make-post.html` ("Edit Post")

One route function handles both GET and POST, and passes the heading "Edit Post" to the shared template.

---

Previous: [Save a new post](Step-5-Save-New-Post) · Next: [Pre-populated form](Step-7-Prefill-Form)
