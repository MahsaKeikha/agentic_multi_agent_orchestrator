import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import run_system  # noqa: E402

case = {"goal": "engineering architecture design", "specialists": ["engineering_agent", "research_agent"]}
result = run_system(case, approve=True)
assert result["status"] == "approved_for_human_follow_through"
assert result["tool_calls"]
assert result["evidence"]
print(result["status"], result["analyses"].get("router_agent"))
