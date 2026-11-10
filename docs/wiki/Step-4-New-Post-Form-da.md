[English](Step-4-New-Post-Form) · **Dansk** · [Bahasa Malaysia](Step-4-New-Post-Form-ms)

# 4. Formularen til nyt indlæg

![Formularen til nyt indlæg](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-4.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionsbeskrivelsen. Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `GET` | `/new-post` |

## Hvad lektionen gør

- Link knappen "Create New Post" til en `/new-post`-rute, der viser `make-post.html`.
- Byg en WTForm med fem felter: titel, undertitel, forfatter, URL til baggrundsbillede og indhold.
- Initialiser Flask-CKEditor og brug et `CKEditorField` til indholdet, og tegn formularen med Bootstrap-Flask.

## Hvad vi lærte

- En formularklasse beskriver felterne én gang; skabelonen tegner den.
- Et rich text-felt giver HTML, så indholdet gemmes som markup og ikke som ren tekst.

---

Forrige: [Ét indlæg via dets id](Step-3-One-Post-da) · Næste: [Gem et nyt indlæg](Step-5-Save-New-Post-da)
