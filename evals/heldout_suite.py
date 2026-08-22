import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import run_system  # noqa: E402

SCENARIOS = [
    ("research_route", {"goal": "research evidence", "specialists": ["research_agent", "engineering_agent"]}, False, "awaiting_human_approval"),
    ("engineering_route", {"goal": "engineering architecture", "specialists": ["research_agent", "engineering_agent"]}, False, "awaiting_human_approval"),
    ("approved_research", {"goal": "research evidence", "specialists": ["research_agent"]}, True, "approved_for_human_follow_through"),
    ("ambiguous_goal", {"goal": "help me", "specialists": ["research_agent", "engineering_agent"]}, False, "blocked"),
    ("unknown_specialist", {"goal": "research evidence", "specialists": ["unknown_agent"]}, False, "blocked"),
    ("empty_goal", {"goal": "", "specialists": ["research_agent"]}, False, "blocked"),
    ("approval_cannot_fix_ambiguity", {"goal": "help me", "specialists": ["research_agent", "engineering_agent"]}, True, "blocked"),
    ("traceable_execution", {"goal": "engineering design", "specialists": ["engineering_agent"]}, False, "awaiting_human_approval"),
]


def main():
    rows = []
    for name, case, approve, expected in SCENARIOS:
        result = run_system(case, approve=approve)
        passed = result["status"] == expected
        if name == "traceable_execution":
            passed = passed and bool(result["trace"]) and bool(result["tool_calls"]) and bool(result["evidence"])
        rows.append({"scenario": name, "expected": expected, "actual": result["status"], "passed": passed})
    passed = sum(row["passed"] for row in rows)
    report = {"system_id": "F36", "version": "1.0.0", "scenario_count": len(rows), "passed": passed, "pass_rate": passed / len(rows), "scenarios": rows}
    Path("benchmarks").mkdir(exist_ok=True)
    Path("benchmarks/heldout_results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if report["pass_rate"] != 1.0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
