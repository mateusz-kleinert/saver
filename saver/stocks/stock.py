from typing import List

from saver.stocks.market import Market
from saver.enums.enums import Currencies


class Stock:
    def __init__(self, name: str, currency: Currencies, market: Market) -> None:
        self.name = name
        self.currency = currency
        self.market = market

    def __str__(self) -> str:
        return f"{self.market}-(self.name)"

    def __repr__(self) -> str:
        return f"{self.market}-(self.name)"
