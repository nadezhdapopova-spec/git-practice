import pytest

@pytest.fixture
def prices():
    return [1000.0, 258.20, 4500.5, 25.8, 300.1, 1.0]

@pytest.fixture
def invalid_prices():
    return [0, -1, -145.2, -1000]
