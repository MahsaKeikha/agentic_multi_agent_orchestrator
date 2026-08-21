from __future__ import annotations

from typing import Any, Dict, List


def review_run(analyses: Dict[str, Any]) -> Dict[str, List[str]]:
    conflicts: List[str] = []
    plan = analyses.get("planner_agent", {}).get("steps", [])
    route = analyses.get("router_agent", {}).get("selected")
    execution = analyses.get("execution_agent", {})

    if not plan:
        conflicts.append("No execution plan is available")
    if plan and route is None:
        conflicts.append("A plan exists but no specialist route is available")
    if route is not None and execution:
        if execution.get("selected_specialist") != route:
            conflicts.append("Execution specialist does not match the router decision")
        if not execution.get("blocked") and execution.get("result") is None:
            conflicts.append("Execution reported success without a result")

    return {"conflicts": conflicts}
