import unittest
from app.validator.jwt_validator import JWTValidator


class JWTValidatorTest(unittest.TestCase):

    def teste_make_jwt_token_success(self):
        """
        Testa se token jwt é retornado com sucesso.

        :return:
        """

        cpf = "555.555.555-66"

        jwt_dict = JWTValidator.make_jwt(cpf=cpf)

        self.assertIsInstance(jwt_dict, str)
