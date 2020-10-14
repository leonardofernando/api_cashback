import unittest
from app.validator.fields_validator import FieldsValidator


class FieldsValidatorTest(unittest.TestCase):

    def test_valid_cpf_success(self):
        """
        Testa se cpf é válido.

        :return:
        """

        cpf = "555.555.555-55"

        result, message = FieldsValidator.valid_cpf(cpf)

        self.assertTrue(result)
        self.assertIsInstance(message, dict)

    def test_valid_cpf_fail(self):
        """
        Testa se cpf é inválido.

        :return:
        """

        cpf = "55.55.55-554"

        result, message = FieldsValidator.valid_cpf(cpf)

        self.assertFalse(result)
        self.assertIsInstance(message, dict)

    def test_valid_email_success(self):
        """
        Testa se email é válido.

        :return:
        """

        email = "teste@teste.com"

        result, message = FieldsValidator.valid_email(email)

        self.assertTrue(result)
        self.assertIsInstance(message, dict)

    def test_valid_email_fail(self):
        """
        Testa se email é inválido.

        :return:
        """

        email = "teste-teste.com"

        result, message = FieldsValidator.valid_email(email)

        self.assertFalse(result)
        self.assertIsInstance(message, dict)

    def test_valid_value_success(self):
        """
        Testa se valor é válido.

        :return:
        """

        value = 1250

        result, message = FieldsValidator.valid_value(value)

        self.assertTrue(result)
        self.assertIsInstance(message, dict)

    def test_valid_value_fail(self):
        """
        Testa se valor é inválido.

        :return:
        """

        value = 0

        result, message = FieldsValidator.valid_value(value)

        self.assertFalse(result)
        self.assertIsInstance(message, dict)

    def test_valid_date_success(self):
        """
        Testa se data é válida.

        :return:
        """

        date = "26/10/2020"

        result, message = FieldsValidator.valid_date(date)

        self.assertTrue(result)
        self.assertIsInstance(message, dict)

    def test_valid_date_fail(self):
        """
        Testa se data é inválida.

        :return:
        """

        date = "2020-10-26"

        result, message = FieldsValidator.valid_date(date)

        self.assertFalse(result)
        self.assertIsInstance(message, dict)
