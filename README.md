# F36 Agentic Multi Agent Orchestrator

F36 is a reference implementation for coordinating specialized AI agents through explicit planning, capability-based routing, bounded specialist execution, critique, safety review, provenance-aware state, and human approval.

## Why this repository exists

Many "multi-agent" examples are role names wrapped around one linear prompt. F36 instead makes the control plane visible: specialized agents have separate responsibilities, routing decisions are inspectable, specialist execution is bounded by a registry, failures become state, and consequential completion requires an explicit human gate.

## Architecture

1. `PlannerAgent` decomposes the requested goal.
2. `RouterAgent` scores eligible specialists against declared capabilities and blocks ambiguous zero-signal routing rather than guessing.
3. `ExecutionAgent` invokes the selected specialist through `SpecialistRegistry` and records the call and result.
4. `CriticAgent` checks workflow consistency.
5. `SafetyAgent` evaluates approval and execution risks.
6. The orchestrator applies the final human approval gate.

## Direct implementation links

- [Planner Agent](AGENTS/planner_agent.py)
- [Router Agent](AGENTS/router_agent.py)
- [Execution Agent](AGENTS/execution_agent.py)
- [Critic Agent](AGENTS/critic_agent.py)
- [Safety Agent](AGENTS/safety_agent.py)
- [Specialist Registry](TOOLS/specialist_registry.py)
- [Orchestrator](orchestration/orchestrator.py)
- [Run State](orchestration/state.py)
- [Approval Gate](safety/approval_gate.py)
- [Tests](tests/test_orchestrator.py)

## Quick start

```bash
python -m pip install -e '.[dev]'
python run.py
pytest -q
```

Core execution is deterministic and offline. The built-in specialists are intentionally local examples so tests and examples do not depend on an external model API.

## Safety model

F36 separates analysis from authority. A successful agent run does not automatically authorize an external action. Missing routing, specialist failure, unresolved conflicts, safety risks, or disabling the human-approval requirement blocks approval. See [docs/SAFETY.md](docs/SAFETY.md).

## Evaluation

The test suite covers capability routing, actual specialist invocation, evidence/tool-call traces, human approval, missing specialists, ambiguous routing, disabled approval requirements, and specialist failures. See [docs/EVALUATION.md](docs/EVALUATION.md).

## Maturity

**L2 candidate, not yet L3 Gold Standard.** This hardening release is designed to satisfy the verified-reference bar after CI and independent reproducibility checks. L3 should only be claimed after benchmark publication and independent validation.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Agents](docs/AGENTS.md)
- [Safety](docs/SAFETY.md)
- [Evaluation](docs/EVALUATION.md)
- [Extending F36](docs/EXTENDING.md)

## Citation and contribution

See `CITATION.cff`, `CONTRIBUTING.md`, and `SECURITY.md`.

## License

MIT. See `LICENSE`.
