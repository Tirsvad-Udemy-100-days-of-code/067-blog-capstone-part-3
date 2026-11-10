[English](Step-5-Save-New-Post) · [Dansk](Step-5-Save-New-Post-da) · **Bahasa Malaysia**

# 5. Simpan catatan baharu

![Simpan catatan baharu](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-5.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

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

---

Sebelumnya: [Borang catatan baharu](Step-4-New-Post-Form-ms) · Seterusnya: [Laluan sunting](Step-6-Edit-Route-ms)
