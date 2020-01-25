class Stock:
    def __init__(self, name: str, currency: str) -> None:
        self.name = name
        self.currency = currency

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> str:
        return self.name

    def __eq__(self, other: 'Stock') -> bool:
        if (self.name == other.name and
            self.currency == other.currency):
            return True
        
        return False

