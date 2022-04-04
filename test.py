from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<name>")
def user(name):
    return f"Selam {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin User!"))


@app.route("/")
def home():
    return "Vezirkopru MYO Bilgisayar <h2> Hosgeldin </h2>"


if __name__ == "__main__":
    app.run()
