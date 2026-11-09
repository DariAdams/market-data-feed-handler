
# Market Data Feed Handler Configuration

HOST = "localhost"
PORT = 8766

WEBSOCKET_URL = f"ws://{HOST}:{PORT}"

SYMBOLS = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]

FEED_INTERVAL = 0.1
MAX_MESSAGES = 100

INITIAL_PRICE = 100.0
