**English**

# 8. Save an edit

![Save an edit](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-8.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `POST` | `/edit-post/<int:post_id>` |

## What the lecture does

- On a valid submit, copy the form values onto the existing post and commit; leave the date unchanged.
- Redirect to the post's page. HTML forms cannot send PUT or PATCH, so the edit is accepted as POST.

## What we gained

- An edit changes an existing row, so no new object is added.
- Plain forms limit you to GET and POST; the verb's intent (update) still shows in the route and the code.

---

Previous: [Pre-populated form](Step-7-Prefill-Form) · Next: [Delete a post](Step-9-Delete-Post)
