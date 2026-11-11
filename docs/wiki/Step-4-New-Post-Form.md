**English** · [Dansk](Step-4-New-Post-Form-da) · [Bahasa Malaysia](Step-4-New-Post-Form-ms)

# 4. The new-post form

![The new-post form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-4.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/new-post` |

## What the lecture does

- Link the "Create New Post" button to a `/new-post` route that renders `make-post.html`.
- Build a WTForm with five fields: title, subtitle, author, background image URL and body.
- Initialise Flask-CKEditor and use a `CKEditorField` for the body, then render the form with Bootstrap-Flask.

## What we gained

- A form class describes the fields once; the template renders it.
- A rich text field produces HTML, so the body is stored as markup, not plain text.

## Where it is in the code

- Form `PostForm` — `src/blog/presentation/features/posts/post_form.py`
- Route `add_new_post` (GET) — `src/blog/presentation/features/posts/routes.py`
- Template — `src/blog/presentation/features/posts/templates/make-post.html`

The form is the same `PostForm` for creating and editing, and CSRF protection is on, so every form carries a token.

---

Previous: [One post by its id](Step-3-One-Post) · Next: [Save a new post](Step-5-Save-New-Post)
