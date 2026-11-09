
from decimal import Decimal

from market_data.models import MarketTick


class MarketDataHandler:
    def __init__(self):
        self.latest_prices: dict[str, Decimal] = {}
        self.message_count = 0
        self.total_volume = 0
        self.last_ticks: dict[str, MarketTick] = {}

    def process_tick(self, tick: MarketTick) -> None:
        if not isinstance(tick, MarketTick):
            raise TypeError("Expected MarketTick")

        self.latest_prices[tick.symbol] = tick.price
        self.last_ticks[tick.symbol] = tick

        self.message_count += 1
        self.total_volume += tick.volume

    def get_latest_price(self, symbol: str) -> Decimal | None:
        return self.latest_prices.get(symbol)

    def get_all_prices(self) -> dict[str, Decimal]:
        return self.latest_prices.copy()

    def get_last_tick(self, symbol: str) -> MarketTick | None:
        return self.last_ticks.get(symbol)

    def snapshot(self) -> dict:
        return {
            "message_count": self.message_count,
            "total_volume": self.total_volume,
            "latest_prices": {
                symbol: str(price)
                for symbol, price in self.latest_prices.items()
            },
        }
