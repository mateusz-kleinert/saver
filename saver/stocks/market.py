class Market:
    def __init__(self, name: str, country_code: str) -> None:
        self.name = name
        self.country_code = country_code

    def __str__(self) -> str:
        return f"{self.country_code}-{self.name}"

    def __repr__(self) -> str:
        return f"{self.country_code}-{self.name}"
