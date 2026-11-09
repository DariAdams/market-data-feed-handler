
from decimal import Decimal

import pytest

from market_data.models import MarketTick


def test_valid_tick():
    tick = MarketTick("AAPL", Decimal("150.25"), 100, 123456.0)
    assert tick.symbol == "AAPL"


def test_invalid_symbol():
    with pytest.raises(ValueError):
        MarketTick("", Decimal("150"), 100, 123456.0)


def test_negative_price():
    with pytest.raises(ValueError):
        MarketTick("AAPL", Decimal("-10"), 100, 123456.0)


def test_float_price_rejected():
    with pytest.raises(TypeError):
        MarketTick("AAPL", 150.25, 100, 123456.0)


def test_negative_volume():
    with pytest.raises(ValueError):
        MarketTick("AAPL", Decimal("150"), -1, 123456.0)
