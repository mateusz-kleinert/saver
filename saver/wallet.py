from typing import Dict

from saver.accounts.billing_account import BillingAccount
from saver.accounts.brokerage_account import BrokerageAccount


class Wallet:
    def __init__(self) -> None:
        # Billing account
        self.billing_accounts: Dict[str, BillingAccount] = {}
        # Brokerage accounts
        self.brokerage_accounts: Dict[str, BrokerageAccount] = {}
