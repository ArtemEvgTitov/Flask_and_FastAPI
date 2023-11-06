from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        response = make_response(redirect(url_for("welcome")))
        response.set_cookie("user_data", f"{name}:{email}", max_age=3600)
        return response

    return render_template("index.html")


@app.route("/welcome")
def welcome():
    user_data = request.cookies.get("user_data")
    if user_data:
        name, email = user_data.split(":")
        return render_template("welcome.html", name=name, email=email)
    else:
        return redirect(url_for("index"))


@app.route("/logout")
def logout():
    response = make_response(redirect(url_for("index")))
    response.set_cookie("user_data", "", expires=0)
    return response


if __name__ == "__main__":
    app.run(debug=True)