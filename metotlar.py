from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "vkmyo"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("index.html")

# login page
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        #pwd = request.form["pwd"]
        session.permanent = True
        session["user"] = user
        flash("Oturum Actiniz", "info")
        # if(pwd == "1234"):
        return redirect(url_for("user"))
        # else:
        #    return redirect(url_for("login"))
    else:
        if "user" in session:
            user = session["user"]
            flash("Zaten oturum Acik", "info")
        return render_template("login.html")

# user page
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("Oturum Acmamissiniz")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        flash("Oturum sonlandirildi!", "info")
        session.pop("user")  # oturum sonlandirilir
        return redirect(url_for("login"))
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
