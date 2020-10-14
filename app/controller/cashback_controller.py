import requests
from typing import Tuple


class CashbackController:

    @staticmethod
    def get_chashback_amount() -> int:
        """
        Função para pegar resultado de cashback de api externa.
        url de exemplo:
            https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf=12312312323

        :return int: Valor do crédito de cashback
        """

        url_api_cashbak = "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback"
        payload = {"cpf": 12312312323}
        headers = {"token": "ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm"}

        response = requests.get(url=url_api_cashbak, params=payload, headers=headers)

        content = response.json()
        credit = content.get("body").get("credit")

        return credit

    @staticmethod
    def get_cashback_percent(value: int) -> Tuple[float, str]:
        """
        Função para calcular porcentagem do cashback da compra.

        :param int value: Valor da compra
        :return float, str: Valor da porcentagem de cashback e descrição
        """

        cashback_percent = 0
        cashback_description = "0%"

        if 0 < value < 1000:
            cashback_percent = 0.10
            cashback_description = "10%"
        elif 1001 < value < 1500:
            cashback_percent = 0.15
            cashback_description = "15%"
        elif 1501 < value:
            cashback_percent = 0.20
            cashback_description = "20%"

        return cashback_percent, cashback_description
