[English](Step-3-One-Post) · [Dansk](Step-3-One-Post-da) · **Bahasa Malaysia**

# 3. Satu catatan mengikut id

![Satu catatan mengikut id](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-3.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `GET` | `/post/<int:post_id>` |

## Apa yang dilakukan pelajaran

- Jadikan setiap tajuk catatan pautan ke laluan yang membawa id unik catatan itu.
- Ambil baris itu mengikut id dan paparkan `post.html`; id yang tidak dikenali memberi halaman 404.

## Apa yang kita pelajari

- Nilai dalam URL (parameter laluan) memilih satu sumber.
- Mengambil mengikut kunci utama ialah cara biasa membaca satu baris.

## Di mana dalam kod

- Laluan `show_post` — `src/blog/presentation/features/posts/routes.py`
- Kes guna — `src/blog/application/use_cases/get_post.py`
- Templat — `src/blog/presentation/features/posts/templates/post.html`

Laluan memanggil kes guna `GetPost`; id yang tidak dikenali menimbulkan `PostNotFoundError`, yang ditukar oleh laluan kepada halaman 404.

---

Sebelumnya: [Semua catatan daripada pangkalan data](Step-2-All-Posts-ms) · Seterusnya: [Borang catatan baharu](Step-4-New-Post-Form-ms)
