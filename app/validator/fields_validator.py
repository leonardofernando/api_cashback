import re
import hashlib
from datetime import datetime
from typing import Tuple


class FieldsValidator:

    @staticmethod
    def valid_cpf(cpf: str) -> Tuple[bool, dict]:
        """
        Função para verificar se cpf é válido.

        :param str cpf: Cpf do revendedor
        :return bool, dict: Status da operação e mensagem
        """

        if not cpf:
            return False, {"cpf": "O cpf não foi informado!"}

        cpf_regx = r"\d{3}.\d{3}.\d{3}-\d{2}"
        cpf_match = re.match(cpf_regx, cpf)

        if not cpf_match:
            return False, {"cpf": "O cpf não é válido!"}
        return True, {}

    @staticmethod
    def valid_email(email: str) -> Tuple[bool, dict]:
        """
        Função para verificar se email é válido.

        :param str email: Email do revendedor
        :return bool, dict: Status da operação e mensagem
        """

        if not email:
            return False, {"email": "O email não foi informado!"}

        email_regx = r"^[\w\.\+\-]+\@[\w\.\+\-]+$"
        email_match = re.match(email_regx, email)

        if not email_match:
            return False, {"email": "O email não é válido!"}
        return True, {}

    @staticmethod
    def valid_value(value: int) -> Tuple[bool, dict]:
        """
        Função para verificar se valor da compra é válido.

        :param int value: Valor da compra
        :return bool, dict: Status da operação e mensagem
        """

        if not value:
            return False, {"valor": "O valor não foi informado!"}

        if not isinstance(value, int):
            return False, {"valor": "O valor não é válido!"}
        return True, {}

    @staticmethod
    def valid_date(date: str) -> Tuple[bool, dict]:
        """
        Função para verificar se data é válida.

        :param str date: Data da compra
        :return bool, dict: Status da operação e mensagem
        """

        if not date:
            return False, {"data": "A data não foi informada!"}

        try:
            formated_date = datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            return False, {"data": "A data não é válida!"}

        return True, {}
