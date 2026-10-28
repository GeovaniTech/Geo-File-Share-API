import uuid
from datetime import datetime
from random import randint

from utils.DatabaseUtil import get_db_connection


def create_room(client_id):
    while True:
        room_id = str(randint(100000, 999999))

        if exists_room(room_id):
            continue
        else:
            break

    conn = get_db_connection()

    sql = """
        INSERT INTO room (id, created_at, client_id)
        VALUES (%s, %s, %s)
    """

    parameters = (room_id, datetime.now(), client_id)

    cursor = conn.cursor()
    cursor.execute(sql, parameters)
    conn.commit()
    conn.close()

    return room_id


def exists_room(room_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
        SELECT * FROM room WHERE id = %s
    """

    parameters = (room_id,)
    cursor.execute(sql, parameters)

    room = cursor.fetchone()

    conn.close()

    return room is not None


def add_files_to_room(room_id, files):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO room_files (id, room_id, file_id)
        VALUES (%s, %s, %s)
    """


    for file_id in files:
         parameters = (str(uuid.uuid4()), room_id, file_id)
         cursor.execute(sql, parameters)

    conn.commit()
    conn.close()

