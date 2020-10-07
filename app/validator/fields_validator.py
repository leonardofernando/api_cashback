import re
import hashlib
from datetime import datetime


class FieldsValidator:

    @staticmethod
    def valid_cpf(cpf: str) -> bool:

        if not cpf:
            return False

        cpf_regx = r"\d{3}.\d{3}.\d{3}-\d{2}"
        cpf_match = re.match(cpf_regx, cpf)

        if not cpf_match:
            return False
        return True

    @staticmethod
    def valid_email(email: str) -> bool:

        if not email:
            return False

        email_regx = r"^[\w\.\+\-]+\@[\w\.\+\-]+$"
        email_match = re.match(email_regx, email)

        if not email_match:
            return False
        return True
