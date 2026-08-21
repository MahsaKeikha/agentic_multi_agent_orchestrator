from __future__ import annotations

from typing import Any, Dict, List


def assess_safety(case: Dict[str, Any], analyses: Dict[str, Any]) -> Dict[str, List[str]]:
    risks: List[str] = []
    if case.get("requires_human_approval", True) is False:
        risks.append("Human approval requirement is disabled")
    if analyses.get("execution_agent", {}).get("blocked"):
        risks.append("Execution is blocked")
    return {"risks": risks}
