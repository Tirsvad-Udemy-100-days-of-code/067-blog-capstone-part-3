[English](Step-1-Starting-Project) · **Dansk** · [Bahasa Malaysia](Step-1-Starting-Project-ms)

# 1. Startprojektet

![Startprojektet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-1.png)

*Illustration med eksempeldata, tegnet til dette repositorium ud fra lektionsbeskrivelsen. Det er ikke et skærmbillede af kursusprojektet.*

| Verbum | Rute |
| --- | --- |
| `GET` | `/` |

## Hvad lektionen gør

- Download startarkivet, opret et virtuelt miljø (`python -m pip install -r requirements.txt`) og åbn projektet.
- Se på `main.py`, skabelonerne og SQLite-databasen `posts.db`; undersøg felterne (id, title, subtitle, date, body, author, img_url) i en databaseviser.
- De tre eksempelindlæg erstatter den npoint JSON-bin, vi brugte før.

## Hvad vi lærte

- Et projekt er lettere at forstå, når man først ser på dets filer og data.
- En database erstatter en ekstern JSON-bin: én lokal fil med de samme felter.

## Hvor det er i koden

- App-fabrik — `src/blog/presentation/app_factory.py` (`create_app`, `seed-db`)
- Model — `src/blog/infrastructure/persistence/blog_post_model.py`
- Eksempelindlæg — `src/blog/infrastructure/seed.py`

I modsætning til lektionen er der ingen downloadet `posts.db`: kommandoen `seed-db` fylder en ny database med eksempelindlæg, og appen bygges af `create_app`.

---

Forrige: [Hjem](Home-da) · Næste: [Alle indlæg fra databasen](Step-2-All-Posts-da)
