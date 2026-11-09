
from decimal import Decimal

import pytest

from market_data.models import MarketTick
from market_data.feed_handler import MarketDataHandler


@pytest.fixture
def handler():
    return MarketDataHandler()


def test_process_tick(handler):
    tick = MarketTick("AAPL", Decimal("150"), 100, 123456.0)

    handler.process_tick(tick)

    assert handler.message_count == 1
    assert handler.total_volume == 100


def test_latest_price(handler):
    handler.process_tick(
        MarketTick("AAPL", Decimal("150"), 100, 123456.0)
    )

    assert handler.get_latest_price("AAPL") == Decimal("150")


def test_update_price(handler):
    handler.process_tick(
        MarketTick("AAPL", Decimal("150"), 100, 123456.0)
    )

    handler.process_tick(
        MarketTick("AAPL", Decimal("155"), 200, 123457.0)
    )

    assert handler.get_latest_price("AAPL") == Decimal("155")


def test_unknown_symbol(handler):
    assert handler.get_latest_price("UNKNOWN") is None


def test_invalid_tick(handler):
    with pytest.raises(TypeError):
        handler.process_tick("invalid")
