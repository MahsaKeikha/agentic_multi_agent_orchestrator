from __future__ import annotations

from typing import Any, Dict, Iterable, List


def summarize_trace(trace: Iterable[Dict[str, Any]]) -> List[str]:
    return [f"{item.get('step')}: {item.get('actor')} | {item.get('event')}" for item in trace]
