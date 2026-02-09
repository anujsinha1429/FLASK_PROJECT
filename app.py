from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# app.secret_key = "secret123"   # session ke liye
import os
app.secret_key = os.getenv("SECRET_KEY", "dev_key")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # simple authentication check
        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/welcome")
def welcome():
    if "user" in session:
        return render_template("welcome.html", user=session["user"])
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))






if __name__ == "__main__":
    app.run(debug=True)