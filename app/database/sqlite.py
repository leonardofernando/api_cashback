import os
import sqlite3


class SqliteConnection:

    db_file = os.environ.get("SQLITE_FILE", "db.sqlite3")

    def __init__(self):
        self.conn = self.create_connection()

    def __enter__(self):
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

    def execute(self, sql: str, params: tuple = ()):

        result = self.cursor.execute(sql, params)

        return result

    def create_connection(self):

        conn = None

        try:
            conn = sqlite3.connect(self.db_file)
        except Exception as e:
            print(e)

        return conn

    def close_connection(self):
        self.conn.close()
