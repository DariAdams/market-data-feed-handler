
# Real-Time Market Data Feed Handler

A Python-based market data streaming simulator designed to demonstrate asynchronous networking, WebSocket communication, event processing, and market analytics.

## Features

- Asynchronous simulated market data generation
- WebSocket server and client
- Market tick validation
- Latest price tracking by symbol
- Average, highest, and lowest price calculations
- Trading volume aggregation
- Unit tests using pytest
- Processing throughput benchmark

## Technologies

Python 3.14, asyncio, websockets, pytest, Decimal

## Installation

Run from the project root:

    python -m pip install -r requirements.txt

## Run the Simulation

    python main.py

## Run Unit Tests

    python -m pytest -v

## Run Benchmark

    python benchmarks/benchmark_feed.py

## Run WebSocket Streaming

Terminal 1:

    python -m market_data.websocket_server

Terminal 2:

    python -m market_data.websocket_client

The client receives 100 simulated market data updates.

## Architecture

Feed Generator -> WebSocket Server -> WebSocket Client
                                      |
                                      v
                              Market Data Handler
                                      |
                                      v
                                Market Analytics

## Benchmark Notes

The benchmark measures in-memory processing of preconstructed ticks. It does not include WebSocket transmission, JSON parsing, or real exchange connectivity.

Results depend on hardware and Python runtime.

## Limitations

This is an educational simulation, not a production market data platform.

It does not connect to live exchanges or implement sequence-gap recovery, reconnection, or backpressure handling.

## Future Improvements

- Automatic reconnect and recovery
- Message sequence tracking
- Bounded queues and backpressure
- Multi-client streaming
- Automated WebSocket integration tests
- GitHub Actions CI
