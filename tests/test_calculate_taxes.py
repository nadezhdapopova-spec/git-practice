import pytest
from src.calculate_taxes import calculate_taxes, calculate_tax


@pytest.mark.parametrize("tax_rate, expected", [
    (10, [1100.0, 284.02, 4950.55, 28.38, 330.11, 1.1]),
    (15, [1150.0, 296.93, 5175.57, 29.67, 345.12, 1.15]),
    (20, [1200.0, 309.84, 5400.6, 30.96, 360.12, 1.2]),
    (0, [1000.0, 258.20, 4500.5, 25.8, 300.1, 1.0])
])
def test_calculate_taxes_success(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate(prices):
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes(prices, -5.0)
    assert str(exc_info.value) == "Неверный налоговый процент"


def test_calculate_taxes_invalid_price(invalid_prices):
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes(invalid_prices, 10.0)
    assert str(exc_info.value) == "Неверная цена"


@pytest.mark.parametrize("price, tax_rate, expected", [
    (1000.0, 10, 1100.0),
    (258.20, 15, 296.93),
    (4500.5, 20, 5400.60),
    (25.8, 0, 25.8)
])
def test_calculate_tax_success(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected


@pytest.mark.parametrize("price, tax_rate, discount, rounder, expected", [
    (1000.25, 10, 10, 0, 990),
    (258.20, 15, 5, 1, 282.1),
    (4500.55, 20, 0, 2, 5400.66),
    (25.99, 0, 15, 3, 22.091)
])
def test_calculate_tax_success(price, tax_rate, discount, rounder, expected):
    assert calculate_tax(price, tax_rate, discount=discount, rounder=rounder) == expected

def test_calculate_tax_without_discount():
    assert calculate_tax(1000.25, 10) == 1100.28


@pytest.mark.parametrize("price, tax_rate", [
    (1000.0, -1.5),
    (258.20, -1),
    (4500.5, 100),
    (25.8, 110)
])
def test_calculate_tax_invalid_tax_rate(price, tax_rate):
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, tax_rate)
    assert str(exc_info.value) == "Неверный налоговый процент"


@pytest.mark.parametrize("price, tax_rate", [
    (-1000, 10),
    (0, 13),
    (-1, 1)
])
def test_calculate_tax_invalid_price(price, tax_rate):
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, tax_rate)
    assert str(exc_info.value) == "Неверная цена"


@pytest.mark.parametrize("price, tax_rate, discount, rounder", [
    ("1000.25", 10, 10, 0),
    (258.20, "15", 5, 1),
    (4500.55, 20, "0", 2),
    (25.99, 0, 15, "3")
])
def test_calculate_tax_wrong_type(price, tax_rate, discount, rounder):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount=discount, rounder=rounder)


def test_calculate_tax_kwargs():
    with pytest.raises(TypeError):
        calculate_tax(100.0, 5, 3, 10)
