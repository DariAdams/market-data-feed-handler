
from decimal import Decimal

from market_data.models import MarketTick


class MarketStats:
    def __init__(self):
        self.prices: dict[str, list[Decimal]] = {}
        self.volumes: dict[str, int] = {}

    def update(self, tick: MarketTick) -> None:
        self.prices.setdefault(tick.symbol, []).append(tick.price)

        self.volumes[tick.symbol] = (
            self.volumes.get(tick.symbol, 0) + tick.volume
        )

    def average_price(self, symbol: str) -> Decimal | None:
        prices = self.prices.get(symbol)

        if not prices:
            return None

        return sum(prices, Decimal("0")) / len(prices)

    def highest_price(self, symbol: str) -> Decimal | None:
        prices = self.prices.get(symbol)

        return max(prices) if prices else None

    def lowest_price(self, symbol: str) -> Decimal | None:
        prices = self.prices.get(symbol)

        return min(prices) if prices else None

    def total_volume(self, symbol: str) -> int:
        return self.volumes.get(symbol, 0)

    def snapshot(self, symbol: str) -> dict:
        return {
            "symbol": symbol,
            "average_price": self.average_price(symbol),
            "highest_price": self.highest_price(symbol),
            "lowest_price": self.lowest_price(symbol),
            "total_volume": self.total_volume(symbol),
        }
