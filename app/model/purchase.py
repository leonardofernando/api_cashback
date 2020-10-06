from .model import Model


class Purchase(Model):

    _table = "Purchase"
    _pk = "id_purchase"

    id_purchase: int = 0
    code: int = 0
    value: str = ""
    date: str = ""
    cpf: str = ""
    status: str = ""
    # status: str = "Em validação"
