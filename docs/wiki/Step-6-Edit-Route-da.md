[English](Step-6-Edit-Route) · **Dansk** · [Bahasa Malaysia](Step-6-Edit-Route-ms)

# 6. Redigeringsruten

![Redigeringsruten](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-6.png)

*Skærmbillede af dette repositoriums blog, der kører med eksempeldata, optaget i en browser uden vindue i en Docker-container (se README). Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `GET` | `/edit-post/<int:post_id>` |

## Hvad lektionen gør

- Opret ruten `/edit-post/<post_id>`, og peg knappen Edit Post på `post.html` på den med indlæggets id.
- Ret `<h1>` i `make-post.html`: "New Post" ved oprettelse, "Edit Post" ved redigering.

## Hvad vi lærte

- Én skabelon kan klare to opgaver, når et flag ændrer teksten.
- Rutens navn og id'et i URL'en fortæller, hvad der redigeres.

## Hvor det er i koden

- Rute `edit_post` — `src/blog/presentation/features/posts/routes.py`
- Skabelon — `src/blog/presentation/features/posts/templates/make-post.html` ("Edit Post")

Én rutefunktion håndterer både GET og POST og giver overskriften "Edit Post" videre til den fælles skabelon.

---

Forrige: [Gem et nyt indlæg](Step-5-Save-New-Post-da) · Næste: [Forudfyldt formular](Step-7-Prefill-Form-da)
