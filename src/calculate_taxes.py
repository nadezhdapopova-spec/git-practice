def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError("Неверная цена")
        tax = price * tax_rate / 100
        taxed_prices.append(round(price + tax, 2))

    return taxed_prices


def calculate_tax(price: float, tax_rate: float, *, discount: int=0, rounder: int=2) -> float:
    """Вычисляет стоимость одного товара с учётом налога."""

    for arg in [price, tax_rate, discount, rounder]:
        if not isinstance(arg, (int | float)):
            raise TypeError("Ошибка типа данных")

    if price <= 0:
        raise ValueError("Неверная цена")
    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")

    new_price = price + price * tax_rate / 100

    return round(new_price - new_price * discount / 100, rounder)
