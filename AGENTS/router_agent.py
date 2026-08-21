from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from SKILLS.routing_policy import choose_route
from TOOLS.specialist_registry import SpecialistRegistry


@dataclass(frozen=True)
class RouterAgent:
    name: str = "router_agent"

    def run(self, state: Any, registry: SpecialistRegistry) -> Dict[str, Any]:
        route = choose_route(state.case, state.analyses, registry)
        state.analyses[self.name] = route
        state.record(self.name, "selected agent route", route)
        if route["selected"] is None:
            state.unresolved_questions.append(f"Routing unresolved: {route['reason']}")
        return route
