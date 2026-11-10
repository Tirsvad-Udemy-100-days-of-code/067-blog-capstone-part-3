**English** · [Dansk](Step-6-Edit-Route-da) · [Bahasa Malaysia](Step-6-Edit-Route-ms)

# 6. The edit route

![The edit route](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-6.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/edit-post/<int:post_id>` |

## What the lecture does

- Create the `/edit-post/<post_id>` route and point the Edit Post button on `post.html` at it with the post's id.
- Change the `<h1>` of `make-post.html`: "New Post" when creating, "Edit Post" when editing.

## What we gained

- One template can serve two jobs when a flag changes the text.
- The route name and the id in the URL say what is edited.

---

Previous: [Save a new post](Step-5-Save-New-Post) · Next: [Pre-populated form](Step-7-Prefill-Form)
