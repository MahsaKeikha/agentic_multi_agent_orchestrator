from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from SKILLS.safety_review import assess_safety


@dataclass(frozen=True)
class SafetyAgent:
    name: str = "safety_agent"

    def run(self, state: Any) -> Dict[str, Any]:
        assessment = assess_safety(state.case, state.analyses)
        state.analyses[self.name] = assessment
        state.record(self.name, "evaluated safety gate", assessment)
        state.risks.extend(assessment["risks"])
        return assessment
