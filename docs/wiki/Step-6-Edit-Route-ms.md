[English](Step-6-Edit-Route) · [Dansk](Step-6-Edit-Route-da) · **Bahasa Malaysia**

# 6. Laluan sunting

![Laluan sunting](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-6.png)

*Tangkapan skrin blog repositori ini yang dijalankan dengan data contoh, dirakam dalam pelayar tanpa kepala dalam bekas Docker (lihat README). Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `GET` | `/edit-post/<int:post_id>` |

## Apa yang dilakukan pelajaran

- Cipta laluan `/edit-post/<post_id>` dan arahkan butang Edit Post pada `post.html` kepadanya dengan id catatan.
- Ubah `<h1>` dalam `make-post.html`: "New Post" semasa mencipta, "Edit Post" semasa menyunting.

## Apa yang kita pelajari

- Satu templat boleh melakukan dua tugas apabila bendera mengubah teks.
- Nama laluan dan id dalam URL menunjukkan apa yang disunting.

## Di mana dalam kod

- Laluan `edit_post` — `src/blog/presentation/features/posts/routes.py`
- Templat — `src/blog/presentation/features/posts/templates/make-post.html` ("Edit Post")

Satu fungsi laluan mengendalikan GET dan POST serta menghantar tajuk "Edit Post" kepada templat yang dikongsi.

---

Sebelumnya: [Simpan catatan baharu](Step-5-Save-New-Post-ms) · Seterusnya: [Borang yang telah diisi](Step-7-Prefill-Form-ms)
