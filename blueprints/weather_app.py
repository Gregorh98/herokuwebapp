from flask import Blueprint, url_for, redirect, flash
from flask import render_template, request

import database.weather_app as db
from utilities.login_required import weather_app_required, login_required

weather_app = Blueprint("weather_app", __name__)
proj_name = "weather_app"


@weather_app.route("/weather_app", methods=["GET", "POST"])
@weather_app_required
@login_required
def home():
    if request.method == "POST":
        weather = request.form.get("weather")
        wind = request.form.get("wind")
        temperature = request.form.get("temperature")
        try:
            result = db.add_weather_entry(weather, wind, temperature)
            flash((f"Successfully {result}", "success"))
        except Exception as E:
            flash((f"Unsuccessful. Error: {E}", "danger"))
        return redirect(url_for(f"{proj_name}.home"))

    return render_template(f"{proj_name}/weather_app.html")


@weather_app.route("/weather_app/history", methods=["GET", "POST"])
@weather_app_required
@login_required
def history():
    return render_template(f"{proj_name}/history.html")
