from flask import request
from functools import wraps
import jwt
from datetime import datetime, timedelta


class JWTValidator:

    jwt_secret_key = "7ac1a75767999e436583319bc57e1ced"

    @staticmethod
    def make_jwt(cpf: str) -> str:
        """
        Função para criar token de validação.

        :param str cpf: Cpf do revendedor
        :return str: Token jwt
        """

        jwt_body = {
            'cpf': cpf,
            'exp': datetime.utcnow() + timedelta(minutes=15)
        }

        jwt_token = jwt.encode(payload=jwt_body, key=JWTValidator.jwt_secret_key, algorithm='HS256')

        return jwt_token.decode("utf-8")
