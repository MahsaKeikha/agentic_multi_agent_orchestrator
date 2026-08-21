from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from SKILLS.execution_policy import prepare_execution


@dataclass(frozen=True)
class ExecutionAgent:
    name: str = "execution_agent"

    def run(self, state: Any) -> Dict[str, Any]:
        result = prepare_execution(state.case, state.analyses)
        state.analyses[self.name] = result
        state.record(self.name, "prepared execution", result)
        if result["blocked"]:
            state.risks.extend(result["reasons"])
        return result
