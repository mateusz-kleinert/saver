from saver.accounts.operation import AccountOperationType, AccountOperation
from saver.enums.enums import Currencies


class BillingAccount:
    def __init__(self, name: str, currency: Currencies, balance: float) -> None:
        self.name = name
        self.currency = currency
        self.balance = balance

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
