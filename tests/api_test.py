import unittest
import random
from app.api import app
from app.controller.dealer_controller import DealerController


class ApiTest(unittest.TestCase):

    def setUp(self) -> None:
        """
        Set up dos valores dos testes.

        :return:
        """
        self.client = app.test_client()
        self.payload_dealer_register = {
            "nome": "Dirceu Gonçalves",
            "cpf": "452.452.452-65",
            "email": "dirceu.test@teste.com",
            "senha": "dirceu12345"
        }

        self.payload_purchase_register = {
            "codigo": random.randint(0, 99999),
            "valor": random.randint(0, 1999),
            "data": "07/10/2020",
            "cpf": "456.456.456-65"
        }

    def test_healthcheck_success(self) -> None:
        """
        Testa se a chamada para o endpoint healthcheck foi um sucesso.

        :return:
        """
        response = self.client.get("/healthcheck")
        self.assertEqual(response.status_code, 200)

    def test_dealer_register_success(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor foi um sucesso.

        :return:
        """
        response = self.client.post("/revendedor/cadastrar", json=self.payload_dealer_register)
        self.assertEqual(response.status_code, 201)

    def test_dealer_register_without_payload(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor falhou com cpf incorreto.

        :return:
        """
        response = self.client.post("/revendedor/cadastrar", json={})
        self.assertEqual(response.status_code, 400)

    def test_dealer_register_without_required_fields(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor falhou com cpf incorreto.

        :return:
        """
        payload_dealer_register = {
            "data_nascimento": ""
        }
        response = self.client.post("/revendedor/cadastrar", json=payload_dealer_register)
        self.assertEqual(response.status_code, 400)

    def test_dealer_register_cpf_incorrect(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor falhou com cpf incorreto.

        :return:
        """
        payload_dealer_register = self.payload_dealer_register.copy()
        payload_dealer_register["cpf"] = "55.145.65-526"
        response = self.client.post("/revendedor/cadastrar", json=payload_dealer_register)
        self.assertEqual(response.status_code, 400)

    def test_dealer_register_email_incorrect(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor falhou com email incorreto.

        :return:
        """
        payload_dealer_register = self.payload_dealer_register.copy()
        payload_dealer_register["email"] = "dirceu.teste.com"
        response = self.client.post("/revendedor/cadastrar", json=payload_dealer_register)
        self.assertEqual(response.status_code, 400)

    def test_dealer_login_success(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor foi um sucesso.

        :return:
        """

        cpf = "555.555.555-66"
        password = "teste12345"

        DealerController.dealer_register(
            name="Lester Montes", cpf="555.555.555-66", email="teste@teste.com", password=password)

        payload = {
            "cpf": cpf,
            "senha": password
        }

        response = self.client.post("/revendedor/login", json=payload)
        self.assertEqual(response.status_code, 200)

    def test_dealer_login_fail(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor foi um sucesso.

        :return:
        """

        cpf = "333.333.333-88"
        password = "teste12345"

        payload = {
            "cpf": cpf,
            "senha": password
        }

        response = self.client.post("/revendedor/login", json=payload)
        self.assertEqual(response.status_code, 401)

    def test_purchase_register_success(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor foi um sucesso.

        :return:
        """

        cpf = "555.555.555-66"
        password = "teste12345"

        DealerController.dealer_register(
            name="Lester Montes", cpf=cpf, email="teste@teste.com", password=password)

        payload = {
            "cpf": cpf,
            "senha": password
        }

        response = self.client.post("/revendedor/login", json=payload)
        headers = {"authorization": response.json["token"]}

        payload = self.payload_purchase_register.copy()
        payload["cpf"] = cpf

        response = self.client.post("/compras/cadastrar", json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_purchase_register_success_with_approved_cpf(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor foi um sucesso.

        :return:
        """

        cpf = "153.509.460-56"
        password = "teste12345"

        DealerController.dealer_register(
            name="Lester Montes", cpf=cpf, email="teste@teste.com", password=password)

        payload = {
            "cpf": cpf,
            "senha": password
        }

        response = self.client.post("/revendedor/login", json=payload)
        headers = {"authorization": response.json["token"]}

        payload = self.payload_purchase_register.copy()
        payload["cpf"] = cpf

        response = self.client.post("/compras/cadastrar", json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_purchase_register_without_authorization(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor foi um sucesso.

        :return:
        """

        cpf = "153.509.460-56"

        headers = {"authorization": ""}

        payload = self.payload_purchase_register.copy()
        payload["cpf"] = cpf

        response = self.client.post("/compras/cadastrar", json=payload, headers=headers)
        self.assertEqual(response.status_code, 401)

    def test_purchase_register_incorrect_authorization(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor foi um sucesso.

        :return:
        """

        cpf = "153.509.460-56"

        headers = {"authorization": "1ad35s1das1d.3a1sd3a5sd"}

        payload = self.payload_purchase_register.copy()
        payload["cpf"] = cpf

        response = self.client.post("/compras/cadastrar", json=payload, headers=headers)
        self.assertEqual(response.status_code, 401)

    def test_purchase_list_success(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor foi um sucesso.

        :return:
        """

        cpf = "458.458.458-96"
        password = "teste12345"

        DealerController.dealer_register(
            name="Lester Montes", cpf=cpf, email="teste@teste.com", password=password)

        payload = {
            "cpf": cpf,
            "senha": password
        }

        response = self.client.post("/revendedor/login", json=payload)
        headers = {"authorization": response.json["token"]}

        response = self.client.get("/compras/listar", headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_cashback_success(self) -> None:
        """
        Testa se a chamada para o endpoint cadastrar revendedor foi um sucesso.

        :return:
        """

        response = self.client.get("/cashback")
        self.assertEqual(response.status_code, 200)
