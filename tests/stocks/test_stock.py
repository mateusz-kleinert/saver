import pytest

from datetime import date

from saver.stocks.market import Market
from saver.stocks.operation import StockOperation
from saver.stocks.stock import Stock


@pytest.fixture
def make_market():
    def _make_market(name, country_code):
        return Market(name=name, country_code=country_code)

    return _make_market


@pytest.fixture
def make_stock():
    def _make_stock(name, currency, market):
        return Stock(name=name, currency=currency, market=market)

    return _make_stock


@pytest.fixture
def make_operation():
    def _make_stock_operation(date, stock, amount, price, commission):
        return StockOperation(
            date=date, stock=stock, amount=amount, price=price, commission=commission
        )

    return _make_stock_operation
