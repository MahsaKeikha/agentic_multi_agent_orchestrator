from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from SKILLS.execution_policy import prepare_execution
from TOOLS.specialist_registry import SpecialistRegistry


@dataclass(frozen=True)
class ExecutionAgent:
    name: str = "execution_agent"

    def run(self, state: Any, registry: SpecialistRegistry) -> Dict[str, Any]:
        result = prepare_execution(state.case, state.analyses, registry)
        state.analyses[self.name] = result
        state.record(self.name, "executed selected specialist", result)
        state.record_tool_call("specialist_registry.invoke", {"selected": result.get("selected_specialist")}, result.get("result"), ok=not result["blocked"])
        if result["blocked"]:
            state.risks.extend(result["reasons"])
        elif result.get("result"):
            state.add_evidence(result["selected_specialist"], str(result["result"]), confidence=0.8)
        return result
