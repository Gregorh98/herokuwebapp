from flask import Blueprint
from flask import render_template, request

weather_app = Blueprint("weather_app", __name__)


@weather_app.route("/weather_app", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        weather = request.form.get("weather")
        wind = request.form.get("wind")
        temperature = request.form.get("temperature")
        return f"{weather}, {wind}, {temperature}"

    return render_template("home.html")
