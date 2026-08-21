from __future__ import annotations

from typing import Any, Dict

from AGENTS.critic_agent import CriticAgent
from AGENTS.execution_agent import ExecutionAgent
from AGENTS.planner_agent import PlannerAgent
from AGENTS.router_agent import RouterAgent
from AGENTS.safety_agent import SafetyAgent
from orchestration.state import RunState


SYSTEM_ID = "F36"
SYSTEM_NAME = "Agentic Multi Agent Orchestrator"
VERSION = "0.1.0"


def run_system(case: Dict[str, Any], approve: bool = False) -> Dict[str, Any]:
    state = RunState(case=case)
    state.record("orchestrator", "run started", {"system_id": SYSTEM_ID, "version": VERSION})

    for agent in [PlannerAgent(), RouterAgent(), ExecutionAgent(), CriticAgent(), SafetyAgent()]:
        agent.run(state)

    blockers = bool(state.unresolved_questions or state.conflicts or state.risks)
    if blockers:
        status = "blocked"
    elif approve:
        status = "approved_for_human_follow_through"
    else:
        status = "awaiting_human_approval"

    state.record("orchestrator", "approval gate evaluated", {"approve": approve, "status": status})
    return {
        "system_id": SYSTEM_ID,
        "system_name": SYSTEM_NAME,
        "version": VERSION,
        "run_id": state.run_id,
        "analyses": state.analyses,
        "evidence": state.evidence,
        "unresolved_questions": state.unresolved_questions,
        "conflicts": state.conflicts,
        "risks": state.risks,
        "status": status,
        "trace": state.trace,
    }
