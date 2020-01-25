from saver.accounts.operation import AccountOperationType, AccountOperation


class BillingAccount:
    def __init__(self, name: str, currency: str, balance: float) -> None:
        self.name = name
        self.currency = currency
        self.balance = balance

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name