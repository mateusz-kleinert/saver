from saver.enums.enums import Countries


class Market:
    def __init__(self, name: str, country: Countries) -> None:
        self.name = name
        self.country = country

    def __str__(self) -> str:
        return f"{self.country}-{self.name}"

    def __repr__(self) -> str:
        return f"{self.country}-{self.name}"
