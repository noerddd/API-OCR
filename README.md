# OTOBOOK

OTOBOOK adalah aplikasi untuk mengelola metadata buku menggunakan OCR dan AI. Aplikasi ini dibangun menggunakan Raspberry Pi 4, webcam, dan beberapa pustaka Python. Proyek ini menggunakan PostgreSQL sebagai database.

## Prasyarat

Pastikan Anda memiliki:

- Raspberry Pi 4 (atau komputer dengan Windows 10)
- Webcam
- Python 3.x
- PostgreSQL
- OpenAI API Key

## Instalasi

### Instalasi PostgreSQL

1. Unduh dan instal PostgreSQL dari [postgresql.org](https://www.postgresql.org/download/windows/).
2. Selama instalasi, ingat username dan password yang Anda buat untuk user `postgres`.
3. Setelah instalasi, buka aplikasi pgAdmin dan buat database `otobook`.

### Instalasi Pustaka Python

Buka Command Prompt atau PowerShell dan jalankan perintah berikut untuk menginstal pustaka yang diperlukan:

```bash
pip install flask psycopg2-binary pytesseract opencv-python-headless

```
# Menjalankan API
Jalankan aplikasi dengan perintah berikut:

bash
Salin kode
python app.py
Aplikasi akan berjalan di http://0.0.0.0:5000. Anda bisa mengaksesnya melalui browser di Windows 10 atau perangkat lain yang terhubung ke jaringan yang sama.

Catatan
Gantilah DATABASE_URL di database.py dengan kredensial PostgreSQL Anda.
Pastikan API_KEY di gpt3.py sudah diisi dengan kunci API dari OpenAI Anda.# API-OCR
# Otobook-Api
