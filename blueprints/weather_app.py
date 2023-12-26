import requests
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
            db.add_weather_entry(weather, wind, temperature)
            flash("Successfully added weather reading")
        except Exception as E:
            flash(f"Unsuccessful. Error: {E}")
        return redirect(url_for(f"{proj_name}.home"))

    return render_template(f"{proj_name}/weather_app.html", current_temp = int(requests.get("https://api.open-meteo.com/v1/forecast?latitude=55.85&longitude=-3.16&current=temperature_2m").json()["current"]["temperature_2m"]))
