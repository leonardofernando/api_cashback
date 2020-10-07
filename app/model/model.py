from app import SqliteConnection


class Model:

    _table = ""
    _pk = ""

    def _select(self):

        with SqliteConnection() as database:
            pass

    def _update(self):

        with SqliteConnection() as database:
            pass

    def _delete(self):

        with SqliteConnection() as database:
            pass

    def _insert(self, table: str, columns: tuple, params: tuple):

        with SqliteConnection() as database:
            parameters = ",".join(["?" for x in params])
            query = f"INSERT INTO {table} ({columns}) VALUES ({parameters})"

            database.execute(sql=query, params=params)

    def save(self):

        self._insert(self._table)

    def _set_insert(self):


