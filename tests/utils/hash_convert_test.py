import unittest
from app.utils.hash_convert import HashConvert


class HashConvertTest(unittest.TestCase):

    def test_convert_password_to_hash_success(self):
        """
        Testa se a string é criptografada corretamente.

        :return:
        """

        password = "senha123"

        result = HashConvert.str_to_hash(string=password)

        self.assertIsInstance(result, str)
