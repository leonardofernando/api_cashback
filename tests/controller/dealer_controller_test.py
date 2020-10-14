import unittest
import random
from app.controller.dealer_controller import DealerController


class DealerControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        """
        Set up dos valores dos testes.

        :return:
        """
        self.name = "Leonardo Fernando"
        rand_number = random.randint(10, 99)
        self.cpf = "555.555.555-%s" % rand_number
        self.email = "teste_%s@teste.com" % rand_number
        self.password = "teste_api"

    def test_create_dealer_success(self) -> None:
        """
        Testa se revendedor é criado com sucesso.

        :return:
        """

        insert_status, message = DealerController.dealer_register(
            name=self.name, cpf=self.cpf, email=self.email, password=self.password
        )

        self.assertTrue(insert_status)
        self.assertIsInstance(message, dict)

    def test_dealer_login_success(self) -> None:
        """
        Testa se revendedor é logado com sucesso.

        :return:
        """
        DealerController.dealer_register(
            name=self.name, cpf=self.cpf, email=self.email, password=self.password
        )

        result, message = DealerController.dealer_login(cpf=self.cpf, password=self.password)

        self.assertTrue(result)
        self.assertIsInstance(message, dict)

    def test_dealer_login_invalid_cpf(self) -> None:
        """
        Testa se o cpf do revendedor é incorreto ao logar.

        :return:
        """

        DealerController.dealer_register(
            name=self.name, cpf=self.cpf, email=self.email, password=self.password
        )

        cpf = "888.888.888-99"

        result, message = DealerController.dealer_login(cpf=cpf, password=self.password)

        self.assertFalse(result)
        self.assertIsInstance(message, dict)

    def test_dealer_login_invalid_password(self) -> None:
        """
        Testa se senha do revendedor é incorreta ao logar.

        :return:
        """
        DealerController.dealer_register(
            name=self.name, cpf=self.cpf, email=self.email, password=self.password
        )

        password = "senha123"

        result, message = DealerController.dealer_login(cpf=self.cpf, password=password)

        self.assertFalse(result)
        self.assertIsInstance(message, dict)
