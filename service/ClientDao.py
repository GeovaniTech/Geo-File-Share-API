import datetime

from utils.DatabaseUtil import get_db_connection

def insert_client(client_id, plan_id):
    conn = get_db_connection()

    sql = "INSERT INTO Client (id, plan_id, created_at, updated_at) VALUES (%s, %s, %s, %s)"

    cursor = conn.cursor()
    cursor.execute(sql, (client_id, plan_id, datetime.datetime.now(), datetime.datetime.now()))
    conn.commit()
    conn.close()


def update_client_plan(client_id, plan_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "UPDATE Client SET plan_id = %s, updated_at = %s WHERE id = %s"

    cursor.execute(sql, (plan_id, datetime.datetime.now(), client_id))
    conn.commit()
    conn.close()

