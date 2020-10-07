import re
import hashlib
from datetime import datetime
from typing import Tuple


class FieldsValidator:

    @staticmethod
    def valid_cpf(cpf: str) -> Tuple[bool, dict]:

        if not cpf:
            return False, {"cpf": "O cpf não foi informado!"}

        cpf_regx = r"\d{3}.\d{3}.\d{3}-\d{2}"
        cpf_match = re.match(cpf_regx, cpf)

        if not cpf_match:
            return False, {"cpf": "O cpf não é válido!"}
        return True, {}

    @staticmethod
    def valid_email(email: str) -> Tuple[bool, dict]:

        if not email:
            return False, {"email": "O email não foi informado!"}

        email_regx = r"^[\w\.\+\-]+\@[\w\.\+\-]+$"
        email_match = re.match(email_regx, email)

        if not email_match:
            return False, {"email": "O email não é válido!"}
        return True, {}

    @staticmethod
    def valid_value(value: str) -> Tuple[bool, dict]:

        if not value:
            return False, {"valor": "O valor não foi informado!"}

        value_regx = r"^\d+[\,\.]\d{2}$"
        value_match = re.match(value_regx, value)

        if not value_match:
            return False, {"valor": "O valor não é válido!"}
        return True, {}
