from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/<name>")
def user(name):
	return f"Merhaba {name}!"

@app.route("/")
def home():
	return "Vezirkopru MYO Bilgisayar <h2> Hosgeldin </h2>" 

@app.route("/admin")
def admin():
	return redirect(url_for("home"))


if __name__ == "__main__":
	app.run()

