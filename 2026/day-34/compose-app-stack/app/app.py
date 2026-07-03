import os

import psycopg2
import redis
from flask import Flask, jsonify


app = Flask(__name__)


def db_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


def redis_client():
    return redis.Redis(host=os.environ["REDIS_HOST"], port=6379, decode_responses=True)


@app.get("/")
def index():
    cache = redis_client()
    visits = cache.incr("visits")

    with db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()[0]

    return jsonify(
        message="Hello from the Day 34 Compose stack",
        visits=visits,
        database=db_version,
    )


@app.get("/health")
def health():
    with db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            cur.fetchone()

    redis_client().ping()
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

