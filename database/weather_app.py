import datetime

from database import common

db_name = "d296mehvjdhrbl"


def get_from_db(query, args):
    return common.get_from_db(db_name, query, args)


def get_one_from_db(query, args):
    return common.get_one_from_db(db_name, query, args)


def send_to_db(query, args):
    return common.send_to_db(db_name, query, args)


def add_weather_entry(weather, wind, temperature):
    td = datetime.date.today()

    sql = "select id from weather_app.entries where date = %s"
    args = (td,)
    id = get_one_from_db(sql, args)
    if not id:
        sql = "insert into weather_app.entries (temperature, wind, weather, date) values (%s, %s, %s, %s)"
        args = (temperature, wind, weather, td)
        send_to_db(sql, args)
    else:
        sql = "update weather_app.entries set temperature = %s, wind = %s, weather = %s where id = %s"
        args = (temperature, wind, weather, id)
        send_to_db(sql, args)
