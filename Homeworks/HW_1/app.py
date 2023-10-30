from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def base():
    context = {
        'title': 'Супер-магазин'
    }
    return render_template("base.html", **context)


@app.route("/products.html/")
def clothes():
    title = 'Товары'
    all_clothes = [
        {'product': 'Куртка', 'size': '42-50', 'info': 'Описание куртки',
         'price': '100$'},
        {'product': 'Джинсы', 'size': '42-50', 'info': 'Описание джинс', 'price': '50$'},
        {'product': 'Свитер', 'size': '42-50', 'info': 'Описание свитера', 'price': '30$'},
        {'product': 'Кроссовки', 'size': '40-45', 'info': 'Описание кроссовок', 'price': '40$'},
        {'product': 'Ботинки', 'size': '40-45', 'info': 'Описание ботинок', 'price': '70$'},
        {'product': 'Перчатки', 'size': '40-50', 'info': 'Описание перчаток', 'price': '20$'},
    ]
    return render_template("products.html", all_clothes=all_clothes, title=title)


@app.route("/contacts.html/")
def shoes():
    title = 'Контакты'
    return render_template("contacts.html", title=title)


if __name__ == '__main__':
    app.run(debug=True)
