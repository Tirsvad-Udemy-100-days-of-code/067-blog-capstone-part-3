[English](Step-7-Prefill-Form) · [Dansk](Step-7-Prefill-Form-da) · **Bahasa Malaysia**

# 7. Borang yang telah diisi

![Borang yang telah diisi](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-7.png)

*Tangkapan skrin blog repositori ini yang dijalankan dengan data contoh, dirakam dalam pelayar tanpa kepala dalam bekas Docker (lihat README). Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `GET` | `/edit-post/<int:post_id>` |

## Apa yang dilakukan pelajaran

- Cari catatan, kemudian cipta borang dengan nilai catatan sebagai argumen (title, subtitle, img_url, author, body).
- Pengguna melihat teks sedia ada dalam setiap medan dan tidak perlu menaip semula catatan.

## Apa yang kita pelajari

- Memberi nilai sedia ada kepada borang ialah cara halaman sunting bermula daripada keadaan semasa.
- Menggunakan semula kelas borang memastikan cipta dan sunting selaras.

## Di mana dalam kod

- `PostForm.prefilled` — `src/blog/presentation/features/posts/post_form.py`

`PostForm.prefilled` menerima view model catatan yang disimpan, bukan baris pangkalan data.

---

Sebelumnya: [Laluan sunting](Step-6-Edit-Route-ms) · Seterusnya: [Simpan suntingan](Step-8-Save-Edit-ms)
