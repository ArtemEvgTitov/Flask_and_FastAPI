from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from form import RegistrationForm
from models import db, User

app = Flask(__name__)

app.config['SECRET_KEY'] = b'81692b0f4e8b276c12b4689455e165cc93bc486709f4c900525a7b371e23a6a3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print(f'Пользователь сохранён: {name} {surname}')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)