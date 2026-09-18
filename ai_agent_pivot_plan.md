# Navid API: Architectural Pivot Plan for AI Agents

This document outlines a phased, step-by-step roadmap to implement the architectural pivots inspired by OpenBB (Modular Gateway), ArcticDB (Time-Series Datastore), and vn.py (Event-Driven/Push Architecture).

It is designed for a daily AI agent to pick up individual, self-contained tasks. Each task builds upon the last and defines clear prerequisites and "Definition of Done" criteria.

---

## Phase 1: Modular Gateway Architecture (Inspiration: OpenBB)
**Goal:** Decouple the API from specific data providers (like TSETMC). Ensure that if the data source changes or fails, the core routing logic remains intact.

### Task 1: Define Data Provider Protocols
*   **Goal:** Create a strict abstract interface for fetching market data.
*   **Context:** Currently, the API routes likely call the scraper/client directly. We need a `Protocol` or `ABC` (Abstract Base Class).
*   **Instructions for AI:**
    1. Create `app/core/provider_interface.py`.
    2. Define abstract methods for fetching a stock's current price, intraday chart, and historical data.
    3. Use Pydantic schemas for the return types.
*   **Definition of Done:** The abstract interface exists, is fully typed, and unit tests verify that it cannot be instantiated directly.

### Task 2: Refactor Existing Client to Implement Protocol
*   **Goal:** Adapt the current TSETMC client to adhere strictly to the new interface.
*   **Context:** `app/tset_client/` contains the legacy logic.
*   **Instructions for AI:**
    1. Create a wrapper class in `app/tset_client/provider.py` that inherits from the interface created in Task 1.
    2. Map the existing functions to the abstract methods.
    3. Ensure the output perfectly matches the Pydantic schemas.
*   **Definition of Done:** The new provider class passes all type checks and successfully wraps the old logic.

### Task 3: Update API Routes to Use Gateway Pattern
*   **Goal:** Make the FastAPI endpoints use a registry of providers rather than hardcoded logic.
*   **Context:** Modify `app/api/` and `app/main.py`.
*   **Instructions for AI:**
    1. Implement a dependency injection strategy in FastAPI to inject the active provider.
    2. Refactor `app/api/` routes to request data exclusively through the injected provider interface.
*   **Definition of Done:** All REST endpoints function identically to before but are now decoupled from the underlying data source.

---

## Phase 2: Time-Series Database Migration (Inspiration: ArcticDB)
**Goal:** Move away from dynamic SQLAlchemy tables for massive tick data, using a specialized time-series storage approach (like ArcticDB, QuestDB, or TimescaleDB).

### Task 4: Setup Time-Series Datastore Infrastructure
*   **Goal:** Configure the project to connect to the new datastore.
*   **Context:** `app/db.py`, `pyproject.toml`.
*   **Instructions for AI:**
    1. Add the chosen time-series DB client to Poetry (e.g., `arcticdb` or `questdb`).
    2. Update `app/core/config.py` to include connection strings for the new datastore.
    3. Create `app/db_timeseries.py` to handle the connection pool and initialization.
*   **Definition of Done:** The application can successfully connect to the time-series datastore on startup without crashing.

### Task 5: Implement Caching & Storage Layer
*   **Goal:** Write market data fetched by the Provider (Phase 1) into the Time-Series DB.
*   **Context:** `app/data/` or a new `app/storage/` module.
*   **Instructions for AI:**
    1. Create a data layer that takes the Pydantic models from the provider and converts them to the format required by the datastore (e.g., Pandas DataFrames for ArcticDB).
    2. Implement methods to read, write, and append tick data.
*   **Definition of Done:** Unit tests confirm that mock data can be written to and read from the new time-series storage.

### Task 6: Implement the Fallback/Router Logic
*   **Goal:** Integrate the Datastore with the API Gateway.
*   **Context:** API route handlers.
*   **Instructions for AI:**
    1. Update the dependency injected in Task 3.
    2. Logic flow: When a request comes in, check the Time-Series DB first. If data is stale or missing, call the Provider interface to fetch fresh data, save it to the Time-Series DB, and return it.
*   **Definition of Done:** The API serves cached data from the Time-Series DB and only hits the scraper when absolutely necessary.

---

## Phase 3: Event-Driven Push Architecture (Inspiration: vn.py)
**Goal:** Transition from a pure REST polling model to a real-time event-driven system with WebSockets.

### Task 7: Implement an Internal Event Bus
*   **Goal:** Create a pub/sub mechanism within the FastAPI application.
*   **Context:** `app/core/events.py`.
*   **Instructions for AI:**
    1. Implement a lightweight asynchronous event bus using `asyncio.Queue` or `anyio` memory object streams.
    2. Create topic definitions (e.g., `market_data.tick.{symbol}`).
*   **Definition of Done:** A service can publish a message to a topic, and a subscriber can receive it asynchronously.

### Task 8: Emit Events on Data Ingestion
*   **Goal:** Connect the Provider/Storage layer to the Event Bus.
*   **Context:** The Gateway router created in Task 6.
*   **Instructions for AI:**
    1. Modify the logic so that whenever fresh data is fetched from the provider and saved to the Time-Series DB, an event containing the new tick data is published to the Event Bus.
*   **Definition of Done:** Fetching data via REST automatically triggers an internal event.

### Task 9: Implement WebSocket Endpoints
*   **Goal:** Allow clients to subscribe to real-time updates without polling.
*   **Context:** `app/api/websockets.py`.
*   **Instructions for AI:**
    1. Create a FastAPI WebSocket endpoint `/ws/market-data`.
    2. Implement logic for clients to subscribe to specific stock symbols.
    3. When the Event Bus receives a tick for a subscribed symbol, push the data to the connected client.
*   **Definition of Done:** A WebSocket client can connect, subscribe to "AAPL", and receive real-time JSON payloads whenever "AAPL" is updated in the system.

---

## Phase 4: Cleanup & Legacy Deprecation
**Goal:** Remove old, unused infrastructure to reduce technical debt.

### Task 10: Deprecate Dynamic SQLAlchemy Tables
*   **Goal:** Remove `stocks_dict_engine` and `today_chart_engine`.
*   **Context:** `app/db.py`, `app/models/`.
*   **Instructions for AI:**
    1. Verify all routes and internal systems are using the new Gateway and Time-Series DB.
    2. Delete the legacy dynamic table creation logic.
    3. Update `app/main.py` startup events to no longer bind these engines.
*   **Definition of Done:** The codebase is free of `stocks_dict` and `today_chart` legacy code, and tests pass.

### Task 11: Final Integration Testing
*   **Goal:** Ensure the entire pipeline works end-to-end.
*   **Context:** `tests/integration/`.
*   **Instructions for AI:**
    1. Write tests that simulate a WebSocket connection, a REST request triggering a scrape, data being saved to the Time-Series DB, and the WebSocket receiving the broadcasted event.
*   **Definition of Done:** 100% pass rate on integration tests demonstrating the full Event-Driven Gateway architecture.