from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_1 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'81692b0f4e8b276c12b4689455e165cc93bc486709f4c900525a7b371e23a6a3'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
