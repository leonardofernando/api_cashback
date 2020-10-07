import unittest
from app import CashbackController


class CashbackControllerTest(unittest.TestCase):

    def test_get_valid_cashback_10_percent(self) -> None:
        value = 850
        percent_expected = 0.10

        cashback_percent, _ = CashbackController.get_cashback_percent(value=value)

        self.assertEqual(cashback_percent, percent_expected)

    def test_get_valid_cashback_15_percent(self) -> None:
        value = 1463
        percent_expected = 0.15

        cashback_percent, _ = CashbackController.get_cashback_percent(value=value)

        self.assertEqual(cashback_percent, percent_expected)

    def test_get_valid_cashback_20_percent(self) -> None:
        value = 2597
        percent_expected = 0.20

        cashback_percent, _ = CashbackController.get_cashback_percent(value=value)

        self.assertEqual(cashback_percent, percent_expected)

    def test_get_invalid_cashback_percent(self) -> None:
        value = 2597
        percent_expected = 0.10

        cashback_percent, _ = CashbackController.get_cashback_percent(value=value)

        self.assertNotEqual(cashback_percent, percent_expected)

    def test_get_valid_cashback_amount(self) -> None:

        cashback_amount = CashbackController.get_chashback_amount()

        self.assertIsInstance(cashback_amount, int)
