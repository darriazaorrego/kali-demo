"""
Lightweight pub/sub. Every meaningful combat event is logged here.
Later phases (replay, analytics, instructor tools) subscribe without
touching core logic.
"""
from collections import defaultdict
from typing import Callable, Any


class EventBus:
    def __init__(self):
        self._subs: dict[str, list[Callable]] = defaultdict(list)

    def subscribe(self, event: str, handler: Callable[[Any], None]) -> None:
        self._subs[event].append(handler)

    def publish(self, event: str, payload: Any) -> None:
        for handler in self._subs[event]:
            handler(payload)
