import datetime

from flask import session

from database.common import get_one_from_db, send_to_db


def add_weather_entry(weather, wind, temperature):
    td = datetime.date.today()
    user_id = session["user_id"]

    sql = "select id from weather_app.entries where date = %s and user_id = %s"
    args = (td, user_id)
    id = get_one_from_db(sql, args)
    if not id:
        sql = "insert into weather_app.entries (temperature, wind, weather, date, user_id) values (%s, %s, %s, %s, %s)"
        args = (temperature, wind, weather, td, user_id)
        send_to_db(sql, args)
        return "added new weather entry"
    else:
        sql = "update weather_app.entries set temperature = %s, wind = %s, weather = %s where id = %s"
        args = (temperature, wind, weather, id)
        send_to_db(sql, args)
        return "updated existing weather entry"
