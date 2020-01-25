from typing import List

from saver.stocks.market import Market


class Stock:
    def __init__(self, name: str, currency: str, market: Market) -> None:
        self.name = name
        self.currency = currency
        self.market = market

        self.operations: List['StockOperation'] = []

    def __str__(self) -> str:
        return f"{self.market}-(self.name)"

    def __repr__(self) -> str:
        return f"{self.market}-(self.name)"
