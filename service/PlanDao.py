import json
from datetime import datetime

from psycopg2.extras import RealDictCursor

from utils.DatabaseUtil import get_db_connection


def upsert_plan(plan_id, title, parameters, price, currency, is_active):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM plan WHERE type = %s", (plan_id,))
    plan_exists = cursor.fetchone()

    if plan_exists is not None:
        operation = "UPDATE"
        cursor.execute(
            """
            UPDATE plan
            SET title = %s, parameters = %s, price = %s, currency = %s, is_active = %s, updated_at = %s
            WHERE type = %s
            """,
            (title, json.dumps(parameters), price, currency, is_active, datetime.now(), plan_id)
        )
    else:
        operation = "CREATE"
        cursor.execute(
            """
            INSERT INTO plan (type, title, parameters, price, currency, is_active, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (plan_id, title, json.dumps(parameters), price, currency, is_active, datetime.now(), datetime.now())
        )

    conn.commit()
    conn.close()

    return operation


def find_plan(plan_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM plan WHERE type = %s", (plan_id,))
    plan = cursor.fetchone()

    if plan is None:
        return None
    else :
        return json.dumps(plan, default=str)

