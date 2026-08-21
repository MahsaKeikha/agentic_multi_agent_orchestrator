from orchestration import run_system
from TOOLS.specialist_registry import SpecialistRegistry


def clean_case():
    return {
        "goal": "research evidence for a system decision",
        "specialists": ["research_agent", "engineering_agent"],
        "requires_human_approval": True,
    }


def test_capability_routing_selects_research_agent():
    result = run_system(clean_case())
    assert result["analyses"]["router_agent"]["selected"] == "research_agent"
    assert result["analyses"]["router_agent"]["reason"] == "capability_match"


def test_selected_specialist_is_actually_invoked():
    result = run_system(clean_case())
    execution = result["analyses"]["execution_agent"]
    assert execution["blocked"] is False
    assert execution["result"]["specialist"] == "research_agent"
    assert result["tool_calls"]
    assert result["evidence"]


def test_clean_run_waits_for_human_approval():
    assert run_system(clean_case())["status"] == "awaiting_human_approval"


def test_clean_run_can_be_approved():
    result = run_system(clean_case(), approve=True)
    assert result["status"] == "approved_for_human_follow_through"
    assert result["approvals"] == [{"actor": "human", "approved": True}]


def test_missing_specialist_blocks():
    case = clean_case()
    case["specialists"] = []
    assert run_system(case, approve=True)["status"] == "blocked"


def test_ambiguous_zero_score_routing_blocks_instead_of_guessing():
    case = clean_case()
    case["goal"] = "prepare an unrelated summary"
    result = run_system(case, approve=True)
    assert result["status"] == "blocked"
    assert result["analyses"]["router_agent"]["reason"] == "ambiguous_capability_match"


def test_disabling_human_approval_is_a_safety_blocker():
    case = clean_case()
    case["requires_human_approval"] = False
    result = run_system(case, approve=True)
    assert result["status"] == "blocked"
    assert "Human approval requirement is disabled" in result["risks"]


def test_specialist_failure_is_contained_and_blocks():
    registry = SpecialistRegistry()

    def failing_handler(case):
        raise RuntimeError("boom")

    registry.register("failing_agent", ["research"], failing_handler)
    case = {
        "goal": "research this problem",
        "specialists": ["failing_agent"],
        "requires_human_approval": True,
    }
    result = run_system(case, approve=True, registry=registry)
    assert result["status"] == "blocked"
    assert result["analyses"]["execution_agent"]["blocked"] is True


def test_trace_contains_agents_tool_call_and_gate():
    result = run_system(clean_case())
    actors = [item["actor"] for item in result["trace"]]
    for expected in ["planner_agent", "router_agent", "execution_agent", "critic_agent", "safety_agent", "tool_gateway", "orchestrator"]:
        assert expected in actors
