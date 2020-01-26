from datetime import date
from enum import Enum


class AccountOperationType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    INITALIZE = "INITIALIZE"


class AccountOperation:
    def __init__(
        self,
        operation_type: AccountOperationType,
        date: date,
        currency: str,
        amount: float,
    ) -> None:
        self.operation_type = operation_type
        self.currency = currency
        self.amount = amount
        self.date = date
