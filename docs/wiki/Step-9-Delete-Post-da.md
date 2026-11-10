[English](Step-9-Delete-Post) · **Dansk** · [Bahasa Malaysia](Step-9-Delete-Post-ms)

# 9. Slet et indlæg

![Slet et indlæg](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-9.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionsbeskrivelsen. Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `GET` | `/delete/<int:post_id>` |

## Hvad lektionen gør

- Tilføj et ✘-link ved hvert indlæg i `index.html`.
- Ruten `/delete/<post_id>` henter indlægget, sletter det, gemmer og omdirigerer til forsiden.

## Hvad vi lærte

- Sletning kræver id og commit, som de andre skriveoperationer.
- Et sletningslink ændrer data med GET; det er enkelt, men ikke sikkert mod forhåndshentning, så rigtige programmer foretrækker POST eller DELETE med bekræftelse.

---

Forrige: [Gem en redigering](Step-8-Save-Edit-da)
