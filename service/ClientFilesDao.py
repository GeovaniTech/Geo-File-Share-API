import uuid

from utils.DatabaseUtil import get_db_connection

def insert_file_for_client(client_id, file_id):
    conn = get_db_connection()

    sql = "INSERT INTO client_files (id, client_id, file_id) VALUES (%s, %s, %s)"

    cursor = conn.cursor()
    cursor.execute(sql, (str(uuid.uuid4()), client_id, file_id))
    conn.commit()
    conn.close()

