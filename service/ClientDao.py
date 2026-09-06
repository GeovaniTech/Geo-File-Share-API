from utils.DatabaseUtil import get_db_connection

def insert_client(client_id):
    conn = get_db_connection()

    sql = "INSERT INTO Client (id) VALUES (%s)"

    cursor = conn.cursor()
    cursor.execute(sql, (client_id,))
    conn.commit()
    conn.close()

