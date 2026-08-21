from orchestration import run_system


def clean_case():
    return {
        "goal": "Coordinate a specialist workflow",
        "specialists": ["research_agent"],
        "requires_human_approval": True,
    }


def test_clean_run_waits_for_human_approval():
    assert run_system(clean_case())["status"] == "awaiting_human_approval"


def test_clean_run_can_be_approved():
    assert run_system(clean_case(), approve=True)["status"] == "approved_for_human_follow_through"


def test_missing_specialist_blocks():
    case = clean_case()
    case["specialists"] = []
    assert run_system(case, approve=True)["status"] == "blocked"


def test_trace_contains_all_agents_and_gate():
    result = run_system(clean_case())
    actors = [item["actor"] for item in result["trace"]]
    for expected in ["planner_agent", "router_agent", "execution_agent", "critic_agent", "safety_agent", "orchestrator"]:
        assert expected in actors
