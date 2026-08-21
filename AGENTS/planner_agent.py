from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from SKILLS.task_decomposition import decompose_task


@dataclass(frozen=True)
class PlannerAgent:
    name: str = "planner_agent"

    def run(self, state: Any) -> Dict[str, Any]:
        plan = decompose_task(state.case)
        state.analyses[self.name] = plan
        state.record(self.name, "created execution plan", plan)
        if not plan["steps"]:
            state.unresolved_questions.append("No executable steps were produced")
        return plan
