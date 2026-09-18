import asyncio
from typing import Dict, List, Callable, Any

class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[asyncio.Queue]] = {}

    def subscribe(self, topic: str) -> asyncio.Queue:
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        queue = asyncio.Queue()
        self.subscribers[topic].append(queue)
        return queue

    def unsubscribe(self, topic: str, queue: asyncio.Queue) -> None:
        if topic in self.subscribers:
            if queue in self.subscribers[topic]:
                self.subscribers[topic].remove(queue)

    async def publish(self, topic: str, message: Any) -> None:
        if topic in self.subscribers:
            for queue in self.subscribers[topic]:
                await queue.put(message)

event_bus = EventBus()
