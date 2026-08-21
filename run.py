from __future__ import annotations

import json

from orchestration import run_system


if __name__ == "__main__":
    case = {
        "goal": "Coordinate a multi agent analysis",
        "specialists": ["research_agent", "engineering_agent"],
        "requires_human_approval": True,
    }
    print(json.dumps(run_system(case), indent=2))
