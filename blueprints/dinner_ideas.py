from flask import Blueprint, request
from flask import render_template

from utilities.login_required import dinner_ideas_required, login_required
from database.dinner_ideas import get_random_dinner_ideas

dinner_ideas = Blueprint("dinner_ideas", __name__)
proj_name = "dinner_ideas"

@dinner_ideas.route(f"/{proj_name}", methods=["GET", "POST"])
@dinner_ideas_required
@login_required
def home():
    food_ideas = []

    if request.method == "POST":
        meal_count_return = request.form.get("meal_count")
        meal_count = int(meal_count_return) if (meal_count_return != '' and meal_count_return is not None) else 7

        food_ideas = get_random_dinner_ideas(meal_count)

    return render_template(f"{proj_name}/dinner_ideas.html", food_ideas=food_ideas, page_title="Dinner Ideas")