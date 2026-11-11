**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Day 67: RESTful blog wiki

Notes on Day 67 of the Udemy course 100 Days of Code: taking the blog further so that posts come from a database and can be created, edited and deleted inside the website. This wiki explains each step and what we gained from it. The repository holds a working version of the blog under `src/blog`. Run it with `flask --app blog.presentation.app_factory:create_app run` after `flask --app blog.presentation.app_factory:create_app seed-db`; see the README.

## The code

The code under `src/blog` is layered, and each layer only depends on the ones inside it:

- **domain**: the post entity, the validation rule, the errors and the repository port.
- **application**: the use cases (list, get, create, update, delete) and the data they take.
- **infrastructure**: SQLAlchemy persistence, the repository, the settings and the example posts.
- **presentation**: the Flask app factory, routes, forms and templates.

Each step page below ends with where its code is.

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
