import uuid

from utils.DatabaseUtil import get_db_connection

def insert_file_for_client(client_id, file_id):
    conn = get_db_connection()

    sql = "INSERT INTO client_files (id, client_id, file_id) VALUES (%s, %s, %s)"

    cursor = conn.cursor()
    cursor.execute(sql, (str(uuid.uuid4()), client_id, file_id))
    conn.commit()
    conn.close()


def delete_file_from_client(client_id, file_url):
    conn = get_db_connection()

    sql = """
        DELETE FROM client_files WHERE client_id = %s AND file_id = (
            SELECT id FROM file WHERE storage_url = %s
        )
    """

    cursor = conn.cursor()
    cursor.execute(sql, (client_id, file_url))
    conn.commit()
    conn.close()