[English](Step-9-Delete-Post) · [Dansk](Step-9-Delete-Post-da) · **Bahasa Malaysia**

# 9. Padam catatan

![Padam catatan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-9.png)

*Tangkapan skrin blog repositori ini yang dijalankan dengan data contoh, dirakam dalam pelayar tanpa kepala dalam bekas Docker (lihat README). Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `GET` | `/delete/<int:post_id>` |

## Apa yang dilakukan pelajaran

- Tambah pautan ✘ di sebelah setiap catatan dalam `index.html`.
- Laluan `/delete/<post_id>` mengambil catatan, memadamnya, commit dan mengalih ke halaman utama.

## Apa yang kita pelajari

- Memadam memerlukan id dan commit, seperti operasi tulis yang lain.
- Pautan padam mengubah data dengan GET; ia mudah tetapi tidak selamat daripada pra-ambil, jadi aplikasi sebenar lebih suka POST atau DELETE dengan pengesahan.

## Di mana dalam kod

- Laluan `delete_post` — `src/blog/presentation/features/posts/routes.py`
- Kes guna `DeletePost` — `src/blog/application/use_cases/delete_post.py`
- Pautan ✘ — `src/blog/presentation/features/posts/templates/index.html`

Pautan ✘ pada senarai catatan memanggil laluan, yang menjalankan kes guna `DeletePost` dan bukannya menyentuh pangkalan data terus; id yang tidak dikenali memberi 404.

---

Sebelumnya: [Simpan suntingan](Step-8-Save-Edit-ms)
