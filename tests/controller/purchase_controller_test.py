import unittest
from app.controller.purchase_controller import PurchaseController
from app.database.sqlite import SqliteConnection


class PurchaseControllerTest(unittest.TestCase):

    def test_get_purchases_success(self):
        """
        Testa se lista de compras e retornada coretamente.

        :return:
        """

        purchase_list = PurchaseController.get_purchases()

        self.assertIsInstance(purchase_list, list)

    def test_purchase_register_success(self):
        """
        Testa se registro de compra é realizado com sucesso.

        :return:
        """

        code = 12345
        value = 1485
        date = "26/02/2020"
        cpf = "555.555.555-55"

        result, message = PurchaseController.purchase_register(code=code, value=value, date=date, cpf=cpf)

        self.assertTrue(result)
        self.assertIsInstance(message, dict)
