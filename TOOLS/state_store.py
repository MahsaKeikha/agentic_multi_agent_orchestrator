from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict


class InMemoryStateStore:
    def __init__(self) -> None:
        self._runs: Dict[str, Dict[str, Any]] = {}

    def save(self, run_id: str, payload: Dict[str, Any]) -> None:
        self._runs[run_id] = deepcopy(payload)

    def load(self, run_id: str) -> Dict[str, Any]:
        return deepcopy(self._runs[run_id])
