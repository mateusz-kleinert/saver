from typing import List, Dict

from saver.accounts.operation import AccountOperationType, AccountOperation
from saver.stocks.stock import Stock
from saver.enums.enums import Currencies


class BrokerageAccount:
    def __init__(self, name: str, currency: Currencies, balance: float) -> None:
        self.name = name
        self.currency = currency
        self.balance = balance

        self.operations: List[AccountOperation] = []
        self.stocks: Dict[str, Stock] = {}

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
