[English](Step-5-Save-New-Post) · **Dansk** · [Bahasa Malaysia](Step-5-Save-New-Post-ms)

# 5. Gem et nyt indlæg

![Gem et nyt indlæg](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-5.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionsbeskrivelsen. Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `POST` | `/new-post` |

## Hvad lektionen gør

- Ved en gyldig POST oprettes et `BlogPost` ud fra formulardata, tilføjes og gemmes (commit).
- Serveren sætter datoen, formateret som `August 31, 2019`, med modulet `datetime`; den er ikke et formularfelt.
- Omdiriger til forsiden, hvor det nye indlæg vises. I `post.html` får filteret `safe` CKEditor-HTML til at blive vist.

## Hvad vi lærte

- Data, serveren selv kender (datoen), spørger man ikke brugeren om.
- Omdirigering efter POST undgår dobbelt indsendelse ved genindlæsning.
- `safe` er kun forsvarligt, når forfatterne er til at stole på; ikke-renset HTML kan indeholde et script.

---

Forrige: [Formularen til nyt indlæg](Step-4-New-Post-Form-da) · Næste: [Redigeringsruten](Step-6-Edit-Route-da)
