from typing import Tuple

from app.model.dealer import Dealer
from app.database.sqlite import SqliteConnection
from app.validator.jwt_validator import JWTValidator
from app.utils.hash_convert import HashConvert


class DealerController:

    @staticmethod
    def dealer_register(name: str, cpf: str, email: str, password: str) -> Tuple[bool, dict]:
        """
        Função para cadastrar novo revendedor.

        :param str name: Nome do revendedor
        :param str cpf: Cpf do revendedor
        :param str email: Email do revendedor
        :param str password: Senha do revendedor
        :return bool, dict: Status da operação e mensagem
        """

        with SqliteConnection() as database:

            password_hash = HashConvert.str_to_hash(password)
            params = (name, cpf, email, password_hash)
            insert_id, db_message = database.insert(table=Dealer.table, columns=Dealer.columns, params=params)

            if not insert_id:
                return False, {"mensagem": "Ocorreu um erro ao inserir o revendedor!", "erro": db_message}

        return True, {"mensagem": "O revendedor foi inserido com sucesso!"}

    @staticmethod
    def dealer_login(cpf: str, password: str) -> Tuple[bool, dict]:
        """
        Função para realizar login do revendedor.

        :param str cpf: Cpf do revendedor
        :param str password: Senha do revendedor
        :return bool, dict: Status da operação e mensagem
        """

        dealer = DealerController.get_dealer(cpf)
        if not dealer:
            return False, {"mensahem": "Revendedor não cadastrado!"}

        password_hash = HashConvert.str_to_hash(password)
        if not password_hash == dealer["password"]:
            return False, {"mensagem": "Login/Cpf ou senha incorreto!"}

        jwt_token = JWTValidator.make_jwt(cpf=dealer["cpf"])

        return True, {"mensagem": "O revendedor foi logado com sucesso!", "token": jwt_token}

    @staticmethod
    def get_dealer(cpf: str) -> dict:
        """
        Função para procurar revendedor na base de dados.

        :param str cpf: Cpf do revendedor
        :return dict: Dados do revendedor
        """

        with SqliteConnection() as database:

            where = ('cpf',)
            params = (cpf,)

            result = database.select(model=Dealer, where=where, params=params)

            dealer = result.fetchone()
            if not dealer:
                return {}

        return dealer
