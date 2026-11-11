[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Hari 67: wiki blog RESTful

Nota tentang Hari 67 kursus Udemy 100 Days of Code: blog dikembangkan supaya catatan datang daripada pangkalan data dan boleh dicipta, disunting dan dipadam di dalam laman web. Wiki ini menerangkan setiap langkah dan apa yang kita pelajari. Repositori ini mengandungi versi blog yang berfungsi di bawah `src/blog`. Jalankannya dengan `flask --app blog.presentation.app_factory:create_app run` selepas `flask --app blog.presentation.app_factory:create_app seed-db`; lihat README.

## Kod

Kod di bawah `src/blog` dibahagi kepada lapisan, dan setiap lapisan hanya bergantung pada lapisan di dalamnya:

- **domain**: entiti catatan, peraturan pengesahan, ralat dan port repositori.
- **application**: kes guna (senarai, dapatkan, cipta, kemas kini, padam) dan data yang diterimanya.
- **infrastructure**: penyimpanan SQLAlchemy, repositori, tetapan dan catatan contoh.
- **presentation**: kilang aplikasi Flask, laluan, borang dan templat.

Setiap halaman langkah di bawah berakhir dengan lokasi kodnya.

## CRUD dan kata kerja HTTP

| Operasi | Kata kerja HTTP | Dalam blog |
| --- | --- | --- |
| Create (cipta) | POST | Simpan catatan baharu daripada borang |
| Read (baca) | GET | Papar semua catatan atau satu catatan |
| Update (kemas kini) | PUT / PATCH | Ganti atau ubah catatan (di sini dihantar sebagai POST, lihat langkah 8) |
| Delete (padam) | DELETE | Buang catatan (di sini satu pautan, lihat langkah 9) |

**Mengapa POST untuk suntingan?** Borang HTML hanya boleh menghantar GET atau POST. Kata kerja REST PUT, PATCH dan DELETE memerlukan klien seperti JavaScript, jadi blog yang dibina dengan borang dan pautan biasa menggunakan POST untuk suntingan dan pautan biasa untuk memadam.

## Alat yang digunakan

- **Flask-SQLAlchemy** membaca dan menulis `posts.db`.
- **Flask-WTF / WTForms** menerangkan dan mengesahkan borang.
- **Flask-CKEditor** menukar medan kandungan menjadi penyunting teks kaya.
- **Bootstrap-Flask** memaparkan borang dengan `render_form`.
- Templat **Jinja** memaparkan data; penapis `safe` membolehkan HTML yang disimpan dipaparkan sebagai HTML.

## Langkah pelajaran

| Langkah | Halaman |
| --- | --- |
| 1 | [Projek permulaan](Step-1-Starting-Project-ms) |
| 2 | [Semua catatan daripada pangkalan data](Step-2-All-Posts-ms) |
| 3 | [Satu catatan mengikut id](Step-3-One-Post-ms) |
| 4 | [Borang catatan baharu](Step-4-New-Post-Form-ms) |
| 5 | [Simpan catatan baharu](Step-5-Save-New-Post-ms) |
| 6 | [Laluan sunting](Step-6-Edit-Route-ms) |
| 7 | [Borang yang telah diisi](Step-7-Prefill-Form-ms) |
| 8 | [Simpan suntingan](Step-8-Save-Edit-ms) |
| 9 | [Padam catatan](Step-9-Delete-Post-ms) |
