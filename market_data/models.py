
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class MarketTick:
    symbol: str
    price: Decimal
    volume: int
    timestamp: float

    def __post_init__(self):
        if not isinstance(self.symbol, str) or not self.symbol.strip():
            raise ValueError("Symbol must be a non-empty string")

        if not isinstance(self.price, Decimal):
            raise TypeError("Price must be a Decimal")

        if not self.price.is_finite() or self.price <= 0:
            raise ValueError("Price must be positive and finite")

        if type(self.volume) is not int or self.volume < 0:
            raise ValueError("Volume must be a non-negative integer")

        if not isinstance(self.timestamp, (int, float)):
            raise TypeError("Timestamp must be numeric")
