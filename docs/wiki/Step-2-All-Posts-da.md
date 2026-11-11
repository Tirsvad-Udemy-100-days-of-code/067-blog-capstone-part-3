[English](Step-2-All-Posts) · **Dansk** · [Bahasa Malaysia](Step-2-All-Posts-ms)

# 2. Alle indlæg fra databasen

![Alle indlæg fra databasen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-2.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionsbeskrivelsen. Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `GET` | `/` |

## Hvad lektionen gør

- I ruten `/` hentes alle `BlogPost`-rækker med Flask-SQLAlchemy i stedet for at læse en JSON-bin.
- Rækkerne sendes til `index.html`, som løber dem igennem.

## Hvad vi lærte

- Et SELECT af alle rækker giver Read i CRUD for en liste.
- Skabelonen er ligeglad med, hvor data kom fra, bare rækkerne har de samme felter.

## Hvor det er i koden

- Rute `show_all_posts` — `src/blog/presentation/features/posts/routes.py`
- Use case — `src/blog/application/use_cases/list_posts.py`
- Skabelon — `src/blog/presentation/features/posts/templates/index.html`

Ruten forespørger ikke selv databasen: den kalder use casen `ListPosts`, som læser gennem en repository-port, og skabelonen får rene view models.

---

Forrige: [Startprojektet](Step-1-Starting-Project-da) · Næste: [Ét indlæg via dets id](Step-3-One-Post-da)
