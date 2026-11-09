
import asyncio
import json

from websockets.asyncio.server import serve

from config import HOST, PORT, MAX_MESSAGES
from market_data.feed_generator import generate_market_data


async def handle_client(websocket):
    async for tick in generate_market_data(count=MAX_MESSAGES):
        await websocket.send(json.dumps(tick))


async def main():
    async with serve(handle_client, HOST, PORT):
        print(
            f"Market Data WebSocket Server running on ws://{HOST}:{PORT}",
            flush=True,
        )
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
