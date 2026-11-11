[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Dag 67: wiki om den RESTful blog

Noter om dag 67 i Udemy-kurset 100 Days of Code: bloggen udvides, så indlæg kommer fra en database og kan oprettes, redigeres og slettes på selve hjemmesiden. Denne wiki forklarer hvert trin og hvad vi lærte af det. Repositoriet indeholder en fungerende version af bloggen under `src/blog`. Kør den med `flask --app blog.presentation.app_factory:create_app run` efter `flask --app blog.presentation.app_factory:create_app seed-db`; se README.

## Koden

Koden under `src/blog` er delt i lag, og hvert lag afhænger kun af dem indenfor:

- **domain**: indlægsentiteten, valideringsreglen, fejlene og repository-porten.
- **application**: use cases (list, hent, opret, opdater, slet) og de data de tager imod.
- **infrastructure**: SQLAlchemy-lagring, repositoryet, indstillingerne og eksempelindlæggene.
- **presentation**: Flask-app-fabrikken, ruter, formularer og skabeloner.

Hver trinside nedenfor slutter med, hvor dens kode findes.

## CRUD og HTTP-verberne

| Operation | HTTP-verbum | I bloggen |
| --- | --- | --- |
| Create (opret) | POST | Gem et nyt indlæg fra formularen |
| Read (læs) | GET | Vis alle indlæg eller ét indlæg |
| Update (opdater) | PUT / PATCH | Erstat eller ændr et indlæg (her sendt som POST, se trin 8) |
| Delete (slet) | DELETE | Fjern et indlæg (her et link, se trin 9) |

**Hvorfor POST til en redigering?** En HTML-formular kan kun sende GET eller POST. REST-verberne PUT, PATCH og DELETE kræver en klient som JavaScript, så en blog bygget med almindelige formularer og links bruger POST til redigering og et almindeligt link til sletning.

## Værktøjer

- **Flask-SQLAlchemy** læser og skriver `posts.db`.
- **Flask-WTF / WTForms** beskriver og validerer formularen.
- **Flask-CKEditor** gør indholdsfeltet til en rich text-editor.
- **Bootstrap-Flask** tegner formularen med `render_form`.
- **Jinja**-skabeloner viser data; filteret `safe` lader gemt HTML blive vist som HTML.

## Lektionens trin

| Trin | Side |
| --- | --- |
| 1 | [Startprojektet](Step-1-Starting-Project-da) |
| 2 | [Alle indlæg fra databasen](Step-2-All-Posts-da) |
| 3 | [Ét indlæg via dets id](Step-3-One-Post-da) |
| 4 | [Formularen til nyt indlæg](Step-4-New-Post-Form-da) |
| 5 | [Gem et nyt indlæg](Step-5-Save-New-Post-da) |
| 6 | [Redigeringsruten](Step-6-Edit-Route-da) |
| 7 | [Forudfyldt formular](Step-7-Prefill-Form-da) |
| 8 | [Gem en redigering](Step-8-Save-Edit-da) |
| 9 | [Slet et indlæg](Step-9-Delete-Post-da) |
