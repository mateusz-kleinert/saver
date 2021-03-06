from datetime import date

from saver.stocks.stock import Stock
from saver.enums.enums import Currencies


class QuotePrice:
    def __init__(
        self, open: float, max: float, min: float, close: float, currency: Currencies
    ) -> None:
        self.open = open
        self.max = max
        self.min = min
        self.close = close
        self.currency = currency


class Quote:
    def __init__(
        self,
        date: date,
        stock: Stock,
        price: QuotePrice,
        change: float,
        volume: int,
        transactions: int,
        value: float,
    ) -> None:
        self.date = date
        self.stock = stock
        self.price = price
        self.change = change
        self.volume = volume
        self.transactions = transactions
        self.value = value

    def __str__(self) -> str:
        return f"{self.date}-{self.stock}"

    def __repr__(self) -> str:
        return f"{self.date}-{self.stock}"
