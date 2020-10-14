from typing import Tuple

from app.model.purchase import Purchase
from app.database.sqlite import SqliteConnection
from .cashback_controller import CashbackController


class PurchaseController:

    FREE_CPFS = ["153.509.460-56"]

    @staticmethod
    def purchase_register(
            code: int, value: int, date: str, cpf: str
    ) -> Tuple[bool, dict]:
        """
        Função para cadastrar compra.

        :param int code: Código da compra
        :param int value: Valor da compra
        :param str date: Data da compra
        :param str cpf: Cpf do revendedor
        :return bool, dict: Status da operação e mensagem
        """

        status = "Em validação"
        if cpf in PurchaseController.FREE_CPFS:
            status = "Aprovado"

        with SqliteConnection() as database:

            params = (code, value, date, cpf, status)
            insert_id, db_message = database.insert(table=Purchase.table, columns=Purchase.columns, params=params)

            if not insert_id:
                return False, db_message

        return True, {"mensagem": "A compra foi inserida com sucesso!"}

    @staticmethod
    def get_purchases() -> list:
        """
        Função para resgatar lista de compras cadastradas.

        :return list: Lista de compras
        """

        purchases_list = []

        with SqliteConnection() as database:

            result = database.select(model=Purchase)

            purchases_data = result.fetchall()

            for row in purchases_data:

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
