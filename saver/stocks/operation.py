from enum import Enum
from datetime import date

from saver.stocks.stock import Stock
from saver.stocks.market import Market
from saver.enums.enums import Currencies


class StockOperationType(Enum):
    BUY = "BUY"
    SELL = "SELL"


class StockOperation:
    def __init__(
        self,
        operation_type: StockOperationType,
        market: Market,
        date: date,
        stock: Stock,
        amount: int,
        price: float,
        currency: Currencies,
        commission: float,
    ) -> None:
        self.operation_type = operation_type
        self.date = date
        self.market = market
        self.stock = stock
        self.amount = amount
        self.price = price
        self.currency = currency
        self.commission = commission

    def __str__(self) -> str:
        return f"{self.date}-{self.operation_type}-{self.market}-{self.stock}"

    def __repr__(self) -> str:
        return f"{self.date}-{self.operation_type}-{self.market}-{self.stock}"
