[English](Step-8-Save-Edit) · [Dansk](Step-8-Save-Edit-da) · **Bahasa Malaysia**

# 8. Simpan suntingan

![Simpan suntingan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/067-blog-capstone-part-3/raw/branch/main/docs/images/step-8.png)

*Ilustrasi dengan data contoh, dilukis untuk repositori ini berdasarkan huraian pelajaran. Ia bukan tangkapan projek kursus.*

| Kata kerja | Laluan |
| --- | --- |
| `POST` | `/edit-post/<int:post_id>` |

## Apa yang dilakukan pelajaran

- Pada penghantaran yang sah, salin nilai borang ke catatan sedia ada dan commit; tarikh tidak diubah.
- Alih ke halaman catatan. Borang HTML tidak boleh menghantar PUT atau PATCH, jadi suntingan diterima sebagai POST.

## Apa yang kita pelajari

- Suntingan mengubah baris sedia ada, jadi tiada objek baharu ditambah.
- Borang biasa menghadkan kepada GET dan POST; niat kata kerja (kemas kini) masih kelihatan dalam laluan dan kod.

---

Sebelumnya: [Borang yang telah diisi](Step-7-Prefill-Form-ms) · Seterusnya: [Padam catatan](Step-9-Delete-Post-ms)
