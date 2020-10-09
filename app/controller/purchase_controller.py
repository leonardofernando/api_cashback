from typing import Tuple

from app.model.purchase import Purchase
from app.database.sqlite import SqliteConnection
from app.validator.fields_validator import FieldsValidator
from .cashback_controller import CashbackController


class PurchaseController:

    FREE_CPFS = ["153.509.460-56"]

    @staticmethod
    def purchase_register(
            code: int, value: str, date: str, cpf: str
    ) -> Tuple[bool, dict]:

        status = "Em validação"
        if cpf in PurchaseController.FREE_CPFS:
            status = "Aprovado"

        with SqliteConnection() as database:

            params = (code, value, date, cpf, status)
            insert_id, db_message = database.insert(table=Purchase.table, columns=Purchase.colums, params=params)

            if not insert_id:
                return False, db_message

        return True, {"mensagem": "A compra foi inserida com sucesso!"}

    @staticmethod
    def get_purchases():

        purchases_list = []

        with SqliteConnection() as database:

            result = database.select(table=Purchase.table, columns=Purchase.colums)

            for row in result.fetchall():

                cb_percent, cb_description = CashbackController.get_cashback_percent(value=row["value"])

                purchase = {
                    "codigo": row["code"],
                    "valor": row["value"],
                    "data": row["date"],
                    "cpf": row["cpf"],
                    "status": row["status"],
                    "cashback": {
                        "porcentagem": cb_description,
                        "valor": cb_percent * row["value"],
                    },
                }

                purchases_list.append(purchase)

        return purchases_list
