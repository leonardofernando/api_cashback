from flask import request
from functools import wraps
from .fields_validator import FieldsValidator


class RouterValidator:

    @staticmethod
    def required_fields(fields: tuple, body: dict):

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
        """Valida a rota de mensagens."""

        @wraps(func)
        def decorator(*args, **kwargs):
            """Rota de mensagens decorator."""
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
        """Valida a rota de mensagens."""

        @wraps(func)
        def decorator(*args, **kwargs):
            """Rota de mensagens decorator."""
            errors = {}

            body = request.json
            if not body:
                return {"json": "Não foi informado o corpo do json!"}, 400

            fields = ("email", "senha")
            is_valid_fields, message = RouterValidator.required_fields(fields=fields, body=body)
            if not is_valid_fields:
                errors.update(message)

            is_valid_email, message = FieldsValidator.valid_email(email=body.get("email"))
            if not is_valid_email:
                errors.update(message)

            if errors:
                return {"erros": errors}, 400

            return func(*args, **kwargs)

        return decorator

    @staticmethod
    def validate_purchase_register_fields(func):
        """Valida a rota de mensagens."""

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
