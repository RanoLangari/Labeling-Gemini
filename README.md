# Labeling-Gemini

Proyek ini menggunakan Google Gemini AI untuk melakukan analisis sentimen otomatis pada teks berbahasa Indonesia. Sistem ini dapat mengklasifikasikan teks ke dalam kategori sentimen: Positif, Negatif, atau Netral.

## 📋 Deskripsi

Labeling-Gemini adalah aplikasi Python yang memanfaatkan API Google Gemini untuk melakukan analisis sentimen secara batch pada data teks yang disimpan dalam file CSV. Aplikasi ini dapat memproses banyak teks sekaligus dan memberikan label sentimen untuk setiap teks secara otomatis.

## ✨ Fitur

- ✅ Analisis sentimen otomatis menggunakan Google Gemini 2.5 Pro
- ✅ Pemrosesan batch data dari file CSV
- ✅ Klasifikasi teks ke dalam 3 kategori: Positif, Negatif, Netral
- ✅ Konfigurasi yang mudah melalui file environment
- ✅ Penanganan error dan fallback untuk klasifikasi
- ✅ Delay antar panggilan API untuk menghindari rate limiting

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/RanoLangari/Labeling-Gemini.git
cd Labeling-Gemini
```

### 2. Buat Virtual Environment
```bash
python -m venv env
```

### 3. Aktivasi Virtual Environment
**Windows:**
```bash
env\Scripts\activate
```

**macOS/Linux:**
```bash
source env/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Setup Environment Variables
Buat file `.env` di root directory dan tambahkan API key Gemini:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 📁 Struktur Proyek

```
Labeling-Gemini/
├── main.py              # Script utama untuk analisis sentimen
├── requirements.txt     # Dependencies Python
├── data_input.csv      # File input data (contoh)
├── data_labeled.csv    # File output hasil labeling (akan dibuat)
├── .env                # File environment variables (buat sendiri)
├── README.md           # Dokumentasi proyek
└── env/                # Virtual environment
```

## 📊 Format Data Input

File `data_input.csv` harus memiliki format sebagai berikut:

```csv
id,text
1,Saya sangat senang dengan pelayanan di toko ini
2,Produk yang saya terima rusak dan mengecewakan
3,Hari ini cuacanya biasa saja, tidak terlalu panas
```

**Kolom yang diperlukan:**
- `id`: Identifier unik untuk setiap baris
- `text`: Teks yang akan dianalisis sentimennya

## 🎯 Cara Penggunaan

### 1. Persiapkan Data Input
Pastikan file `data_input.csv` berisi data yang akan dianalisis dengan format yang benar.

### 2. Jalankan Analisis
```bash
python main.py
```

### 3. Lihat Hasil
Hasil analisis akan disimpan dalam file `data_labeled.csv` dengan kolom tambahan `sentiment`.

## ⚙️ Konfigurasi

Anda dapat mengubah konfigurasi di file `main.py`:

```python
MODEL_NAME = "gemini-2.5-pro"          # Model Gemini yang digunakan
INPUT_CSV = "data_input.csv"           # File input
OUTPUT_CSV = "data_labeled.csv"        # File output
TEXT_COLUMN = "text"                   # Nama kolom teks
SENTIMENT_COLUMN = "sentiment"         # Nama kolom hasil sentimen
DELAY_BETWEEN_CALLS = 0.5             # Delay antar panggilan API (detik)
```

## 📋 Dependencies

Proyek ini menggunakan beberapa library Python utama:

- `pandas`: Untuk manipulasi data CSV
- `google-generativeai`: SDK untuk Google Gemini AI
- `python-dotenv`: Untuk manajemen environment variables
- `numpy`: Untuk operasi array (dependency pandas)

Untuk daftar lengkap dependencies, lihat file `requirements.txt`.

## 🔑 Mendapatkan API Key Gemini

1. Kunjungi [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Login dengan akun Google Anda
3. Buat API key baru
4. Copy API key dan masukkan ke file `.env`

## 📈 Contoh Output

Setelah menjalankan script, file `data_labeled.csv` akan berisi:

```csv
id,text,sentiment
1,Saya sangat senang dengan pelayanan di toko ini,Positive
2,Produk yang saya terima rusak dan mengecewakan,Negative
3,Hari ini cuacanya biasa saja, tidak terlalu panas,Neutral
```

## 🛠️ Troubleshooting

### Error: API key tidak ditemukan
- Pastikan file `.env` ada di root directory
- Pastikan `GEMINI_API_KEY` sudah diset dengan benar

### Error: Kolom 'text' tidak ditemukan
- Pastikan file CSV memiliki kolom dengan nama `text`
- Atau ubah variable `TEXT_COLUMN` sesuai nama kolom di file Anda

### Rate Limiting
- Jika mendapat error rate limit, tingkatkan nilai `DELAY_BETWEEN_CALLS`

## 🤝 Kontribusi

1. Fork repository ini
2. Buat branch feature baru (`git checkout -b feature/amazing-feature`)
3. Commit perubahan (`git commit -m 'Add some amazing feature'`)
4. Push ke branch (`git push origin feature/amazing-feature`)
5. Buat Pull Request

## 📝 Lisensi

Proyek ini dilisensikan di bawah MIT License. Lihat file `LICENSE` untuk detail lengkap.

## 👨‍💻 Author

**RanoLangari**
- GitHub: [@RanoLangari](https://github.com/RanoLangari)

## 🙏 Acknowledgments

- Google AI untuk menyediakan Gemini API
- Tim Google AI Studio untuk tools yang mudah digunakan
- Komunitas open source Python

---

💡 **Tips**: Untuk hasil terbaik, pastikan teks input dalam bahasa Indonesia yang jelas dan tidak terlalu panjang (maksimal beberapa kalimat).
