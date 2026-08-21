from __future__ import annotations

from typing import Dict, Iterable


def build_registry(agent_names: Iterable[str]) -> Dict[str, Dict[str, str]]:
    return {name: {"name": name, "status": "available"} for name in agent_names}
