import os

import waitress as waitress
from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_session import Session

import database.users as db_users
from blueprints import api as bp_api
from blueprints import weather_app as bp_weather_app
from utilities.login_required import login_required

app = Flask(__name__)
app.config["SESSION_TYPE"] = "memcached"
app.config["SECRET_KEY"] = "super secret key"
sess = Session()
app.register_blueprint(bp_api.api)
app.register_blueprint(bp_weather_app.weather_app)


@app.route("/")
@login_required
def index():
    return redirect(url_for("home"))


@app.route("/home")
@login_required
def home():
    links = [{"name": "API", "link": url_for("api.index")}]

    if session["weather_app"]:
        links.append({"name": "Weather App", "link": url_for("weather_app.home")})

    return render_template("index.html", links=links)


@app.route("/login", methods=("POST", "GET"))
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if db_users.login(email, password):
            flash(("Logged in successfully!", "success"))
            return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            if db_users.add_user(email, password, first_name, last_name):
                flash(("User added successfully", "success"))
                return redirect(url_for("login"))
        except Exception as E:
            flash((E, "danger"))
            return redirect(url_for("register"))

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    flash(("Logged out successfully", "success"))
    return redirect(url_for("login"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    waitress.serve(app, host="0.0.0.0", port=port)
