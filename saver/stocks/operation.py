from enum import Enum
from datetime import date

from saver.stocks.stock import Stock
from saver.stocks.market import Market


class StockOperationType(Enum):
    BUY = "BUY"
    SELL = "SELL"


class StockOperation:
    """
    Event class represents a single Event of buying/selling Stocks.
    """

    def __init__(
        self,
        operation_type: StockOperationType,
        market: Market,
        date: date,
        stock: Stock,
        amount: int,
        price: float,
        commission: float,
    ) -> None:
        self.operation_type = operation_type
        self.date = date
        self.market = market
        self.stock = stock
        self.amount = amount
        self.price = price
        self.commission = commission

    def __str__(self) -> str:
        return f"{self.date}-{self.operation_type}-{self.market}-{self.stock}"

    def __repr__(self) -> str:
        return f"{self.date}-{self.operation_type}-{self.market}-{self.stock}"
