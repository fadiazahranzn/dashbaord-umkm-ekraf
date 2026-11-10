# UMKM Siap AI

Dashboard interaktif: seberapa siap UMKM Indonesia memanfaatkan AI, dan di mana kesenjangannya paling besar?

Final Project Track Data Analytics, Creative Technology Future Talents 2026. Dibuat oleh Fadia Zahran Zain.

## Isi dashboard

| Tab | Fungsi |
|-----|--------|
| Kondisi UMKM | KPI nasional, peta kesiapan 38 provinsi (kuadran Siap / Potensial / Bergerak / Tertinggal), tren, distribusi antar pulau, hambatan, gap kenal vs pakai AI, key insights. Ada filter wilayah, kuadran, rentang akses internet, dan warna peta. |
| Cek Kesiapan AI | Kuis 8 pertanyaan dengan skor langsung dan 3 langkah berikutnya. |
| Rekomendasi AI | Peta jalan 4 minggu per jenis usaha, dengan checklist yang tersimpan di browser. |
| Kalkulator Hemat | Perkiraan jam kerja per bulan yang bisa dihemat dengan AI. |

Tersedia mode gelap dan sidebar yang bisa dilipat. Tampilan responsif untuk HP.

## Cara membuka

Buka `index.html` di browser (klik dua kali). Tidak perlu server atau instalasi.
Butuh internet karena Chart.js dan font Poppins dimuat dari CDN.

## Struktur folder

```
index.html     dashboard (satu file: HTML, CSS, JS, data)
analisis.py    skrip pandas: menggabungkan data BPS, menghitung per 1.000 penduduk,
               korelasi, median, dan kuadran. Hasil: data/analisis_provinsi_2024.csv, data/derived.json
data/          data mentah dan hasil olahan (CSV/JSON), lengkap dengan kolom sumber
archive/       versi desain editorial lama (cadangan)
```

Menjalankan ulang analisis: `python analisis.py data` (butuh pandas dan numpy).
Hasil `derived.json` lalu dipindahkan ke objek `DATA` di `index.html`.

## Metodologi singkat

- Usaha e-commerce per 1.000 penduduk = jumlah usaha e-commerce 2024 (BPS) / proyeksi penduduk 2024 x 1.000.
- Kuadran dibagi dengan median dua indikator: akses internet dan usaha e-commerce per 1.000 penduduk.
- Korelasi internet vs usaha per 1.000 penduduk: Spearman rho = 0,76; Pearson r = 0,51.
- Pertumbuhan 2020 ke 2024 hanya ditampilkan per pulau, karena definisi data berubah antar tahun survei BPS.

## Sumber data

Daftar lengkap ada di bagian "Sumber data" di kaki dashboard. Garis besarnya:
BPS Statistik E-Commerce (2021 sampai 2024), BPS tabel penduduk dan akses internet per provinsi,
serta pemberitaan survei adopsi AI (Google, UKM Indonesia x ICCI, pernyataan Menteri UMKM).
Peta batas provinsi memakai "Indonesia GeoJSON & TopoJSON Maps (38 Provinces)" (CC BY 4.0), disederhanakan untuk tampilan.

## Batasan yang perlu diketahui

- Angka adopsi AI (76%, 67,65%, 14,5%, dan lebih dari 90%) berasal dari survei dengan metode berbeda. Baca sebagai arah, bukan satu seri data yang sebanding.
- Langkah di tab Rekomendasi, urutan mingguannya, dan angka default Kalkulator disusun penulis sebagai saran praktis. Itu bukan hasil olah data BPS.
- Skor dan batas level kuis adalah skema penulis, bukan standar resmi.
- Klaim "ada versi gratis" pada tools AI perlu dicek ulang karena paket gratis sering berubah.
- Pulau-pulau kecil tidak tampil di peta karena batas wilayah disederhanakan.

## Membagikan lewat GitHub Pages (opsional)

1. Buat repo baru di GitHub lalu unggah isi folder ini (minimal `index.html`).
2. Settings, Pages, Source: `Deploy from a branch`, pilih `main` dan folder `/ (root)`.
3. Dalam beberapa menit dashboard terbuka di `https://<username>.github.io/<nama-repo>/`.
