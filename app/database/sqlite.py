import os
import sqlite3


class SqliteConnection:

    db_file = os.environ.get("SQLITE_FILE", r"/home/leonardo/github/api-cashback/db.sqlite3")

    def __init__(self):
        self.conn = self.create_connection()

    def __enter__(self):
        self.conn = self.conn if self.conn else self.create_connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

    def execute(self, sql: str, params: tuple = ()):

        result = self.cursor.execute(sql, params)

        return result

    def insert(self, table: str, columns: tuple, params: tuple):

        parameters = ["?"] * len(params)
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(parameters)})"

        self.execute(sql=query, params=params)
        self.conn.commit()

        return self.cursor.lastrowid

    def select(self, table: str, columns: tuple, params: tuple = ()):

        query = f"""
            SELECT {', '.join(columns)} FROM {table}  
        """

        if params:
            parameters = ["%s = ?" % x for x in columns]
            query += f"""WHERE {' AND '.join(parameters)}"""

        result = self.execute(sql=query, params=params)
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
