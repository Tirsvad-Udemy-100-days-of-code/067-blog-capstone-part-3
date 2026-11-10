[English](Step-8-Save-Edit) · **Dansk** · [Bahasa Malaysia](Step-8-Save-Edit-ms)

# 8. Gem en redigering

![Gem en redigering](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-8.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionsbeskrivelsen. Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `POST` | `/edit-post/<int:post_id>` |

## Hvad lektionen gør

- Ved en gyldig indsendelse kopieres formularens værdier over på det eksisterende indlæg og gemmes; datoen ændres ikke.
- Omdiriger til indlæggets side. HTML-formularer kan ikke sende PUT eller PATCH, så redigeringen modtages som POST.

## Hvad vi lærte

- En redigering ændrer en eksisterende række, så der tilføjes intet nyt objekt.
- Almindelige formularer begrænser til GET og POST; verbets hensigt (opdater) ses stadig i ruten og koden.

---

Forrige: [Forudfyldt formular](Step-7-Prefill-Form-da) · Næste: [Slet et indlæg](Step-9-Delete-Post-da)
