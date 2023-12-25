from flask import session

from database.common import get_one_from_db, send_to_db
from utilities import password_hashing


def add_user(email, password, first_name, last_name):
    sql = "select id from public.users where email = %s"
    args = (email,)
    id = get_one_from_db(sql, args)
    if not id:
        sql = "insert into public.users (email, password, first_name, last_name) values (%s, %s, %s, %s)"
        args = (email, password_hashing.hash_password(password), first_name, last_name)
        send_to_db(sql, args)
        return True
    else:
        raise Exception("This user already exists")


def login(email, password):
    sql = "select id, first_name, last_name, password, weather_app from public.users where email = %s"
    args = (email,)

    id, first_name, last_name, encrypted_password, weather_app = get_one_from_db(
        sql, args
    )

    if password_hashing.check_password(password, encrypted_password):
        session["id"] = id
        session["first_name"] = first_name
        session["last_name"] = last_name
        session["email"] = email
        session["weather_app"] = weather_app

        return True
    else:
        raise Exception("Cannot log in. Please check email and password.")
