from distutils.log import debug
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ders")
def ders():
    return render_template("ders.html")


@app.route("/ogrenci")
def ogrenci():
    return render_template("ogrenci.html")


if __name__ == "__main__":
    app.run(debug=True)
