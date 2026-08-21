from __future__ import annotations

from typing import Any, Dict, List


def decompose_task(case: Dict[str, Any]) -> Dict[str, List[str]]:
    requested = str(case.get("goal", "")).strip()
    if not requested:
        return {"steps": []}
    steps = [step.strip() for step in case.get("steps", []) if str(step).strip()]
    return {"steps": steps or ["analyze goal", "select specialist", "review result"]}
