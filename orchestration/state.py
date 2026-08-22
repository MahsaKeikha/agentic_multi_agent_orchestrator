from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4


@dataclass
class RunState:
    case: Dict[str, Any]
    run_id: str = field(default_factory=lambda: str(uuid4()))
    analyses: Dict[str, Any] = field(default_factory=dict)
    evidence: List[Dict[str, Any]] = field(default_factory=list)
    unresolved_questions: List[str] = field(default_factory=list)
    conflicts: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)
    approvals: List[Dict[str, Any]] = field(default_factory=list)
    trace: List[Dict[str, Any]] = field(default_factory=list)

    def record(self, actor: str, event: str, artifact: Any = None) -> None:
        self.trace.append({
            "step": len(self.trace) + 1,
            "actor": actor,
            "event": event,
            "artifact": artifact,
        })

    def record_tool_call(self, tool: str, inputs: Dict[str, Any], output: Any, ok: bool = True) -> None:
        item = {"tool": tool, "inputs": inputs, "output": output, "ok": ok}
        self.tool_calls.append(item)
        self.record("tool_gateway", "tool invoked", item)

    def add_evidence(self, source: str, claim: str, confidence: float = 1.0) -> None:
        self.evidence.append({"source": source, "claim": claim, "confidence": confidence})
