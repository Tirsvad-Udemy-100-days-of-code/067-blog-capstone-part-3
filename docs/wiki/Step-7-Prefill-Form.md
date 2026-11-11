**English** · [Dansk](Step-7-Prefill-Form-da) · [Bahasa Malaysia](Step-7-Prefill-Form-ms)

# 7. Pre-populated form

![Pre-populated form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-7.png)

*Screenshot of this repository's blog running with example data, captured in a headless browser in a Docker container (see the README). It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/edit-post/<int:post_id>` |

## What the lecture does

- Look up the post, then create the form with the post's values as arguments (title, subtitle, img_url, author, body).
- The user sees the existing text in every field and does not retype the post.

## What we gained

- Passing existing values to the form is how an edit page starts from the current state.
- Reusing the form class keeps create and edit consistent.

## Where it is in the code

- `PostForm.prefilled` — `src/blog/presentation/features/posts/post_form.py`

`PostForm.prefilled` takes a view model of the stored post instead of the database row.

---

Previous: [The edit route](Step-6-Edit-Route) · Next: [Save an edit](Step-8-Save-Edit)
