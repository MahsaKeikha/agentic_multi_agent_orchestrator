from __future__ import annotations

from typing import Any, Dict

from TOOLS.specialist_registry import SpecialistRegistry


def prepare_execution(case: Dict[str, Any], analyses: Dict[str, Any], registry: SpecialistRegistry) -> Dict[str, Any]:
    route = analyses.get("router_agent", {}).get("selected")
    if route is None:
        return {"selected_specialist": None, "blocked": True, "reasons": ["No specialist route selected"], "result": None}

    try:
        output = registry.invoke(route, case)
    except Exception as exc:  # defensive boundary around specialist execution
        return {
            "selected_specialist": route,
            "blocked": True,
            "reasons": [f"Specialist execution failed: {type(exc).__name__}"],
            "result": None,
        }

    return {"selected_specialist": route, "blocked": False, "reasons": [], "result": output}
