from __future__ import annotations

from typing import Any, Dict, Optional


def choose_route(case: Dict[str, Any], analyses: Dict[str, Any]) -> Dict[str, Optional[str]]:
    specialists = [str(item) for item in case.get("specialists", []) if str(item).strip()]
    requested = str(case.get("preferred_specialist", "")).strip()
    if requested and requested in specialists:
        return {"selected": requested}
    return {"selected": specialists[0] if specialists else None}
