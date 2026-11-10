**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Day 67: RESTful blog wiki

Notes on Day 67 of the Udemy course 100 Days of Code: taking the blog further so that posts come from a database and can be created, edited and deleted inside the website. This wiki explains each step and what we gained from it. The repository holds no application code; the code belongs to the course.

## CRUD and the HTTP verbs

| Operation | HTTP verb | In the blog |
| --- | --- | --- |
| Create | POST | Save a new post from the form |
| Read | GET | Show all posts, or one post |
| Update | PUT / PATCH | Replace or change a post (here sent as POST, see step 8) |
| Delete | DELETE | Remove a post (here a link, see step 9) |

**Why POST for an edit?** An HTML form can only send GET or POST. The REST verbs PUT, PATCH and DELETE need a client such as JavaScript, so a blog built with plain forms and links uses POST for edits and a plain link for delete.

## Tools used

- **Flask-SQLAlchemy** reads and writes `posts.db`.
- **Flask-WTF / WTForms** describes and validates the form.
- **Flask-CKEditor** turns the body field into a rich text editor.
- **Bootstrap-Flask** renders the form with `render_form`.
- **Jinja** templates show the data; the `safe` filter lets saved HTML render as HTML.

## The lecture steps

| Step | Page |
| --- | --- |
| 1 | [The starting project](Step-1-Starting-Project) |
| 2 | [All posts from the database](Step-2-All-Posts) |
| 3 | [One post by its id](Step-3-One-Post) |
| 4 | [The new-post form](Step-4-New-Post-Form) |
| 5 | [Save a new post](Step-5-Save-New-Post) |
| 6 | [The edit route](Step-6-Edit-Route) |
| 7 | [Pre-populated form](Step-7-Prefill-Form) |
| 8 | [Save an edit](Step-8-Save-Edit) |
| 9 | [Delete a post](Step-9-Delete-Post) |
