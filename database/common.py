import os
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Database connection parameters
db_url = os.getenv("DB_URL")


def get_conn():
    result = urlparse(db_url)

    return psycopg2.connect(
        dbname=result.path[1:],  # The path includes a leading '/', so we remove it
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port,
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
