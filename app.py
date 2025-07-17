# file: app.py
from flask import Flask, render_template

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    todo_list = [
        {'task': 'Belajar Dasar-dasar Flask', 'done': True},
        {'task': 'Buat Aplikasi "Hello, World!"', 'done': True},
        {'task': 'Belajar HTML Template', 'done': True},
        {'task': 'Gunakan For Loops di Template', 'done': True},
        {'task': 'Push ke Github', 'done': True},
        {'task': 'Buat halaman about', 'done': False}
    ]

    return render_template('index.html',
                           page_title='My To-Do App',
                           todos=todo_list)

# (KODE BARU) Route untuk halaman 'About'
@app.route('/about')
def about():
    """Menampilkan halaman 'About'."""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)