**English** · [Dansk](Step-5-Save-New-Post-da) · [Bahasa Malaysia](Step-5-Save-New-Post-ms)

# 5. Save a new post

![Save a new post](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-5.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `POST` | `/new-post` |

## What the lecture does

- On a valid POST, build a `BlogPost` from the form data, add it and commit.
- The server sets the date, formatted like `August 31, 2019`, with the `datetime` module; it is not a form field.
- Redirect to the home page, where the new post appears. In `post.html` the `safe` filter renders the CKEditor HTML.

## What we gained

- Data that the server can know (the date) is not asked from the user.
- Redirect after POST avoids a duplicate submission on refresh.
- `safe` is only acceptable when the authors are trusted; unsanitised HTML can carry a script.

## Where it is in the code

- Route `add_new_post` (POST) — `src/blog/presentation/features/posts/routes.py`
- Use case — `src/blog/application/use_cases/create_post.py`
- Validation — `src/blog/domain/rules/post_validation.py`

The `CreatePost` use case sets the date as a real `date` (today), validates the content with a domain rule, and the page shows it as "Month DD, YYYY".

---

Previous: [The new-post form](Step-4-New-Post-Form) · Next: [The edit route](Step-6-Edit-Route)
