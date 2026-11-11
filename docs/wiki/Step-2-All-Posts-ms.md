[English](Step-2-All-Posts) · [Dansk](Step-2-All-Posts-da) · **Bahasa Malaysia**

# 2. Semua catatan daripada pangkalan data

![Semua catatan daripada pangkalan data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-2.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `GET` | `/` |

## Apa yang dilakukan pelajaran

- Dalam laluan `/`, tanya semua baris `BlogPost` dengan Flask-SQLAlchemy dan bukan membaca JSON bin.
- Hantar baris itu ke `index.html`, yang mengulanginya satu demi satu.

## Apa yang kita pelajari

- SELECT semua baris memberi Read dalam CRUD untuk senarai.
- Templat tidak peduli dari mana data datang, asalkan barisnya mempunyai medan yang sama.

## Di mana dalam kod

- Laluan `show_all_posts` — `src/blog/presentation/features/posts/routes.py`
- Kes guna — `src/blog/application/use_cases/list_posts.py`
- Templat — `src/blog/presentation/features/posts/templates/index.html`

Laluan tidak membuat pertanyaan pangkalan data sendiri: ia memanggil kes guna `ListPosts`, yang membaca melalui port repositori, dan templat menerima view model biasa.

---

Sebelumnya: [Projek permulaan](Step-1-Starting-Project-ms) · Seterusnya: [Satu catatan mengikut id](Step-3-One-Post-ms)
