import os

import waitress as waitress
from flask import Flask, render_template, url_for
from flask_session import Session

from blueprints import api as bp_api
from blueprints import weather_app as bp_weather_app

app = Flask(__name__)
app.config["SESSION_TYPE"] = "memcached"
app.config["SECRET_KEY"] = "super secret key"
sess = Session()
app.register_blueprint(bp_api.api)
app.register_blueprint(bp_weather_app.weather_app)


@app.route("/")
def index():
    links = [
        {"name": "API", "link": url_for("api.index")},
        {"name": "Weather App", "link": url_for("weather_app.home")},
    ]

    return render_template("index.html", links=links)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    waitress.serve(app, host="0.0.0.0", port=port)
