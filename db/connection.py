import os
import sqlite3


def get_connection():
    db_path = os.getenv("DB_PATH", "network_assets.db")
    return sqlite3.connect(db_path)
