from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, Optional


@dataclass(frozen=True)
class Specialist:
    name: str
    capabilities: tuple[str, ...]
    handler: Callable[[Dict[str, Any]], Dict[str, Any]]


class SpecialistRegistry:
    def __init__(self) -> None:
        self._items: Dict[str, Specialist] = {}

    def register(self, name: str, capabilities: Iterable[str], handler: Callable[[Dict[str, Any]], Dict[str, Any]]) -> None:
        normalized = tuple(sorted({str(item).strip().lower() for item in capabilities if str(item).strip()}))
        self._items[name] = Specialist(name=name, capabilities=normalized, handler=handler)

    def get(self, name: str) -> Optional[Specialist]:
        return self._items.get(name)

    def names(self) -> list[str]:
        return sorted(self._items)

    def score(self, name: str, goal: str) -> int:
        specialist = self._items[name]
        tokens = {token.strip(".,:;!?()[]{}").lower() for token in goal.split() if token.strip()}
        return sum(1 for capability in specialist.capabilities if capability in tokens)

    def invoke(self, name: str, case: Dict[str, Any]) -> Dict[str, Any]:
        specialist = self._items[name]
        return specialist.handler(dict(case))


def default_registry() -> SpecialistRegistry:
    registry = SpecialistRegistry()
    registry.register(
        "research_agent",
        ["research", "evidence", "literature", "analysis"],
        lambda case: {"specialist": "research_agent", "finding": f"Research analysis prepared for: {case.get('goal', '')}"},
    )
    registry.register(
        "engineering_agent",
        ["engineering", "architecture", "system", "design", "implementation"],
        lambda case: {"specialist": "engineering_agent", "finding": f"Engineering analysis prepared for: {case.get('goal', '')}"},
    )
    return registry
