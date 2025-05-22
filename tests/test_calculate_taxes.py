import pytest
from src.calculate_taxes import calculate_taxes


@pytest.mark.parametrize("tax_rate, expected", [
    (10, [1100.0, 284.02, 4950.55, 28.38, 330.11, 1.1]),
    (15, [1150.0, 296.93, 5175.57, 29.67, 345.12, 1.15]),
    (20, [1200.0, 309.84, 5400.6, 30.96, 360.12, 1.2])
])
def test_calculate_taxes_success(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected
