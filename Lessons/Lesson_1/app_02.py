from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, незнакомец!'


@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'


@app.route('/Артём/')
def artem():
    return 'Привет, Артём!'


@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
 return 'Привет, Феодор!'


if __name__ == '__main__':
    app.run()