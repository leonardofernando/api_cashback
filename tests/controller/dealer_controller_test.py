import unittest
from app.controller.dealer_controller import DealerController


class DealerControllerTest(unittest.TestCase):

    def test_create_dealer_success(self) -> None:

        name = "Leonardo Fernando"
        cpf = "555.555.555-57"
        email = "teste@teste.com.bb"
        password = "passageiro"

        insert_status, insert_id = DealerController.dealer_register(
            name=name, cpf=cpf, email=email, password=password
        )

        self.assertTrue(insert_status)
        self.assertIsInstance(insert_id, int)
        self.assertNotEqual(insert_id, 0)

    def test_create_dealer_incorrect_cpf(self) -> None:

        name = "Leonardo Fernando"
        cpf = "55.55.55-57"
        email = "teste@teste.com.bb"
        password = "passageiro"

        insert_status, insert_id = DealerController.dealer_register(
            name=name, cpf=cpf, email=email, password=password
        )

        self.assertFalse(insert_status)
        self.assertIsInstance(insert_id, int)
        self.assertEqual(insert_id, 0)

    def test_create_dealer_incorrect_email(self) -> None:

        name = "Leonardo Fernando"
        cpf = "555.555.555-59"
        email = "testeteste.com.bb"
        password = "passageiro"

        insert_status, insert_id = DealerController.dealer_register(
            name=name, cpf=cpf, email=email, password=password
        )

        self.assertFalse(insert_status)
        self.assertIsInstance(insert_id, int)
        self.assertEqual(insert_id, 0)

    def test_dealer_login_success(self) -> None:

        email = "teste@teste.com"
        password = "senha123"

        result = DealerController.dealer_login(email=email, password=password)

        self.assertTrue(result)

    def test_dealer_login_fail(self) -> None:

        email = "teste@teste.com"
        password = "senha"

        result = DealerController.dealer_login(email=email, password=password)

        self.assertTrue(result)
