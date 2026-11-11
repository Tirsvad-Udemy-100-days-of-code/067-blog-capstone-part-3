[English](Step-7-Prefill-Form) · **Dansk** · [Bahasa Malaysia](Step-7-Prefill-Form-ms)

# 7. Forudfyldt formular

![Forudfyldt formular](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-7.png)

*Skærmbillede af dette repositoriums blog, der kører med eksempeldata, optaget i en browser uden vindue i en Docker-container (se README). Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `GET` | `/edit-post/<int:post_id>` |

## Hvad lektionen gør

- Slå indlægget op, og opret formularen med indlæggets værdier som argumenter (title, subtitle, img_url, author, body).
- Brugeren ser den eksisterende tekst i hvert felt og skal ikke skrive indlægget igen.

## Hvad vi lærte

- At give formularen de eksisterende værdier er måden, en redigeringsside starter fra den nuværende tilstand.
- Genbrug af formularklassen holder oprettelse og redigering ens.

## Hvor det er i koden

- `PostForm.prefilled` — `src/blog/presentation/features/posts/post_form.py`

`PostForm.prefilled` tager en view model af det gemte indlæg i stedet for databaserækken.

---

Forrige: [Redigeringsruten](Step-6-Edit-Route-da) · Næste: [Gem en redigering](Step-8-Save-Edit-da)
