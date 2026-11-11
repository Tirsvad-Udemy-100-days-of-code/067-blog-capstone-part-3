[English](Step-3-One-Post) · **Dansk** · [Bahasa Malaysia](Step-3-One-Post-ms)

# 3. Ét indlæg via dets id

![Ét indlæg via dets id](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-3.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionsbeskrivelsen. Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `GET` | `/post/<int:post_id>` |

## Hvad lektionen gør

- Gør hver indlægstitel til et link til en rute, der bærer indlæggets unikke id.
- Hent netop den række via id og vis `post.html`; et ukendt id giver en 404-side.

## Hvad vi lærte

- En værdi i URL'en (en stiparameter) udpeger én ressource.
- At hente på primærnøgle er den normale måde at læse én række på.

## Hvor det er i koden

- Rute `show_post` — `src/blog/presentation/features/posts/routes.py`
- Use case — `src/blog/application/use_cases/get_post.py`
- Skabelon — `src/blog/presentation/features/posts/templates/post.html`

Ruten kalder use casen `GetPost`; et ukendt id giver `PostNotFoundError`, som ruten gør til en 404-side.

---

Forrige: [Alle indlæg fra databasen](Step-2-All-Posts-da) · Næste: [Formularen til nyt indlæg](Step-4-New-Post-Form-da)
