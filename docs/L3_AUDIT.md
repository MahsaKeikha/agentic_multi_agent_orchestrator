# F36 L3 Gold Standard Audit

F36 is eligible for L3 only when the promotion commit proves all of the following:

- capability-based routing with no arbitrary first-specialist fallback
- real specialist invocation through a registry
- specialist failure containment and explicit blocking on ambiguity
- evidence, tool-call provenance, chronological trace, risks, conflicts, unresolved questions, and approvals in shared state
- human approval required after automated gates and unable to override blockers
- unit, integration, adversarial, and malformed-input tests
- deterministic primary benchmark scenarios
- separate eight-scenario held-out reproducibility suite with 100% expected-behavior pass rate
- clean-checkout minimal and complete examples
- Python 3.10, 3.11, and 3.12 CI green
- held-out result artifact published by Python 3.12
- version 1.0.0 and MIT licensing/citation/governance metadata

L3 denotes a reproducible, independently reviewable orchestration reference implementation. It does not imply autonomous authority, universal routing correctness, or production suitability without environment-specific validation.
