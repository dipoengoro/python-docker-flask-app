# file: app.py
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Menampilkan halaman utama menggunakan template HTML."""

    # Menyiapkan data yang akan dikirim ke template
    waktu_sekarang = datetime.now().strftime("%H:%M:%S")

    # Me-render file 'index.html' dan mengirimkan variabel ke dalamnya
    return render_template('index.html',
                           page_title='My First Web App',
                           main_greeting='Halo dari Template!',
                           current_time=waktu_sekarang)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)