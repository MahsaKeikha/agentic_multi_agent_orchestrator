from __future__ import annotations

from typing import Any, Dict


def prepare_execution(case: Dict[str, Any], analyses: Dict[str, Any]) -> Dict[str, Any]:
    route = analyses.get("router_agent", {}).get("selected")
    blocked = route is None
    reasons = ["No specialist route selected"] if blocked else []
    return {"selected_specialist": route, "blocked": blocked, "reasons": reasons}
