from functools import wraps

from flask import session, redirect, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_id" in session:
            # User is logged in, proceed with the original function
            return func(*args, **kwargs)
        else:
            # User is not logged in, redirect to the login page
            return redirect(url_for("login"))

    return wrapper


def weather_app_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("weather_app"):
            return func(*args, **kwargs)
        else:
            print("You do not have access to this application")
            return redirect(url_for("home"))

    return wrapper


def dinner_ideas_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("dinner_ideas"):
            return func(*args, **kwargs)
        else:
            print("You do not have access to this application")
            return redirect(url_for("home"))

    return wrapper
