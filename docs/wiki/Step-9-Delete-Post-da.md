[English](Step-9-Delete-Post) · **Dansk** · [Bahasa Malaysia](Step-9-Delete-Post-ms)

# 9. Slet et indlæg

![Slet et indlæg](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-9.png)

*Skærmbillede af dette repositoriums blog, der kører med eksempeldata, optaget i en browser uden vindue i en Docker-container (se README). Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `GET` | `/delete/<int:post_id>` |

## Hvad lektionen gør

- Tilføj et ✘-link ved hvert indlæg i `index.html`.
- Ruten `/delete/<post_id>` henter indlægget, sletter det, gemmer og omdirigerer til forsiden.

## Hvad vi lærte

- Sletning kræver id og commit, som de andre skriveoperationer.
- Et sletningslink ændrer data med GET; det er enkelt, men ikke sikkert mod forhåndshentning, så rigtige programmer foretrækker POST eller DELETE med bekræftelse.

## Hvor det er i koden

- Rute `delete_post` — `src/blog/presentation/features/posts/routes.py`
- Use case `DeletePost` — `src/blog/application/use_cases/delete_post.py`
- Link ✘ — `src/blog/presentation/features/posts/templates/index.html`

Linket ✘ på indlægslisten kalder ruten, som kører use casen `DeletePost` i stedet for at røre databasen direkte; et ukendt id giver en 404.

---

Forrige: [Gem en redigering](Step-8-Save-Edit-da)
