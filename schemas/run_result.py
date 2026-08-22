from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class RunResult:
    system_id: str
    system_name: str
    version: str
    run_id: str
    analyses: Dict[str, Any]
    evidence: List[Dict[str, Any]]
    unresolved_questions: List[str]
    conflicts: List[str]
    risks: List[str]
    tool_calls: List[Dict[str, Any]]
    approvals: List[Dict[str, Any]]
    status: str
    trace: List[Dict[str, Any]]
