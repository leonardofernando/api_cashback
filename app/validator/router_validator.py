import json
from functools import wraps
from flask import Response, request


class RouterValidator:

    @staticmethod
    def dealer_login_fields(func):

        @wraps(func)
        def decorator(*args, **kwargs):
            errors = {}
            body = request.json

            # verifica campos requeridos
            required_fields = ("email", "senha")

            # verifica campo email com regxp

            if len(errors) > 0:
                # RoutersValidator.__add_failed_request()
                return Response(errors, 400)

            return func(*args, **kwargs)

        return decorator

    @staticmethod
    def dealer_register_fields(func):

        @wraps(func)
        def decorator(*args, **kwargs):
            errors = {}
            body = request.json

            # verifica campos requeridos
            required_fields = ("name", "cpf", "email", "password")

            # verifica campos como cpf, email com regxp


            if len(errors) > 0:
                # RoutersValidator.__add_failed_request()
                return Response(errors, 400)

            return func(*args, **kwargs)

        return decorator

    @staticmethod
    def check_required_fields(fields: tuple, payload: dict):
        """Verifica se os campos requeridos estão no dicionário informado.

        Args:
            fields (tuple): lista com os nomes dos campos requerido
            payload (dict): dicionário onde iremos verificar se os campos foram enviados

        Returns:
            bool, list: [description]
        """
        result = list(filter(lambda x: payload.get(x, False), fields))
        return (len(result) == len(fields)), (set(fields) - set(result))
