from __future__ import annotations

from typing import Any, Dict

from TOOLS.specialist_registry import SpecialistRegistry


def choose_route(case: Dict[str, Any], analyses: Dict[str, Any], registry: SpecialistRegistry) -> Dict[str, Any]:
    allowed = [str(item) for item in case.get("specialists", registry.names()) if str(item).strip()]
    candidates = [name for name in allowed if registry.get(name) is not None]
    preferred = str(case.get("preferred_specialist", "")).strip()
    goal = str(case.get("goal", "")).strip()

    if preferred and preferred in candidates:
        return {"selected": preferred, "reason": "explicit_preference", "scores": {preferred: registry.score(preferred, goal)}}

    if not candidates:
        return {"selected": None, "reason": "no_eligible_specialist", "scores": {}}

    scores = {name: registry.score(name, goal) for name in candidates}
    best_score = max(scores.values())
    best = sorted(name for name, score in scores.items() if score == best_score)

    if best_score == 0 and len(candidates) > 1:
        return {"selected": None, "reason": "ambiguous_capability_match", "scores": scores}

    return {"selected": best[0], "reason": "capability_match", "scores": scores}
