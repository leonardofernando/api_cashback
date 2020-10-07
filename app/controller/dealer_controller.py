from app import Dealers


class DealerController:

    def dealer_register(self, name: str, cpf: str, email: str, password: str) -> bool:

        dealer = Dealers()
        dealer.name = name
        dealer.cpf = cpf
        dealer.email = email
        dealer.password = password

        dealer.save()

        return True

    def get_dealer(self, email: str, password: str) -> bool:

        return True
