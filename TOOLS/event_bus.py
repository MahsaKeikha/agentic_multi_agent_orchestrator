from __future__ import annotations

from typing import Any, Dict, List


class EventBus:
    def __init__(self) -> None:
        self.events: List[Dict[str, Any]] = []

    def publish(self, event: Dict[str, Any]) -> None:
        self.events.append(dict(event))

    def snapshot(self) -> List[Dict[str, Any]]:
        return [dict(event) for event in self.events]
