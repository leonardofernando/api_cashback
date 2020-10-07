from typing import Tuple

from app.model.dealer import Dealer
from app.database.sqlite import SqliteConnection
from app.validator.fields_validator import FieldsValidator


class DealerController:

    @staticmethod
    def dealer_register(name: str, cpf: str, email: str, password: str) -> Tuple[bool, int]:

        if not FieldsValidator.valid_cpf(cpf):
            return False, 0

        if not FieldsValidator.valid_email(email):
            return False, 0

        with SqliteConnection() as database:

            params = (name, cpf, email, password)
            insert_id = database.insert(table=Dealer.table, columns=Dealer.colums, params=params)

            if not insert_id:
                return False, 0

        return True, insert_id

    @staticmethod
    def dealer_login(email: str, password: str) -> bool:

        with SqliteConnection() as database:

            columns = ('email', 'password')
            params = (email, password)

            result = database.select(table=Dealer.table, columns=columns, params=params)

            dealer = result.fetchone()

            if not dealer:
                return False

        return True
