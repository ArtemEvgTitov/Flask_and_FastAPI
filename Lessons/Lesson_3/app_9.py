from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

# Настройка защиты от CSRF-атак
app = Flask(__name__)
app.config['SECRET_KEY'] = b'81692b0f4e8b276c12b4689455e165cc93bc486709f4c900525a7b371e23a6a3'
csrf = CSRFProtect(app)

"""
Генерация секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi'


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return "NO CSRF protection"


if __name__ == '__main__':
    app.run(debug=True)
