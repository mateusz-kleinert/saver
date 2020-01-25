import pytest

from datetime import date

from saver.stocks.stock import Stock
from saver.stocks.wallet import Asset

@pytest.fixture
def make_stock():
    def _make_stock(name, currency):
        return Stock(name = name, currency = currency)
    
    return _make_stock

@pytest.fixture
def make_asset():
    def _make_asset(date, stock, amount, price, commission):
        return Asset(date = date, stock = stock, amount = amount,
            price = price, commission = commission)

    return _make_asset

def test_asset_equal(make_stock, make_asset):
    """ Assets are considered equal if attributes contains the same data """

    asset_one = make_asset(date(2020, 1, 10), make_stock("EXAMPLE", "PLN"),
        100, 14.05, 3.00)

    print(asset_one.__dict__.keys())
    asset_two = make_asset(date(2020, 1, 10), make_stock("EXAMPLE", "PLN"),
        100, 14.05, 3.00)

    assert asset_one == asset_two

def test_asset_not_equal(make_stock, make_asset):
    """ Assets are considered equal if attributes contains the same data """

    asset_one = make_asset(date(2020, 1, 10), make_stock("EXAMPLE", "PLN"),
        100, 14.05, 3.00)
    asset_two = make_asset(date(2020, 1, 10), make_stock("EXAMPLE", "CHF"),
        100, 14.05, 3.00)

    assert asset_one != asset_two

