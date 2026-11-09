
import asyncio
import random
import time
from decimal import Decimal

from config import SYMBOLS, FEED_INTERVAL


async def generate_market_data(
    count=100,
    delay=FEED_INTERVAL,
    seed=42,
):
    rng = random.Random(seed)

    prices = {
        symbol: Decimal(str(rng.randint(10000, 30000))) / 100
        for symbol in SYMBOLS
    }

    for _ in range(count):
        symbol = rng.choice(SYMBOLS)

        change = Decimal(rng.randint(-100, 100)) / 100
        prices[symbol] = max(Decimal("0.01"), prices[symbol] + change)

        yield {
            "symbol": symbol,
            "price": str(prices[symbol]),
            "volume": rng.randint(1, 1000),
            "timestamp": time.time(),
        }

        await asyncio.sleep(delay)
