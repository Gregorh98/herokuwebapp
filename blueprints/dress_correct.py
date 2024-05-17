from flask import Blueprint
from flask import render_template

from utilities.login_required import login_required

dress_correct = Blueprint("dress_correct", __name__)
proj_name = "dress_correct"


@dress_correct.route("/dress_correct", methods=["GET", "POST"])
@login_required
def home():
    return render_template(f"{proj_name}/dress_correct.html")
