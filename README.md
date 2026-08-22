# F36 Agentic Multi Agent Orchestrator

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

F36 is a reference implementation for coordinating specialized AI agents through explicit planning, capability-based routing, bounded specialist execution, critique, safety review, provenance-aware state, and human approval.

## Why this repository exists

Many multi-agent examples are role names wrapped around one linear prompt. F36 instead makes the control plane visible: specialized agents have separate responsibilities, routing decisions are inspectable, specialist execution is bounded by a registry, failures become state, and consequential completion requires an explicit human gate.

## Architecture

1. `PlannerAgent` decomposes the requested goal.
2. `RouterAgent` scores eligible specialists against declared capabilities and blocks ambiguous zero-signal routing rather than guessing.
3. `ExecutionAgent` invokes the selected specialist through `SpecialistRegistry` and records the call and result.
4. `CriticAgent` checks workflow consistency.
5. `SafetyAgent` evaluates approval and execution risks.
6. The orchestrator applies the final human approval gate.

## Reproduce

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python evals/run_benchmarks.py
python evals/heldout_suite.py
python examples/minimal.py
python examples/complete.py
python run.py
```

CI runs these gates on Python 3.10, 3.11, and 3.12 and publishes held-out results from Python 3.12.

## Safety model

F36 separates analysis from authority. A successful run never automatically authorizes an external action. Missing routing, specialist failure, unresolved conflicts, unresolved questions, safety risks, or failed approval eligibility block progression. Human approval is required after automated gates pass and cannot repair an active blocker.

## L3 evidence

L3 requires capability-based routing, real specialist invocation, evidence and tool-call provenance, failure containment, adversarial tests, deterministic primary benchmarks, a separate held-out reproducibility suite, clean-checkout examples, green multi-version CI, and published evaluation artifacts. See `docs/L3_AUDIT.md` and `benchmarks/RESULTS.md`.

L3 denotes a reproducible, independently reviewable reference implementation. It does not imply universal routing correctness or autonomous authority over consequential actions.

## Documentation

See `docs/ARCHITECTURE.md`, `docs/AGENTS.md`, `docs/SAFETY.md`, `docs/EVALUATION.md`, `docs/EXTENDING.md`, and `docs/L3_AUDIT.md`.

## Citation and contribution

See `CITATION.cff`, `CONTRIBUTING.md`, and `SECURITY.md`.

## License

MIT. See `LICENSE`.
