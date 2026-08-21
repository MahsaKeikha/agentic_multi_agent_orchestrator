from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from SKILLS.quality_review import review_run


@dataclass(frozen=True)
class CriticAgent:
    name: str = "critic_agent"

    def run(self, state: Any) -> Dict[str, Any]:
        review = review_run(state.analyses)
        state.analyses[self.name] = review
        state.record(self.name, "reviewed run quality", review)
        state.conflicts.extend(review["conflicts"])
        return review
