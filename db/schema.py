from .connection import get_connection


def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.executescript(open("schema.sql").read())

    conn.commit()
    conn.close()
