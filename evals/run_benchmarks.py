from __future__ import annotations

import json
from pathlib import Path

from orchestration import run_system


def main() -> int:
    scenarios = json.loads(Path("benchmarks/scenarios.json").read_text())
    failures = []
    for scenario in scenarios:
        result = run_system({
            "goal": scenario["goal"],
            "specialists": scenario["specialists"],
            "requires_human_approval": True,
        })
        route = result.get("analyses", {}).get("router_agent", {}).get("selected")
        if route != scenario["expected_route"] or result["status"] != scenario["expected_status"]:
            failures.append({"id": scenario["id"], "route": route, "status": result["status"]})

    report = {"total": len(scenarios), "passed": len(scenarios) - len(failures), "failures": failures}
    print(json.dumps(report, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
