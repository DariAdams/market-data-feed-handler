
import asyncio
import json
from decimal import Decimal

from websockets.asyncio.client import connect

from config import WEBSOCKET_URL, MAX_MESSAGES
from market_data.models import MarketTick
from market_data.feed_handler import MarketDataHandler
from analytics.market_stats import MarketStats


async def consume_market_data(
    url=WEBSOCKET_URL,
    max_messages=MAX_MESSAGES,
):
    handler = MarketDataHandler()
    stats = MarketStats()

    async with connect(url) as websocket:
        for _ in range(max_messages):
            message = await websocket.recv()
            data = json.loads(message)

            tick = MarketTick(
                symbol=data["symbol"],
                price=Decimal(data["price"]),
                volume=data["volume"],
                timestamp=data["timestamp"],
            )

            handler.process_tick(tick)
            stats.update(tick)

            print(
                f"{tick.symbol} | "
                f"Price: ${tick.price} | "
                f"Volume: {tick.volume}"
            )

    print("\n=== MARKET SUMMARY ===")
    print(handler.snapshot())

    return handler, stats


if __name__ == "__main__":
    asyncio.run(consume_market_data())
