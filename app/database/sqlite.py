import os
import sqlite3


class SqliteConnection:

    db_file = os.environ.get("SQLITE_FILE", "db.sqlite3")

    def __init__(self):
        pass

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def execute(self, sql: str, params: tuple = ()):

        result = self.cursor.execute(sql, params)

        return result

