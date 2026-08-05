# 🐍 Neon Snake - Pygame Edition

> Game Snake klasik yang dibuat ulang menggunakan **Pygame** dengan tampilan modern, efek visual menarik, dan fitur gameplay yang diperkaya.

---

## 1. Deskripsi Singkat Project

**Neon Snake** adalah game arcade klasik berbasis Python yang mengadaptasi konsep permainan ular legendaris dengan sentuhan visual modern. Dibangun menggunakan library **Pygame**, game ini menawarkan pengalaman bermain yang responsif dengan tampilan **tema gelap neon**, efek partikel, sistem level, dan power-up spesial.

Project ini merupakan hasil konversi dari library **Turtle Graphics** ke **Pygame**, dengan penambahan berbagai fitur modern untuk meningkatkan kualitas gameplay dan estetika visual.

---

## 2. Fitur Project

| Fitur | Penjelasan |
|-------|------------|
| 🎮 **Kontrol Responsif** | Gerakan ular menggunakan Arrow Keys atau WASD dengan deteksi arah balik yang otomatis dicegah |
| 🟢 **Makanan Normal** | Makanan merah coral standar, bernilai +1 poin |
| 🟡 **Makanan Emas (Power-up)** | Muncul dengan probabilitas 10%, bernilai +5 poin dengan efek ledakan partikel dan screen shake |
| 🔵 **Makanan Biru (Slow Motion)** | Muncul dengan probabilitas 10%, bernilai +2 poin dan mengaktifkan efek gerak lambat selama 5 detik |
| ✨ **Efek Partikel** | Ledakan partikel saat ular memakan makanan dengan warna yang sesuai tipe makanan |
| 📳 **Screen Shake** | Efek getaran layar saat game over atau memakan makanan emas |
| 🌟 **Neon Glow Effect** | Efek cahaya pada kepala ular dan makanan untuk tampilan futuristik |
| 👁️ **Mata Ular Animasi** | Mata pada kepala ular yang mengikuti arah gerakan secara real-time |
| 📈 **Sistem Level** | Kecepatan ular bertambah otomatis setiap kelipatan 5 poin |
| 🏆 **High Score Persistence** | Skor tertinggi tersimpan secara otomatis ke file `data.txt` |
| 🖥️ **Start Menu Interaktif** | Menu utama dengan animasi partikel background, tombol hover effect, dan shortcut keyboard |
| ⏸️ **Pause ke Menu** | Tekan ESC saat bermain untuk kembali ke menu utama tanpa menutup game |
| 🎨 **Grid Background** | Latar belakang grid transparan dengan tema warna gelap neon |

---

## 3. Tech Stack

Berikut adalah teknologi dan library yang harus dipersiapkan untuk menjalankan project ini:

| Komponen | Versi Minimum | Keterangan |
|----------|---------------|------------|
| **Python** | 3.8+ | Bahasa pemrograman utama |
| **Pygame** | 2.1.0+ | Library untuk grafis, audio, dan event handling |
| **Math** | Built-in | Modul bawaan Python untuk fungsi trigonometri |
| **Random** | Built-in | Modul bawaan Python untuk randomisasi posisi makanan |
| **OS** | Built-in | Modul bawaan Python untuk operasi file (high score) |

### Instalasi Dependensi

```bash
# Pastikan Python sudah terinstall
python --version

# Install Pygame
pip install pygame
```

---

## 4. Cara Menjalankan Project

### Langkah 1: Clone Repository

```bash
# Clone repository ke lokal
git clone https://github.com/username/neon-snake-pygame.git

# Masuk ke direktori project
cd neon-snake-pygame
```

### Langkah 2: Install Dependensi

```bash
# Install library Pygame
pip install pygame
```

### Langkah 3: Jalankan Game

```bash
# Jalankan file utama
python main.py
```

### Kontrol Bermain

| Tombol | Fungsi |
|--------|--------|
| `↑` / `W` | Gerak ke atas |
| `↓` / `S` | Gerak ke bawah |
| `←` / `A` | Gerak ke kiri |
| `→` / `D` | Gerak ke kanan |
| `ENTER` / `SPACE` | Mulai game dari menu / Restart saat Game Over |
| `ESC` | Kembali ke menu utama / Keluar dari menu |

---

## 5. Struktur Direktori

```
neon-snake-pygame/
│
├── main.py              # Entry point game, mengatur game loop dan state
├── menu.py              # Start menu dengan animasi dan tombol interaktif
├── snake.py             # Logika ular: gerakan, pertumbuhan, collision detection
├── food.py              # Logika makanan: spawn, tipe makanan, animasi pulse
├── scoreboard.py        # Manajemen skor, high score, dan level progression
├── particle.py          # Sistem efek partikel dan screen shake
├── settings.py          # Konfigurasi warna, ukuran, font, dan konstanta game
├── data.txt             # File penyimpanan high score (auto-generated)
│
└── README.md            # Dokumentasi project (file ini)
```

### Penjelasan File

- **`main.py`** — Menginisialisasi Pygame, menangani game loop utama, event handling, dan mengoordinasikan semua komponen game (snake, food, scoreboard, particle).
- **`menu.py`** — Menampilkan layar start menu sebelum game dimulai. Berisi animasi partikel background, judul dengan efek glow, tombol interaktif, dan shortcut keyboard.
- **`snake.py`** — Mengatur seluruh logika ular: inisialisasi tubuh, pergerakan segmen, deteksi tabrakan (dinding & ekor sendiri), pertumbuhan, dan rendering visual dengan efek gradient.
- **`food.py`** — Mengatur spawn makanan acak, 3 tipe makanan (normal, gold, slow), animasi pulse (membesar-mengecil), dan pemberian skor sesuai tipe.
- **`scoreboard.py`** — Mengelola skor saat ini, high score (read/write ke `data.txt`), penghitungan level, dan tampilan panel skor serta layar Game Over.
- **`particle.py`** — Sistem partikel untuk efek ledakan saat memakan makanan. Juga mengatur efek screen shake saat terjadi event penting.
- **`settings.py`** — Pusat konfigurasi: ukuran layar, ukuran grid, warna tema neon, font, dan kecepatan dasar game.
- **`data.txt`** — File teks sederhana yang menyimpan nilai high score tertinggi. File ini dibuat otomatis saat pertama kali bermain.

---

## 📝 Catatan Tambahan

- Game menggunakan resolusi **600×650 pixel** (600×600 area permainan + 50 pixel panel skor di atas).
- Grid permainan berukuran **30×30 sel** dengan ukuran sel 20×20 pixel.
- File `data.txt` akan dibuat secara otomatis di direktori root project saat pertama kali game dijalankan dan skor tercapai.
- Tidak diperlukan asset eksternal (gambar/audio) karena seluruh visual dibuat secara procedural menggunakan Pygame.

---

<p align="center">Dibuat dengan ❤️ menggunakan Python & Pygame</p>
