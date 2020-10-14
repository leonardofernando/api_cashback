import jwt
from typing import Tuple
from flask import request
from functools import wraps
from .fields_validator import FieldsValidator
from app.controller.dealer_controller import DealerController


class RouterValidator:

    jwt_secret_key = "7ac1a75767999e436583319bc57e1ced"

    @staticmethod
    def required_fields(fields: tuple, body: dict) -> Tuple[bool, dict]:
        """
        Função para validar os campos obrigatórios do payload informado.

        :param tuple fields: Campos obrigatórios do payload
        :param dict body: Payload da requisição
        :return bool, dict: Status da operação e mensagem
        """

        body_keys = body.keys()

        missing_fields = list(set(fields) - set(body_keys))

        if missing_fields:
            message = {
                "campos": {
                    "mensagem": "Não foram encontrados todos os campos necessários!",
                    "campos_faltando": missing_fields,
                }
            }
            return False, message

        return True, {}

    @staticmethod
    def validate_dealer_register_fields(func):
        """
        Valida campos de registro do revendedor.

        :param func:
        :return:
        """

        @wraps(func)
        def decorator(*args, **kwargs):
            """Decorator."""
            errors = {}

            body = request.json
            if not body:
                return {"json": "Não foi informado o corpo do json!"}, 400

            fields = ("nome", "cpf", "email", "senha")
            is_valid_fields, message = RouterValidator.required_fields(fields=fields, body=body)
            if not is_valid_fields:
                errors.update(message)

            is_valid_cpf, message = FieldsValidator.valid_cpf(cpf=body.get("cpf"))
            if not is_valid_cpf:
                errors.update(message)

            is_valid_email, message = FieldsValidator.valid_email(email=body.get("email"))
            if not is_valid_email:
                errors.update(message)

            if errors:
                return {"erros": errors}, 400

            return func(*args, **kwargs)

        return decorator

    @staticmethod
    def validate_dealer_login_fields(func):
        """
        Valida campos de login do revendedor.

        :param func:
        :return:
        """

        @wraps(func)
        def decorator(*args, **kwargs):
            """Decorator."""
            errors = {}

            body = request.json
            if not body:
                return {"json": "Não foi informado o corpo do json!"}, 400

            fields = ("cpf", "senha")
            is_valid_fields, message = RouterValidator.required_fields(fields=fields, body=body)
            if not is_valid_fields:
                errors.update(message)

            is_valid_cpf, message = FieldsValidator.valid_cpf(cpf=body.get("cpf"))
            if not is_valid_cpf:
                errors.update(message)

            if errors:
                return {"erros": errors}, 400

            return func(*args, **kwargs)

        return decorator

    @staticmethod
    def validate_purchase_register_fields(func):
        """
        Valida campos de registro da compra.

        :param func:
        :return:
        """

        @wraps(func)
        def decorator(*args, **kwargs):
            """Rota de mensagens decorator."""
            errors = {}

            body = request.json
            if not body:
                return {"json": "Não foi informado o corpo do json!"}, 400

            fields = ("codigo", "valor", "data", "cpf")
            is_valid_fields, message = RouterValidator.required_fields(fields=fields, body=body)
            if not is_valid_fields:
                errors.update(message)

            is_valid_cpf, message = FieldsValidator.valid_cpf(cpf=body.get("cpf"))
            if not is_valid_cpf:
                errors.update(message)

            is_valid_value, message = FieldsValidator.valid_value(value=body.get("valor"))
            if not is_valid_value:
                errors.update(message)

            is_valid_data, message = FieldsValidator.valid_date(date=body.get("data"))
            if not is_valid_data:
                errors.update(message)

            if errors:
                return {"erros": errors}, 400

            return func(*args, **kwargs)

        return decorator

    @staticmethod
    def validate_jwt(func):
        """
        Valida token de autenticação jwt.

        :param func:
        :return:
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            authorization = request.headers.get('authorization')
            if not authorization:
                return {"header": "Não foi informado o authorization!"}, 401
            try:
                token_data = jwt.decode(authorization, RouterValidator.jwt_secret_key, True, 'HS256')
                dealer = DealerController.get_dealer(token_data['cpf'])

                if not dealer:
                    return {"header": "Token inválido!"}, 401

            except Exception as error:
                return {"header": "Token inválido!"}, 401

            return func(*args, **kwargs)

        return wrapper
