import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import run_system  # noqa: E402

result = run_system({"goal": "research evidence", "specialists": ["research_agent"]})
assert result["status"] == "awaiting_human_approval"
print(result["status"])
