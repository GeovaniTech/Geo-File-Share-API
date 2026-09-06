from datetime import datetime

from utils.DatabaseUtil import get_db_connection

def insert_file(file_id, filename, size, extension, storage_url):
    conn = get_db_connection()

    sql = """
        INSERT INTO file (id, filename, size, extension, storage_url, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    parameters = (file_id, filename, size, extension, storage_url, datetime.now())

    cursor = conn.cursor()
    cursor.execute(sql, parameters)
    conn.commit()
    conn.close()

