# file: app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Data list of dictionaries untuk to-do list kita
    todo_list = [
        {'task': 'Belajar Dasar-dasar Flask', 'done': True},
        {'task': 'Buat Aplikasi "Hello, World!"', 'done': True},
        {'task': 'Belajar HTML Template', 'done': True},
        {'task': 'Gunakan For Loops di Template', 'done': False},
        {'task': 'Push ke Github', 'done': False}
    ]

    return render_template('index.html',
                           page_title='My To-Do App',
                           todos=todo_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)