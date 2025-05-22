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
