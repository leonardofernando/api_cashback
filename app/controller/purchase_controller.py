

class PurchaseController:

    FREE_CPFS = ["153.509.460-56"]

    def purchase_register(self, code: int, value: str, date: str, cpf: str, status: str = "Em validação"):

        if cpf in self.FREE_CPFS:
            status = "Aprovado"

    def get_purchases(self):
        pass
