from flask import Flask, request
from app.validator.router_validator import RouterValidator
from app.controller.dealer_controller import DealerController
from app.controller.cashback_controller import CashbackController
from app.controller.purchase_controller import PurchaseController


app = Flask(__name__)


@app.route("/healthcheck", methods=["GET"])
def health_check():
    """Função para checar a saúde da api."""
    return {"status": "OK"}, 200


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
    login_status, message = DealerController().dealer_login(
        cpf=body.get("cpf"), password=body.get("senha")
    )

    if not login_status:
        return message, 401

    return message, 200


@app.route("/compras/cadastrar", methods=["POST"])
@RouterValidator.validate_jwt
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


@app.route("/compras/listar", methods=["GET"])
@RouterValidator.validate_jwt
def purchase_list():
    """Função para listar compras."""
    purchases_list = PurchaseController.get_purchases()

    return {"compras": purchases_list}, 200


@app.route("/cashback", methods=["GET"])
def get_cashback():
    """Função para resgatar quantidade de cashback."""
    credit = CashbackController.get_chashback_amount()
    return {"credito_cashback": credit}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
