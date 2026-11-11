[English](Step-8-Save-Edit) · **Dansk** · [Bahasa Malaysia](Step-8-Save-Edit-ms)

# 8. Gem en redigering

![Gem en redigering](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-8.png)

*Skærmbillede af dette repositoriums blog, der kører med eksempeldata, optaget i en browser uden vindue i en Docker-container (se README). Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `POST` | `/edit-post/<int:post_id>` |

## Hvad lektionen gør

- Ved en gyldig indsendelse kopieres formularens værdier over på det eksisterende indlæg og gemmes; datoen ændres ikke.
- Omdiriger til indlæggets side. HTML-formularer kan ikke sende PUT eller PATCH, så redigeringen modtages som POST.

## Hvad vi lærte

- En redigering ændrer en eksisterende række, så der tilføjes intet nyt objekt.
- Almindelige formularer begrænser til GET og POST; verbets hensigt (opdater) ses stadig i ruten og koden.

## Hvor det er i koden

- Rute `edit_post` (POST) — `src/blog/presentation/features/posts/routes.py`
- Use case `UpdatePost` — `src/blog/application/use_cases/update_post.py`

Use casen `UpdatePost` erstatter kun titel, undertitel, forfatter, billed-URL og indhold, så id'et og den oprindelige dato bevares; redigeringen sendes som POST og er beskyttet af CSRF.

---

Forrige: [Forudfyldt formular](Step-7-Prefill-Form-da) · Næste: [Slet et indlæg](Step-9-Delete-Post-da)
