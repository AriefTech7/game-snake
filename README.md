# 🐍 Snake Game

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Turtle](https://img.shields.io/badge/Library-Turtle-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Sebuah implementasi klasik permainan **Snake (Ular)** yang dibangun menggunakan modul bawaan Python, **Turtle Graphics**. Proyek ini menyelesaikan masalah kebutuhan akan contoh implementasi Object-Oriented Programming (OOP) sederhana dalam membangun game 2D interaktif tanpa dependensi eksternal, lengkap dengan sistem skor persisten (high score) yang tersimpan di penyimpanan lokal.

---

## ✨ Fitur Utama

- **Kontrol Arah Responsif** — Kendalikan ular menggunakan tombol panah (Up, Down, Left, Right) pada keyboard.
- **Mekanisme Pertumbuhan Ular** — Badan ular akan bertambah panjang secara dinamis setiap kali berhasil memakan makanan.
- **Deteksi Tabrakan (Collision Detection)**:
  - Deteksi tabrakan dengan dinding batas layar.
  - Deteksi tabrakan ular dengan badan/ekornya sendiri.
- **Sistem Skor & High Score** — Skor bertambah otomatis saat memakan makanan, dan skor tertinggi (*high score*) disimpan secara persisten ke dalam file `data.txt`.
- **Reset Otomatis** — Permainan akan otomatis mereset posisi ular dan skor saat terjadi tabrakan (game over), tanpa perlu menutup aplikasi.
- **Posisi Makanan Acak** — Makanan akan muncul di posisi acak dalam area permainan setelah dimakan.
- **Rendering Ringan** — Menggunakan `screen.tracer(0)` dan `screen.update()` manual untuk animasi yang halus dan efisien.

---

## 🛠️ Teknologi yang Digunakan (Tech Stack)

| Kategori | Teknologi |
|---|---|
| Bahasa Pemrograman | Python 3.12 |
| Library Grafis | `turtle` (Standard Library) |
| Library Utilitas | `random`, `time` (Standard Library) |
| Penyimpanan Data | File teks lokal (`data.txt`) |
| Paradigma | Object-Oriented Programming (OOP) |

> **Catatan:** Proyek ini **tidak memerlukan library eksternal** (tidak ada `requirements.txt`) karena seluruh dependensi (`turtle`, `random`, `time`) merupakan bagian dari Python Standard Library.

---

## 📋 Prasyarat (Prerequisites)

Sebelum menjalankan proyek ini, pastikan sistem Anda memiliki:

- **Python 3.12 atau lebih baru** terinstal.
- Modul **Tkinter** aktif pada instalasi Python (dibutuhkan oleh `turtle` untuk membuka jendela GUI).
  - Di Linux (Debian/Ubuntu), instal dengan: `sudo apt-get install python3-tk`
  - Di Windows/macOS, Tkinter biasanya sudah terpasang secara default bersama Python.
- Editor teks atau IDE (opsional, misalnya VS Code, PyCharm).

---

## ⚙️ Instalasi

1. **Clone repositori** ini ke komputer lokal Anda:
```bash
   git clone https://github.com/username/snake-game.git
   cd snake-game
```

2. **(Opsional) Buat virtual environment** untuk isolasi proyek:
```bash
   python -m venv venv
   source venv/bin/activate   # Untuk Linux/macOS
   venv\Scripts\activate      # Untuk Windows
```

3. **Instal dependensi** — tidak ada library eksternal yang perlu diinstal via `pip`, karena semua modul yang digunakan (`turtle`, `random`, `time`) sudah tersedia bawaan Python.

4. **Siapkan file penyimpanan skor** — pastikan file `data.txt` tersedia pada direktori proyek. Jika belum ada, buat secara manual dengan isi awal `0`:
```bash
   echo "0" > data.txt
```

5. **Sesuaikan path penyimpanan skor** — pada file `scoreboard.py`, path menuju `data.txt` saat ini masih menggunakan path absolut (hardcoded):
```python
   with open("/home/guebanget/Documents/Python/Codingan Python Project/data.txt") as file:
```
   Disarankan untuk mengubahnya menjadi path relatif agar proyek portable di komputer lain, contoh:
```python
   with open("data.txt") as file:
```

---

## ▶️ Cara Penggunaan (Usage)

Jalankan aplikasi melalui terminal/command prompt dengan perintah berikut dari direktori root proyek:

```bash
python main.py
```

**Kontrol permainan:**

| Tombol | Aksi |
|---|---|
| `↑` (Arrow Up) | Menggerakkan ular ke atas |
| `↓` (Arrow Down) | Menggerakkan ular ke bawah |
| `←` (Arrow Left) | Menggerakkan ular ke kiri |
| `→` (Arrow Right) | Menggerakkan ular ke kanan |

**Contoh alur permainan:**
1. Jendela game berwarna hitam berukuran 600x600 akan terbuka.
2. Ular (kotak putih) akan bergerak otomatis ke arah kanan.
3. Gunakan tombol panah untuk mengarahkan ular menuju makanan (lingkaran abu-abu).
4. Setiap makanan yang dimakan akan menambah skor dan memperpanjang badan ular.
5. Jika ular menabrak dinding atau badannya sendiri, skor akan direset dan permainan dimulai ulang secara otomatis.
6. Klik pada jendela game untuk keluar dari aplikasi.

---

## 📁 Struktur Direktori
```
snake-game/
│
├── main.py # Entry point aplikasi, mengatur game loop dan logika utama
├── snake.py # Class Snake — logika pergerakan, penambahan badan, dan reset ular
├── food.py # Class Food — logika penempatan dan refresh posisi makanan
├── scoreboard.py # Class Score — logika perhitungan skor dan high score
├── data.txt # File penyimpanan nilai high score secara persisten
└── README.md # Dokumentasi proyek
```

---

## 🤝 Kontribusi & Lisensi

### Kontribusi
Kontribusi sangat terbuka! Jika Anda ingin berkontribusi:
1. Fork repositori ini.
2. Buat branch fitur baru (`git checkout -b fitur-baru`).
3. Commit perubahan Anda (`git commit -m 'Menambahkan fitur baru'`).
4. Push ke branch (`git push origin fitur-baru`).
5. Buka Pull Request.

Silakan laporkan bug atau ajukan permintaan fitur melalui halaman **Issues**.

### Lisensi
Proyek ini dilisensikan di bawah **MIT License**. Silakan gunakan, modifikasi, dan distribusikan sesuai kebutuhan Anda.
