[English](Step-4-New-Post-Form) · [Dansk](Step-4-New-Post-Form-da) · **Bahasa Malaysia**

# 4. Borang catatan baharu

![Borang catatan baharu](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-4.png)

*Tangkapan skrin blog repositori ini yang dijalankan dengan data contoh, dirakam dalam pelayar tanpa kepala dalam bekas Docker (lihat README). Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `GET` | `/new-post` |

## Apa yang dilakukan pelajaran

- Pautkan butang "Create New Post" ke laluan `/new-post` yang memaparkan `make-post.html`.
- Bina WTForm dengan lima medan: tajuk, subtajuk, pengarang, URL imej latar dan kandungan.
- Mulakan Flask-CKEditor dan gunakan `CKEditorField` untuk kandungan, kemudian paparkan borang dengan Bootstrap-Flask.

## Apa yang kita pelajari

- Kelas borang menerangkan medan sekali sahaja; templat memaparkannya.
- Medan teks kaya menghasilkan HTML, jadi kandungan disimpan sebagai markup dan bukan teks biasa.

## Di mana dalam kod

- Borang `PostForm` — `src/blog/presentation/features/posts/post_form.py`
- Laluan `add_new_post` (GET) — `src/blog/presentation/features/posts/routes.py`
- Templat — `src/blog/presentation/features/posts/templates/make-post.html`

Borang ialah `PostForm` yang sama untuk mencipta dan menyunting, dan perlindungan CSRF dihidupkan, jadi setiap borang membawa token.

---

Sebelumnya: [Satu catatan mengikut id](Step-3-One-Post-ms) · Seterusnya: [Simpan catatan baharu](Step-5-Save-New-Post-ms)
