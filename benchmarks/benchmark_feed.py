
import sys
import time
from pathlib import Path
from decimal import Decimal

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from market_data.models import MarketTick
from market_data.feed_handler import MarketDataHandler
from analytics.market_stats import MarketStats


def benchmark(count=100000):
    handler = MarketDataHandler()
    stats = MarketStats()

    tick = MarketTick(
        symbol="AAPL",
        price=Decimal("150.25"),
        volume=100,
        timestamp=time.time(),
    )

    start = time.perf_counter()

    for _ in range(count):
        handler.process_tick(tick)
        stats.update(tick)

    elapsed = time.perf_counter() - start

    print(f"Messages processed: {count:,}")
    print(f"Processing time: {elapsed:.6f} seconds")
    print(f"Throughput: {count / elapsed:,.0f} messages/second")
    print(f"Average time: {elapsed / count * 1_000_000:.3f} microseconds/message")


if __name__ == "__main__":
    benchmark()
