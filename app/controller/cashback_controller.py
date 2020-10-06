import requests


class CashbackController:

    def get_chashback_amount(self):
        pass

    @staticmethod
    def get_cashback_percent(self, value: int):

        cashback_percent = 0
        cashback_description = "0%"

        if 0 < value < 1000:
            cashback_percent = 0.10
            cashback_description = "10%"
        elif 1001 < value < 1500:
            cashback_percent = 0.15
            cashback_description = "15%"
        elif 1501 < value:
            cashback_percent = 0.20
            cashback_description = "20%"

        return cashback_percent, cashback_description
