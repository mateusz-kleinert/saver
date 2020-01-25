from datetime import date
from collections import defaultdict
from typing import DefaultDict, List

from .stock import Stock
from .market import Market

class Asset:
    """
    Asset class represents a single Event of buying Stocks.
    """
    def __init__(self, market: Market, date: date, stock: Stock, amount: int, price: float, commission: float) -> None:
        self.date = date
        self.market = market
        self.stock = stock
        self.amount = amount
        self.price = float
        self.commission = commission

    def __str__(self) -> str:
        return f"{market.name}-{self.stock.name}"

    def __repr__(self) -> str:
        return f"{market.name}-{self.stock.name}"

    def __hash__(self) -> str:
        return f"{market.name}-{self.stock.name}"

    def __eq__(self, other: 'Asset') -> bool:
        """
        Assets are considered equal if all of their user defined
        attributes are equal.
        """

        for key, value in self.__dict__.items():
            if value != other.__dict__[key]:
                return False

        return True

class Wallet:
    """
    Contains Assets from all available Markets.
    """
    def __init__(self) -> None:
        self.assets: DefaultDict[str, List[Asset]]

    def add_asset(self, asset: Asset) -> None:
        self.assets[asset].append(asset)

    def remove_asset(self, asset: Asset) -> None:
        raise NotImplemented

