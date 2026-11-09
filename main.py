
import asyncio
from decimal import Decimal

from market_data.feed_generator import generate_market_data
from market_data.models import MarketTick
from market_data.feed_handler import MarketDataHandler
from analytics.market_stats import MarketStats


async def main():
    handler = MarketDataHandler()
    stats = MarketStats()

    async for data in generate_market_data(count=20, delay=0.01):
        tick = MarketTick(
            symbol=data["symbol"],
            price=Decimal(data["price"]),
            volume=data["volume"],
            timestamp=data["timestamp"],
        )

        handler.process_tick(tick)
        stats.update(tick)

        print(
            f"{tick.symbol}: ${tick.price} "
            f"(volume: {tick.volume})"
        )

    print("\n=== FINAL SUMMARY ===")
    print(handler.snapshot())

    for symbol in handler.latest_prices:
        print(stats.snapshot(symbol))


if __name__ == "__main__":
    asyncio.run(main())
