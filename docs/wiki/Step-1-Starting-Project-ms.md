[English](Step-1-Starting-Project) · [Dansk](Step-1-Starting-Project-da) · **Bahasa Malaysia**

# 1. Projek permulaan

![Projek permulaan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-1.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `GET` | `/` |

## Apa yang dilakukan pelajaran

- Muat turun arkib permulaan, cipta persekitaran maya (`python -m pip install -r requirements.txt`) dan buka projek.
- Lihat `main.py`, templat dan pangkalan data SQLite `posts.db`; periksa medannya (id, title, subtitle, date, body, author, img_url) dalam pelihat pangkalan data.
- Tiga catatan contoh menggantikan npoint JSON bin yang digunakan sebelum ini.

## Apa yang kita pelajari

- Projek lebih mudah difahami apabila kita mula-mula melihat fail dan datanya.
- Pangkalan data menggantikan JSON bin jauh: satu fail setempat dengan medan yang sama.

## Di mana dalam kod

- Kilang aplikasi — `src/blog/presentation/app_factory.py` (`create_app`, `seed-db`)
- Model — `src/blog/infrastructure/persistence/blog_post_model.py`
- Catatan contoh — `src/blog/infrastructure/seed.py`

Berbeza daripada pelajaran, tiada `posts.db` yang dimuat turun: arahan `seed-db` mengisi pangkalan data baharu dengan catatan contoh, dan aplikasi dibina oleh `create_app`.

---

Sebelumnya: [Utama](Home-ms) · Seterusnya: [Semua catatan daripada pangkalan data](Step-2-All-Posts-ms)
