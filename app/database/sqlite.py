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

        try:
            self.execute(sql=query, params=params)
        except sqlite3.Error as error:
            return 0, {"db_error": error}

        self.conn.commit()

        return self.cursor.lastrowid, {}

    def select(self, model, where: tuple = (), params: tuple = (), columns: tuple = ()):

        query_columns = ','.join(columns if columns else model.columns)

        query = f"""
            SELECT {query_columns} FROM {model.table}  
        """

        if where and params:
            parameters = ["%s = ?" % x for x in where]
            query += f"""WHERE {' AND '.join(parameters)}"""

        try:
            result = self.execute(sql=query, params=params)
        except sqlite3.Error as error:
            return None, {"db_erro": error}

        return result

    def create_connection(self):

        conn = None

        try:
            conn = sqlite3.connect(self.db_file)
            conn.row_factory = sqlite3.Row
            conn.text_factory = str
        except Exception as e:
            print(e)

        return conn

    def close_connection(self):
        self.conn.close()
