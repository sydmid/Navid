from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.core.events import event_bus
import asyncio

router = APIRouter()

@router.websocket("/market-data")
async def websocket_endpoint(websocket: WebSocket, symbol: str):
    await websocket.accept()
    topic = f"market_data.tick.{symbol}"
    queue = event_bus.subscribe(topic)

    async def wait_for_disconnect():
        try:
            while True:
                await websocket.receive()
        except WebSocketDisconnect:
            return

    async def send_messages():
        while True:
            data = await queue.get()
            await websocket.send_json({"symbol": symbol, "data": data})

    try:
        # Run both tasks concurrently. If client disconnects, receive() will raise WebSocketDisconnect
        send_task = asyncio.create_task(send_messages())
        disconnect_task = asyncio.create_task(wait_for_disconnect())

        done, pending = await asyncio.wait(
            [send_task, disconnect_task],
            return_when=asyncio.FIRST_COMPLETED
        )

        for task in pending:
            task.cancel()
    finally:
        event_bus.unsubscribe(topic, queue)
