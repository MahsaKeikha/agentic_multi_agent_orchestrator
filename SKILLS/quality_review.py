from __future__ import annotations

from typing import Any, Dict, List


def review_run(analyses: Dict[str, Any]) -> Dict[str, List[str]]:
    conflicts: List[str] = []
    plan = analyses.get("planner_agent", {}).get("steps", [])
    route = analyses.get("router_agent", {}).get("selected")
    if plan and route is None:
        conflicts.append("A plan exists but no specialist route is available")
    return {"conflicts": conflicts}
