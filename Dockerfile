# Menggunakan base image resmi Python versi 3.11 yang ramping (slim)
FROM python:3.11-slim

# Menetapkan direktori kerja di dalam kontainer menjadi /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin sisa file aplikasi
COPY . .

# Beri tahu Docker bahwa container ini akan 'mendengarkan' di port 5000
EXPOSE 5000

# Perintah yang akan dijalankan saat kontainer dimulai
CMD ["python", "app.py"]
