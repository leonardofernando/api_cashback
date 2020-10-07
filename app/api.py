"""Api.

[x] Rota para cadastrar um novo revendedor(a) exigindo no mínimo nome completo, CPF, e- mail e senha;

[x] Rota para validar um login de um revendedor(a);

[x] Rota para cadastrar uma nova compra exigindo no mínimo código, valor, data e CPF do revendedor(a).
    Todos os cadastros são salvos com o status “Em validação” exceto quando o CPF do revendedor(a) for
    153.509.460-56, neste caso o status é salvo como “Aprovado”;

[x] Rota para listar as compras cadastradas retornando código, valor, data, % de cashback aplicado para
    esta compra, valor de cashback para esta compra e status;

[x] Rota para exibir o acumulado de cashback até o momento, essa rota irá consumir essa informação de
    uma API externa disponibilizada pelo Boticário.
"""
from flask import Flask, request
from app.validator.router_validator import RouterValidator
from app.controller.dealer_controller import DealerController
from app.controller.cashback_controller import CashbackController
from app.controller.purchase_controller import PurchaseController


app = Flask(__name__)


@app.route("/healthcheck", methods=["GET"])
def health_check():
    """Função para checar a saúde da api."""
    return "OK", 200


@app.route("/revendedor/cadastrar", methods=["POST"])
@RouterValidator.validate_dealer_register_fields
def dealer_register():
    """Função para cadastrar novo revendedor."""
    body = request.json
    is_registered, message = DealerController().dealer_register(
        name=body.get("nome"), cpf=body.get("cpf"), email=body.get("email"), password=body.get("senha")
    )

    if not is_registered:
        return message, 400

    return message, 201


@app.route("/revendedor/login", methods=["POST"])
@RouterValidator.validate_dealer_login_fields
def dealer_login():
    """Função para realizar login do revendedor."""
    body = request.json
    login_status = DealerController().dealer_login(
        email=body.get("email"), password=body.get("senha")
    )

    if not login_status:
        return {"message": "Incorrect user or password! Please try again."}, 400

    return {"message": "Logged with success"}, 200


@app.route("/compra/cadastrar", methods=["POST"])
@RouterValidator.validate_purchase_register_fields
def purchase_register():
    """Função para cadastrar nova compra."""
    body = request.json

    is_registered, message = PurchaseController.purchase_register(
        code=body.get('codigo'), value=body.get('valor'), date=body.get('data'), cpf=body.get('cpf')
    )
    if not is_registered:
        return message, 400

    return message, 201


@app.route("/compra/listar", methods=["GET"])
def purchase_list():
    """Função para listar compras."""
    purchases_list = PurchaseController.get_purchases()

    return {"purchases": purchases_list}, 200


@app.route("/cashback", methods=["GET"])
def get_cashback():
    """Função para resgatar quantidade de cashback."""
    credit = CashbackController.get_chashback_amount()
    return {"cashback_credit": credit}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
