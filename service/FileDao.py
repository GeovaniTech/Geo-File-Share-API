from datetime import datetime

from utils.DatabaseUtil import get_db_connection

CONN = None

def insert_file(file_id, filename, size, extension, storage_url):
    global CONN

    if CONN is None:
        CONN = get_db_connection()

    sql = """
        INSERT INTO file (id, filename, size, extension, storage_url, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    parameters = (file_id, filename, size, extension, storage_url, datetime.now())

    cursor = CONN.cursor()
    cursor.execute(sql, parameters)
    CONN.commit()
    CONN.close()

