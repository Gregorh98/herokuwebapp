import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Database connection parameters
user = "uobseijcswqdyl"
password = os.getenv("DB_PASS")
host = "ec2-54-155-46-64.eu-west-1.compute.amazonaws.com"
port = "5432"


def get_conn(dbname):
    return psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )


def get_from_db(db_name, query, args=()):
    with get_conn(db_name) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchall()
            return result


def get_one_from_db(db_name, query, args=()):
    with get_conn(db_name) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchone()
            return result


def send_to_db(db_name, query, args=()):
    with get_conn(db_name) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
            conn.commit()
