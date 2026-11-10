**English** · [Dansk](Step-9-Delete-Post-da) · [Bahasa Malaysia](Step-9-Delete-Post-ms)

# 9. Delete a post

![Delete a post](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-9.png)

*Illustration with example data, drawn for this repository from the lecture description. It is not a capture of the course project.*

| Verb | Route |
| --- | --- |
| `GET` | `/delete/<int:post_id>` |

## What the lecture does

- Add a ✘ link beside each post on `index.html`.
- The `/delete/<post_id>` route loads the post, deletes it, commits and redirects to the home page.

## What we gained

- Delete needs the id and a commit, like the other write operations.
- A delete link changes data with GET; it is simple but not safe against prefetching, so real applications prefer POST or DELETE with a confirmation.

---

Previous: [Save an edit](Step-8-Save-Edit)
