import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Database connection parameters
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = "5432"


def get_conn():
    return psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )


def get_from_db(query, args=()):
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchall()
            return result


def get_one_from_db(query, args=()):
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchone()
            return result


def send_to_db(query, args=()):
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
            conn.commit()
