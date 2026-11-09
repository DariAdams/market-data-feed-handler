
from decimal import Decimal

from analytics.market_stats import MarketStats
from market_data.models import MarketTick


def test_average_price():
    stats = MarketStats()

    stats.update(MarketTick("AAPL", Decimal("100"), 10, 1.0))
    stats.update(MarketTick("AAPL", Decimal("200"), 20, 2.0))

    assert stats.average_price("AAPL") == Decimal("150")


def test_highest_price():
    stats = MarketStats()

    stats.update(MarketTick("AAPL", Decimal("100"), 10, 1.0))
    stats.update(MarketTick("AAPL", Decimal("200"), 20, 2.0))

    assert stats.highest_price("AAPL") == Decimal("200")


def test_lowest_price():
    stats = MarketStats()

    stats.update(MarketTick("AAPL", Decimal("100"), 10, 1.0))
    stats.update(MarketTick("AAPL", Decimal("200"), 20, 2.0))

    assert stats.lowest_price("AAPL") == Decimal("100")


def test_total_volume():
    stats = MarketStats()

    stats.update(MarketTick("AAPL", Decimal("100"), 10, 1.0))
    stats.update(MarketTick("AAPL", Decimal("200"), 20, 2.0))

    assert stats.total_volume("AAPL") == 30


def test_empty_stats():
    stats = MarketStats()

    assert stats.average_price("AAPL") is None
    assert stats.highest_price("AAPL") is None
    assert stats.lowest_price("AAPL") is None
    assert stats.total_volume("AAPL") == 0
