import pytest
from src.calculate_taxes import calculate_taxes


def test_calculate_taxes_success_1(prices):
    print(calculate_taxes(prices, 10))


def test_calculate_taxes_success_2(prices):
    print(calculate_taxes(prices, 50))


def test_calculate_taxes_success_3(prices):
    print(calculate_taxes(prices, 0))


def test_calculate_taxes_success_4(prices):
    print(calculate_taxes(prices, 1))


@pytest.mark.parametrize("prices, tax_rate, result", [
    ([1000.0, 258.20, 4500.5, 25.8, 300.1, 1.0], )
]