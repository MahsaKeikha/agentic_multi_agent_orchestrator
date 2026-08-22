from __future__ import annotations

from typing import Any, Dict, Optional

from AGENTS.critic_agent import CriticAgent
from AGENTS.execution_agent import ExecutionAgent
from AGENTS.planner_agent import PlannerAgent
from AGENTS.router_agent import RouterAgent
from AGENTS.safety_agent import SafetyAgent
from orchestration.state import RunState
from safety.approval_gate import can_approve
from TOOLS.specialist_registry import SpecialistRegistry, default_registry

SYSTEM_ID = "F36"
SYSTEM_NAME = "Agentic Multi Agent Orchestrator"
VERSION = "1.0.0"
MATURITY = "L3 Gold Standard"


def run_system(
    case: Dict[str, Any],
    approve: bool = False,
    registry: Optional[SpecialistRegistry] = None,
) -> Dict[str, Any]:
    active_registry = registry or default_registry()
    state = RunState(case=dict(case))
    state.record("orchestrator", "run started", {"system_id": SYSTEM_ID, "version": VERSION, "maturity": MATURITY})

    PlannerAgent().run(state)
    if not state.unresolved_questions:
        RouterAgent().run(state, active_registry)
    if not state.unresolved_questions:
        ExecutionAgent().run(state, active_registry)

    CriticAgent().run(state)
    SafetyAgent().run(state)

    eligible = can_approve(state.unresolved_questions, state.conflicts, state.risks)
    if not eligible:
        status = "blocked"
    elif approve:
        status = "approved_for_human_follow_through"
        state.approvals.append({"actor": "human", "approved": True})
    else:
        status = "awaiting_human_approval"

    state.record("orchestrator", "approval gate evaluated", {"approve_requested": approve, "eligible": eligible, "status": status})
    return {
        "system_id": SYSTEM_ID,
        "system_name": SYSTEM_NAME,
        "version": VERSION,
        "maturity": MATURITY,
        "run_id": state.run_id,
        "analyses": state.analyses,
        "evidence": state.evidence,
        "unresolved_questions": state.unresolved_questions,
        "conflicts": state.conflicts,
        "risks": state.risks,
        "tool_calls": state.tool_calls,
        "approvals": state.approvals,
        "status": status,
        "trace": state.trace,
    }
