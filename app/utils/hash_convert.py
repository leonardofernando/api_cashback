import hashlib


class HashConvert:

    @staticmethod
    def str_to_hash(string: str):
        """
        Função para criptografar string.

        :param string:
        :return:
        """

        utf8_string = string.encode("utf-8")

        string_hash = hashlib.md5(utf8_string)

        return string_hash.hexdigest()
