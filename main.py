import os

import waitress as waitress
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
   links = [
      {"name":"Index", "link":url_for("index")},
      {"name": "Index", "link": url_for("index")},
      {"name": "Index", "link": url_for("index")}
   ]

   return render_template("index.html", links=links)


if __name__ == '__main__':
   port = int(os.environ.get("PORT", 8080))
   waitress.serve(app, host="0.0.0.0", port=port)