from flask import Blueprint
from flask import render_template

from utilities.login_required import login_required

inktrigue = Blueprint("inktrigue", __name__)
proj_name = "inktrigue"


@inktrigue.route("/inktrigue", methods=["GET", "POST"])
@login_required
def home():
    return render_template(f"{proj_name}/inktrigue.html")
