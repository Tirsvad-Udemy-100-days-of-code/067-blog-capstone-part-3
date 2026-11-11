[English](Step-5-Save-New-Post) · [Dansk](Step-5-Save-New-Post-da) · **Bahasa Malaysia**

# 5. Simpan catatan baharu

![Simpan catatan baharu](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-5.png)

*Tangkapan skrin blog repositori ini yang dijalankan dengan data contoh, dirakam dalam pelayar tanpa kepala dalam bekas Docker (lihat README). Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `POST` | `/new-post` |

## Apa yang dilakukan pelajaran

- Pada POST yang sah, bina `BlogPost` daripada data borang, tambah dan commit.
- Pelayan menetapkan tarikh, diformatkan seperti `August 31, 2019`, dengan modul `datetime`; ia bukan medan borang.
- Alih ke halaman utama, tempat catatan baharu muncul. Dalam `post.html`, penapis `safe` memaparkan HTML CKEditor.

## Apa yang kita pelajari

- Data yang pelayan sendiri tahu (tarikh) tidak ditanya daripada pengguna.
- Alih selepas POST mengelakkan penghantaran berganda apabila halaman dimuat semula.
- `safe` hanya wajar apabila pengarang boleh dipercayai; HTML yang tidak dibersihkan boleh membawa skrip.

## Di mana dalam kod

- Laluan `add_new_post` (POST) — `src/blog/presentation/features/posts/routes.py`
- Kes guna — `src/blog/application/use_cases/create_post.py`
- Pengesahan — `src/blog/domain/rules/post_validation.py`

Kes guna `CreatePost` menetapkan tarikh sebagai `date` sebenar (hari ini), mengesahkan kandungan dengan peraturan domain, dan halaman memaparkannya sebagai "Month DD, YYYY".

---

Sebelumnya: [Borang catatan baharu](Step-4-New-Post-Form-ms) · Seterusnya: [Laluan sunting](Step-6-Edit-Route-ms)
